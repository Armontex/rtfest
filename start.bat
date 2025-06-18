@echo off
cd frontend/
echo Запускаем фронтенд...
start "" "cmd" /k "npm run dev"

cd ..
call venv\Scripts\activate
echo Запускаем бэкенд...
start "" "cmd" /k "uvicorn main:app --reload"