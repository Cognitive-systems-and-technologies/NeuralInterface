@echo off

set REPO_URL=https://github.com/Cognitive-systems-and-technologies/pythonProject
set PROJECT_DIR=C:\Projects\NeuralAlgorithmsInterface\pythonProject
set PROJECT_VENV=C:\Projects\NeuralAlgorithmsInterface

echo Installation Requirements
echo 1. Python not version less than 3.9
echo 2. GIT
echo Projection installation start.
echo Please wait.
echo To clone a repository, you need to verify your GIT account
echo The project will automatically be placed in the folder C:\Projects\NeuralAlgorithmsInterface
echo Creating and activating a virtual environment
python -m venv %PROJECT_VENV%\venv
call %PROJECT_VENV%\venv\Scripts\activate

echo Cloning a repository
git clone %REPO_URL% %PROJECT_DIR%

echo Installing dependencies
pip install -r %PROJECT_DIR%\requirements.txt

REM Collection of static files
python %PROJECT_DIR%\manage.py collectstatic --noinput

echo The project has been deployed successfully.