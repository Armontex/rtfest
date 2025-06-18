@echo off
REM Запуск FastAPI сервера с Uvicorn
call venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
pause