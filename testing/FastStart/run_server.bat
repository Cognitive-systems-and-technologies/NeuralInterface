@echo off
cd C:\Projects\NeuralInterface
call C:\Projects\NeuralInterface\venv\Scripts\activate

cd C:\Projects\NeuralInterface\NeuralInterface
start cmd /k "C:\Projects\NeuralInterface\venv\Scripts\python.exe manage.py runserver"

timeout /t 5

start "" "http://127.0.0.1:8000"