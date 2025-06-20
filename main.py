from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Base64Bytes, field_serializer, field_validator
from sqlalchemy import select, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

app = FastAPI()

# ----------------------------------------------------------
# Разрешите запросы от любых источников (для разработки)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене замените "*" на конкретные домены (например, ["http://localhost:5173"])
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешить все заголовки
)
# ----------------------------------------------------------

engine = create_async_engine("sqlite+aiosqlite:///events.db", echo=True)
session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with session_maker() as session:
        yield session

class Base(DeclarativeBase):
    pass

class EventModel(Base):
    __tablename__ = "events"
    id       : Mapped[int]   = mapped_column(primary_key=True)
    type     : Mapped[str]
    title    : Mapped[str]
    date     : Mapped[str]
    time     : Mapped[str]
    location : Mapped[str]
    cover    : Mapped[Optional[bytes]] = mapped_column(nullable=True)
    descr    : Mapped[str]

# Модель записи на мероприятие
class RegistrationModel(Base):
    __tablename__ = "registrations"
    id         : Mapped[int] = mapped_column(primary_key=True)
    event_id   : Mapped[int] = mapped_column(ForeignKey("events.id"))
    email      : Mapped[str]
    created_at : Mapped[str] = mapped_column(default=lambda: datetime.now().isoformat())

    event = relationship("EventModel")


class EventAddSchema(BaseModel):
    type     : str
    title    : str
    date     : str
    time     : str
    location : str
    cover    : Optional[bytes] = None
    descr    : str

class EventSchema(BaseModel):
    id       : int
    type     : str
    title    : str
    date     : str
    time     : str
    location : str
    cover    : Optional[str] = None
    descr    : str
    class Config:
        from_attributes = True


class EventDetailSchema(BaseModel):
    title    : str
    type     : str
    cover    : Optional[str] = None
    time     : str
    location : str
    descr    : str
    class Config:
        from_attributes = True


class RegistrationAddSchema(BaseModel):
    event_id: int
    email: str


FILTERS = [
    "cinema", "victorins", "computer_games", "quests", "master_class",
    "music", "board_games", "picnics", "sport",
    "dances", "standup", "festivals"
]

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}

@app.post("/events")
async def add_event(data: EventAddSchema, session: AsyncSession = Depends(get_session)):
    ev = EventModel(**data.model_dump())
    session.add(ev)
    await session.commit()
    return {"ok": True}

@app.get("/events", response_model=List[EventSchema])
async def get_events(
    session: AsyncSession = Depends(get_session),
    types: Optional[List[str]] = Query(
        None,
        description="фильтры по виду события (можно несколько), пример: /events?types=music&types=picnics"
    )
):
    query = select(EventModel)
    if types:
        invalid = set(types) - set(FILTERS)
        if invalid:
            raise HTTPException(400, detail=f"Unknown filter(s): {', '.join(invalid)}")
        query = query.where(EventModel.type.in_(types))
    result = await session.execute(query)
    return result.scalars().all()

@app.get("/event/{event_id}", response_model=EventDetailSchema)
async def get_event(event_id: int, session: AsyncSession = Depends(get_session)):
    ev = await session.get(EventModel, event_id)
    if not ev:
        raise HTTPException(404, "Event not found")
    return EventDetailSchema(
        title    = ev.title,
        type     = ev.type,
        cover    = ev.cover,
        time     = ev.time,
        location = ev.location,
        descr    = ev.descr
    )

# Запись пользователя на мероприятие
@app.post("/register")
async def register_user(data: RegistrationAddSchema, session: AsyncSession = Depends(get_session)):
    event = await session.get(EventModel, data.event_id)
    if not event:
        raise HTTPException(404, "Event not found")

    reg = RegistrationModel(event_id=data.event_id, email=data.email)
    session.add(reg)
    await session.commit()
    return {"ok": True}
