# Интерфейс для обучения агентов

## Описание

Целью проекта является разработка открытой библиотеки, реализующей алгоритмы глубокого иерархического обучения для
мобильных роботов и многоагентных систем на ARM-процессорах.

Библиотека будет применяться для обучения мобильных роботов, способных к коллективному взаимодействию с другими
роботами. Использование библиотеки позволит реализовывать мультиагентные системы на базе мобильных роботов и
интеллектуальные роботизированные системы на базе ARM процессоров, обучать их на выполнение пользовательских задач и
производить удаленное управление и мониторинг за счет локальных и веб интерфейсов.

## Подготовка к установке

1. Установите python с версией не менее 3.9.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/cef11f5a-3f76-4a7d-9b8d-bb3c2c39ad46

   Ссылка: https://www.python.org/downloads/

   Обязательно, установите в галочку в пункте "Add python.exe to path"
   Также, установите python для всех пользователей Windows.
2. Установите Git.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/blob/main/interface/static/video/InstallGit.mp4

   Ссылка: https://git-scm.com/downloads

## Установка

1. Создайте папку для проекта.

   Например: C:\Projects\NeuralInterface

2. Откройте командную строку и пропишите путь к папке, которую только что создали, используя команду:

   cd C:\Projects\NeuralInterface

3. Создайте виртуальное окружение с помощью команды:

   python -m venv venv

4. Активируйте виртуальное окружение с помощью команды:

   .\venv\Scripts\activate

5. Загрузите данные из репозитория с помощью команды:

   git clone https://github.com/Cognitive-systems-and-technologies/NeuralInterface

   Также, Вы можете сделать данное действие, без использования Git. Для этого нажмите на кнопку "Code", а затем в
   выпадающем меню нажмите Download ZIP. После этого распакуйте содержимое архива в папку C:
   \Projects\NeuralAlgorithmsInterface

6. Перейдите в папку проекта с помощью команды:

   cd C:\Projects\NeuralInterface\NeuralInterface

7. Установите зависимости с помощью команды:

   pip install -r requirements.txt

8. Запустите проект с помощью команды:

   python manage.py runserver

9. Откройте браузер на странице http://127.0.0.1:8000/

## Запуск

1. Откройте командную строку и пропишите путь к папке, в которой находится проект, используя команду:

   cd C:\Projects\NeuralInterface

2. Активируйте виртуальное окружение с помощью команды:

   .\venv\Scripts\activate

3. Перейдите в папку проекта с помощью команды:

   cd C:\Projects\NeuralInterface\NeuralInterface

4. Запустите проект с помощью команды:

   python manage.py runserver

5. Откройте браузер на странице http://127.0.0.1:8000/

## Решение возможных ошибок при установке

1. Ошибка:

   Невозможно загрузить файл D:\...\python\1_PyCharm\django\djsite\venv\Scripts\Activate.ps1, так
   как выполнение сценариев отключено в этой системе.

   Запустите командную строку от имени администратора и введите "powershel"

   Затем введите "Set-ExecutionPolicy RemoteSigned"

2. Если при установке виртуального окружения происходят ошибки или ничего не происходит при использовании команды
   "python -m venv venv", необходимо проверить правильность установки Python.
   Для того чтобы понять месторасположение Python, можно воспользоваться командой:

   where python

   Также, необходимо проверить была ли поставлена галочка в пункте "Add python.exe to path" при установке Python

## Использование

В самом сайте на странице "Информация о проекте" есть подробная инструкция по использованию

## Лицензия

Этот проект находится под лицензией [MIT License](LICENSE).
