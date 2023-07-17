# Интерфейс для обучения агентов

## Описание

Этот проект реализует алгоритм на основе нейронной сети для поиска выхода из лабиринта. Нейронная сеть учится перемещаться по лабиринту, обучаясь на наборе размеченных карт лабиринта.

Цель состоит в том, чтобы предоставить решение проблемы поиска кратчайшего пути от начальной точки до выхода из заданного лабиринта.

Данный проект создан для управления агентами и их данными, отображения актуальной информации об обучении агентов.

## Подготовка к установке
1. Установите python с версией не менее 3.9. 

   Ссылка: https://www.python.org/downloads/

   Обязательно, установите в галочку в пункте "Add python.exe to path"
   Также, установите python для всех пользователей Windows.
2. Установите Git.
   
   Ссылка: https://git-scm.com/downloads

## Автоматическая установка и запуск на ОС Windows.

1. Скопируйте два файла AutoStart.bat и AutoInstall.bat из папки auto_installation в любое удобное Вам место

2. Запустите файл AutoInstall.bat

   Файл создаст директорию "C:\Projects\NeuralAlgorithmsInterface" на Вашем компьютере и установит в неё проект, а также установит папку виртуальным окружением.

3. Запустите файл AutoStart.bat

   Файл активирует виртуальное окружение и откроет браузер со страницей сайта, после чего запустит сервер.

## Ручная установка и запуск

1. Откройте командную строку и пропишите путь к папке, в которой будет запускаться проект, используя команду: 
   
   cd C:\Projects\NeuralAlgorithmsInterface

   Замените C:\Projects\NeuralAlgorithmsInterface на необходимую Вам дерикторию. 

2. Создайте виртуальное окружение с помощью команды:
   
   python -m venv venv
   
3. Активируйте виртуальное окружение с помощью команды: 
   
   .\venv\Scripts\activate

4. Замените путь к папке с помощью команды:

   C:\Projects\NeuralAlgorithmsInterface\pythonProject

5. Загрузите данные из репозитория с помощью команды:
   
   git clone https://github.com/Cognitive-systems-and-technologies/pythonProject

   Git попросит Вас выполнить авторизацию для данного действия.
   
   Также, Вы можете сделать данное действие, без использования Git. Для этого нажмите на кнопку "Code", а затем в 
   выпадающем меню нажмите Download ZIP. После этого распакуйте содержимое архива в нужную папку.

6. Установите зависимости с помощью команды:

   pip install -r requirements.txt

7. Запустите проект с помощью команды:
   
   python manage.py runserver

Для  запука проекта вручную, необходимо выполнить пункты 1, 3, 4, 7.

## Решение возможных ошибок при установке
1. Ошибка:

   Невозможно загрузить файл D:\...\python\1_PyCharm\django\djsite\venv\Scripts\Activate.ps1, так 
   как выполнение сценариев отключено в этой системе. 

   Запустите командную строку от имени администратора и введите "powershel" 
   
   Затем введите "Set-ExecutionPolicy RemoteSigned"

2. Если при установке виртуального окружения происходят ошибки, необходимо проверить правильность установки Python. Для того, чтобы понять месторасположение Python, можно воспользоваться командой:

where python

## Использование

В самом сайте на странице "Информация о проекте" есть подробная инструкция по использованию

## Лицензия

Этот проект находится под лицензией [MIT License](LICENSE).
