@echo off

set SITE_URL=http://127.0.0.1:8000
set PROJECT_VENV=C:\Projects\NeuralAlgorithmsInterface

echo Activating the virtual environment
call %PROJECT_VENV%\venv\Scripts\activate

echo Opening the browser with the site and starting the server
start "" %SITE_URL% && python %PROJECT_VENV%\pythonProject\manage.py runserver

