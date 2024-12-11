# General description
NeuralInterface is a monitoring and visualization module used to display the work of agents (mobile robots).

This module is a web application with several pages displaying the current status of agents, their belonging to certain groups.

The functionality of direct control of agents is also implemented. You can set the direction of their movement, download and unload their status data, start or stop their training.

Practical application.

The library can be used in areas where it is necessary to develop systems using neural networks, deep machine learning models, and reinforcement learning of intelligent agents.

The developers consider the following areas to be the main areas of applied use of the library:
- warehouse logistics (programming industrial robots in warehouses);
- educational robotics (training in programming mobile robots using deep machine learning algorithms);
- smart home devices (robot vacuum cleaners and other devices that require autonomous operation without operator intervention).

This module is linked to the module:

https://github.com/Cognitive-systems-and-technologies/RoboAICore.

An example of the NeuralInterface module installed on a PC and linked to the RoboAICore module installed on an agent (mobile robot):

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/15780a6c-fa6e-4170-a1f9-37d5b954e09b

This video demonstrates the control of an agent using the NeuralInterface module. When you press the movement buttons, the mobile robot moves in the corresponding direction, you can also see the learning process of the mobile robot, changing the distance from the rangefinders designed to determine the distance to objects such as HC-SR04 located on the mobile robot.

To get a result similar to the one in the video, you need to install both library modules: NeuralInterface on a PC, RoboAICore on the STM32F4 debug board or Raspberry pi 3 (model B). The NeuralInterface module must be configured so that requests from the web application are sent to agents, receive and send a response. You also need to have a Yahboom Raspbot AI Vision Robot Car with FPV camera with three HC-SR04 ultrasonic sensors for determining distances to objects installed on it, an STM32F4 debug board or Raspberry pi 3 (model B) with the RoboAICore library installed on this debug board.
Otherwise, the NeuralInterface module will work in demo mode, without communication with agents, and when trying to send a request, it will return an error that will depend on the devices located in the local network and their states.

Agent characteristics.

To illustrate the example of the library operation, two Yahboom Raspbot AI Vision Robot Car with FPV camera robots were selected, on which three ultrasonic sensors for determining the distance to objects of the HC-SR04 type were installed, debug boards: one for the STM32 processor family of the STM32F4 series based on the ARM Cortex-M4 architecture, model STM32F429ZI with a bit depth of 32 bits, the second - Raspberry pi 3 (model B).
The operating frequency of the STM32F429ZI processor is 180 MHz, the size of the programmable memory is 2 MB, the amount of RAM is 256 KB.
Characteristics for raspberry pi: processor: 64-bit quad-core ARM Cortex-A53 with a clock frequency of 1.2 GHz on a single-crystal chip Broadcom BCM2837, RAM 1 GB LPDDR2 SDRAM.

Yahboom Raspbot AI Vision Robot Car with FPV camera specifications:

- Control controller: Raspberry Pi (not included).
- Programming language: Python.
- Degree of freedom (DOF): 2 degrees of freedom, 180° up, down, left, right.
- Steering: 15kg x 5 + 6kg x 1 serial bus servo.
- Data input: wide-angle camera, infrared obstacle avoidance sensor, IR receiver, ultrasonic distance measurement sensor, four-channel tracking sensor, IIC interface.
- Data output: servo, TT gear motor, passive serial interface buzzer.
- Remote control: mobile APP / PC / IR remote control.
- Sensor: ultrasonic, infrared obstacle avoidance, buzzer, LED.
- Communication method: Wi-Fi network, IR remote control.
- Protection: from overcurrent, from overvoltage.
- Functionality: tracking and recognition of colors, gesture recognition, recognition and tracking of faces, movement along a given trajectory, recognition and avoidance of obstacles, remote control capability.

## Why a web application?
Using the web server version of the NeuralInterface module instead of a desktop application allows you to deploy this project not only on the Windows operating system, but also on Linux, as well as on any server, allowing you to combine multiple devices even outside the local network.

## Requirements for running the NeuralInterface module on a PC
1. Operating system of your choice:
- Windows 7/8/10 64-rbit
- Linux (Ubuntu 18.04 LTS or newer recommended)
- macOS Big Sur (version 11) or newer
3. Processor: Intel Core i3 or AMD equivalent
4. RAM: 2 GB (4 GB or more recommended for more complex projects)
5. Hard Drive: 10 GB (minimum for Django and its dependencies)
6. Python: Python 3.9 or newer
7. pip package installer: Installed and configured for Python 3 (installed with python)
8. Git: Installed (Git version 2.0 or higher recommended)

The installation instructions are provided for Windows operating systems only.
## Preparing for installation

1. Install python with version at least 3.9.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/cef11f5a-3f76-4a7d-9b8d-bb3c2c39ad46

Link: https://www.python.org/downloads/

Make sure to check the box "Add python.exe to path"
Also, install python for all Windows users.
2. Install Git.

[InstallGit.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/c10de4e7-464e-4d73-89af-ec22ccf08b38)

Link: https://git-scm.com/downloads

## Installation

[InstallProject.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/6f259c2d-492f-4dbb-8bc3-079bdbe7bcd9)

1. Create a folder for the project.

For example: C:\Projects\NeuralInterface

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/2b48d108-8de3-482a-926c-7ac8ccfc7cdf)

3. Open a command prompt and specify the path to the folder you just created using the command:

cd C:\Projects\NeuralInterface

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/197cedf3-e042-4052-bf68-e27cf248f2d1)

5. Create a virtual environment using the command:

python -m venv venv

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/ddff6223-df93-4a33-90a6-87218f15f92c)

7. Activate the virtual environment with the command:

.\venv\Scripts\activate

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/09bbe463-7819-4577-8602-8f309a1a1afd)

9. Download the data from the repository with the command:

git clone https://github.com/Cognitive-systems-and-technologies/NeuralInterface

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/6028bae2-04c4-4f61-8c0c-9fb28f05a875)

You can also do this without using Git. To do this, click the "Code" button, and then in the
drop-down menu, click Download ZIP. After that, unzip the archive contents to the C:
\Projects\NeuralAlgorithmsInterface folder

9. Go to the project folder using the command:

cd C:\Projects\NeuralInterface\NeuralInterface

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/2b6042bf-54e7-4141-a61f-b2d67782e733)

11. Install dependencies using the command:

pip install -r requirements.txt

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/8a814552-d7b3-4294-b1f7-989c1c80d51b)

11. Run the project with the command:

python manage.py runserver

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/bbdc81f5-ba40-4231-a097-73c5e354e2de)

11. Open your browser on the page http://127.0.0.1:8000/

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/f17937c3-adf7-4b92-bfdf-ccf03633cc29)


## Fast Launch

Run file C:\Projects\NeuralInterface\NeuralInterface\testing\FastStart\run_server.bat

## Manual Launch

1. Open a command prompt and specify the path to the folder where the project is located using the command:

cd C:\Projects\NeuralInterface

2. Activate the virtual environment using the command:

.\venv\Scripts\activate

3. Go to the project folder using the command:

cd C:\Projects\NeuralInterface\NeuralInterface

4. Run the project using the command:

python manage.py runserver

5. Open a browser on the page http://127.0.0.1:8000/

## Troubleshooting possible installation errors

1. Error:

Unable to load file D:\...\python\1_PyCharm\django\djsite\venv\Scripts\Activate.ps1 because
script execution is disabled on this system.

Run the command prompt as administrator and type "powershel"

Then type "Set-ExecutionPolicy RemoteSigned"

2. If errors occur during the installation of the virtual environment or nothing happens when using the command
"python -m venv venv", you need to check that Python is installed correctly.
In order to understand the location of Python, you can use the command:

where python

You also need to check whether the "Add python.exe to path" checkbox was checked when installing Python

## Usage

The NeuralInterface module on the "Project Information" page has detailed instructions on how to use it. It is also described insame.
Use the link: http://127.0.0.1:8000/info/ to go to the instructions when you deploy the project.

Login and password from the admin panel:

Login: root | Password: 1234

## Testing the library in demo mode without robots.

To check the functionality of the library, in addition to running the NeuralInterface module itself, you must also run the requests.exe file in the C:\Projects\NeuralInterface\NeuralInterface\testing folder. This program simulates the robot API and adds data to the NeuralInterface module database.

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/e1026e9a-83a3-46a4-8bd3-642ff749dc6d)

After the program starts, the agent training data is simulated to be written to the NeuralInterface module database. Wait until the data writing process is complete.

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/325de00b-761b-42b0-9628-dc651e21af77)

After that, you can check the functionality of the "Monitoring" page. After each click on the button on the right side of the page, a request will be sent to the agent. Information about this can be seen in the console.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/17d5d939-c464-4f51-8621-1e01875254e5

# Description of each page
## Control panel
Allows you to work with data from the database. You can fully manage data only for tables with agents and agent groups. You can create, modify, and delete records from the corresponding tables. If you try to delete a record that is linked to another record in another table via a foreign key, the system will issue a warning that this cannot be done and that you must first delete all data so that the database retains the structure of the third normal form. Everything is done using buttons. When creating and modifying, a modal window opens to fill in or change data, respectively. The agent types table is static and contains default values. Other tables, if necessary, must be filled in through the site's administrative panel, which allows you to completely change the data.

Working with agents:

[Working with agents.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/bca3f481-fb6f-4aa0-bc3c-6b7be5d203b1)

Important! For the web application to work correctly, the MAC addresses and IP addresses of the agents must be unique. The data in the tables is linked by foreign keys. You cannot delete linked data. For example, you cannot delete an agent if there is data in the table with files for this agent or in any other table.

Working with groups:

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/18a031e6-caa7-4e54-8fae-f901c9257e4e

Important! Agent groups are subject to the same restrictions as agents themselves. For example, you cannot delete an agent group if at least one agent belongs to it.

## Monitoring
Displays information about agent training, and also allows you to manage agent data. By default, the first record from the agent errors table is always selected. The graph displays agent training data. When you select the required agent in the table, the graph is redrawed based on the error values ​​​​for a specific agent. The panel in the lower right part of the screen allows you to send the necessary commands to agents.

Working with the graph:

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/fb44d64e-dca6-4530-a515-6f2d56efe3ae

The buttons in the lower right part of the page are responsible for direct control and interaction with agents. When you click on a button, a request is sent, which, depending on the state of the agent, sends a certain response. As shown in the video, the server cannot find an agent in the local network with such an address and sends an error, which is displayed in full at the bottom of the page.

Important! The graph does not update automatically. To update the data, click on the graph update button at the top of the screen or on the line with the agent in the table

## Admin Panel
Login: root | Password: 1234

The Django admin panel is a built-in tool provided by Django for managing your web application data. It provides a convenient and powerful interface for working with models and data in your database without the need to create your own user interface.

Administrative panel view:

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/f22aa1a9-888e-4f31-b673-afd2f28e046a)

Login to the admin panel

1. Go to the admin panel page
Open a web browser and enter the admin panel address (usually /admin) in the address bar of the site or click "Admin panel" in the left menu
2. Log in
You will be asked to enter your credentials. Enter the login and password specified above

Important! Be careful when deleting, changing or adding data! Violation of the integrity of the database structure may result in unstable operation of the entire application. If you still need to change the database structure, add new tables, or change foreign keys, we recommend using the free Dbeaver program.

# License

This project is licensed under the [MIT License](LICENSE).

# Общее описание
NeuralInterface - это модуль мониторинга и визуализации, используемый для отображения работы агентов (мобильных роботов). 
Данный модуль представляет собой веб-приложение с несколькими страницами, отображающими текущий статус агентов, их принадлежность к определенным группам. 
Также реализован функционал прямого управления агентами. Можно задать направление их перемещения, загрузить и выгрузить данные их состояния, начать или прекратить их обучение. 

Практическое применение.

Библиотека может применяться в направлениях, где требуется разработка систем, использующих нейронные сети, модели глубокого машинного обучения, обучение с подкреплением интеллектуальных агентов. 
Основными направлениями прикладного использования библиотеки разработчики считают следующие сферы:
- складская логистика (программирование промышленных роботов на складах);
- образовательная робототехника (обучение программированию мобильных роботов используя алгоритмы глубокого машинного обучения);
- устройства систем умного дома (роботы-пылесосы и др. устройства требующие автономной работы без участия оператора).

Данный модуль связан с модулем:

https://github.com/Cognitive-systems-and-technologies/RoboAICore.

Пример работы модуля NeuralInterface установленным на ПК и связанным с модулем RoboAICore, установленным на агента (мобильного робота):

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/15780a6c-fa6e-4170-a1f9-37d5b954e09b

В данном видео продемонстрировано управление агентом с помощью модуля NeuralInterface. При нажатии на кнопки передвижения, мобильный робот перемещается в соответствующем направлении, также можно видеть процесс обучения мобильного робота, изменение расстояния от дальномеров, предназначенных для определения расстояний до объектов типа HC-SR04 расположенных на мобильном роботе.

Для получения подобного результата, как на видео, необходимо установить оба модуля библиотеки: NeuralInterface на ПК, RoboAICore на отладочную плату STM32F4 или Raspberry pi 3 (model B). Модуль NeuralInterface необходимо настроить таким образом, чтобы запросы из веб-приложения отправлялись на агентов, принимали и отсылали ответ. Также необходимо иметь в наличии робота Yahboom Raspbot AI Vision Robot Car with FPV camera с установленными на нем ультразвуковыми датчиками определения расстояний до объектов типа HC-SR04 в количестве трех, отладочную плату STM32F4 или Raspberry pi 3 (model B) с установленной библиотекой RoboAICore на данную отладочную плату. 
В противном случае, модуль NeuralInerface будет работать в демо режиме, без связи с агентами, и при попытке отправить запрос будет выдавать ошибку, которая будет зависеть от устройств, расположенных в локальной сети и их состояний.

Характеристики агентов.

Для иллюстрации примера работы библиотеки были выбраны два робота Yahboom Raspbot AI Vision Robot Car with FPV camera на которые были установлены ультразвуковые датчики определения расстояний до объектов типа HC-SR04 в количестве трех, отладочные платы: одна для семейства процессоров STM32 серии STM32F4 на базе архитектуры ARM Cortex-M4 модель STM32F429ZI разрядностью 32bit, вторая - Raspberry pi 3 (model B). 
Частота работы процессора STM32F429ZI - 180MHz, размер программируемой памяти 2MB, объем оперативной памяти 256KB. 
Характеристики для raspberry pi: процессор: 64-битный четырёхъядерный ARM Cortex-A53 с тактовой частотой 1,2 ГГц на однокристальном чипе Broadcom BCM2837, оперативная память 1ГБ LPDDR2 SDRAM.

Характеристики Yahboom Raspbot AI Vision Robot Car with FPV camera:

- Управляющий контроллер:	Raspberry Pi (не входит в комплект).
- Язык программирование: Python.
- Степень свободы (DOF): 2 степени свободы, 180° вверх, вниз, влево, вправо.
- Рулевое управление: 15 кг х 5 + 6 кг х 1 сервопривод с последовательной шиной.
- Ввод данных: широкоугольная камера, инфракрасный датчик обхода препятствий, ИК приёмник, ультразвуковой датчик измерения расстояния, четырехканальный датчик слежения, интерфейс IIC.
- Вывод данных: сервопривод, ТТ мотор-редуктор, пассивный зуммер последовательного интерфейса.
- Дистанционное управление: мобильное приложение/ПК/ИК пульт дистанционного управления.
- Датчик: ультразвуковой, инфракрасный обход препятствий, зуммер, светодиод.
- Метод связи: сеть Wi-Fi, ИК пульт.
- Защита: от перегрузки по току, от перенапряжения.
- Функциональные возможности: отслеживание и распознавание цветов, распознавание жестов, распознавание и отслеживание лиц, движение по заданной траектории, распознавание и объезд препятсвий, возможность дистанционного управления.

## Почему веб-приложение?
Использование веб-серверной версии модуля NeuralInterface вместо десктопного приложения позволяет развернуть данный проект не только на операционной 
системе Windows, но и на Linux, а также на любом сервере, позволяя объединять множество устройств даже вне локальной сети.

## Требования для запуска модуля NeuralInterface на ПК 
1. Операционная система на выбор:
   - Windows 7/8/10 64-разрядная
   - Linux (рекомендуется Ubuntu 18.04 LTS или более новая версия)
   - macOS Big Sur (версия 11) или более новая
3. Процессор: Intel Core i3 или эквивалентный AMD
4. Оперативная память (RAM): 2 ГБ (рекомендуется 4 ГБ и более для более сложных проектов)
5. Жесткий диск: 10 ГБ (минимально для Django и его зависимостей)
6. Python: Python 3.9 или более новая версия
7. Установщик пакетов pip: Установлен и настроен для Python 3 (устанавливается вместе с python)
8. Git: Установлен (рекомендуется версия Git 2.0 и выше)

Инструкция по установке представлена только для операционной системы Windows 

## Подготовка к установке

1. Установите python с версией не менее 3.9.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/cef11f5a-3f76-4a7d-9b8d-bb3c2c39ad46

   Ссылка: https://www.python.org/downloads/

   Обязательно, установите галочку в пункте "Add python.exe to path"
   Также, установите python для всех пользователей Windows.
2. Установите Git.

[InstallGit.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/c10de4e7-464e-4d73-89af-ec22ccf08b38)

   Ссылка: https://git-scm.com/downloads

## Установка

[InstallProject.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/6f259c2d-492f-4dbb-8bc3-079bdbe7bcd9)

1. Создайте папку для проекта.

   Например: C:\Projects\NeuralInterface

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/2b48d108-8de3-482a-926c-7ac8ccfc7cdf)

3. Откройте командную строку и пропишите путь к папке, которую только что создали, используя команду:

   cd C:\Projects\NeuralInterface

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/197cedf3-e042-4052-bf68-e27cf248f2d1)

5. Создайте виртуальное окружение с помощью команды:

   python -m venv venv

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/ddff6223-df93-4a33-90a6-87218f15f92c)

7. Активируйте виртуальное окружение с помощью команды:

   .\venv\Scripts\activate

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/09bbe463-7819-4577-8602-8f309a1a1afd)

9. Загрузите данные из репозитория с помощью команды:

   git clone https://github.com/Cognitive-systems-and-technologies/NeuralInterface

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/6028bae2-04c4-4f61-8c0c-9fb28f05a875)

   Также, Вы можете сделать данное действие, без использования Git. Для этого нажмите на кнопку "Code", а затем в
   выпадающем меню нажмите Download ZIP. После этого распакуйте содержимое архива в папку C:
   \Projects\NeuralAlgorithmsInterface

9. Перейдите в папку проекта с помощью команды:

   cd C:\Projects\NeuralInterface\NeuralInterface

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/2b6042bf-54e7-4141-a61f-b2d67782e733)

11. Установите зависимости с помощью команды:

   pip install -r requirements.txt

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/8a814552-d7b3-4294-b1f7-989c1c80d51b)

11. Запустите проект с помощью команды:

   python manage.py runserver

   ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/bbdc81f5-ba40-4231-a097-73c5e354e2de)

11. Откройте браузер на странице http://127.0.0.1:8000/

    ![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/f17937c3-adf7-4b92-bfdf-ccf03633cc29)

## Быстрый запуск

Запустите файл C:\Projects\NeuralInterface\NeuralInterface\testing\FastStart\run_server.bat

## Ручной запуск

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

   Также необходимо проверить, была ли поставлена галочка в пункте "Add python.exe to path" при установке Python

## Использование

В модуле NeuralInterface на странице "Информация о проекте" есть подробная инструкция по использованию. Также она описана ниже.
Используйте ссылку: http://127.0.0.1:8000/info/ для перехода к инструкции, когда развернете проект.

Логин и пароль от панели администратора: 

Логин: root | Пароль: 1234

## Тестирование библиотеки в демо-режиме без роботов.

Для проверки работоспособности библиотеки, необходимо помимо запуска самого модуля NeuralInterface также запустить файл requests.exe в папке C:\Projects\NeuralInterface\NeuralInterface\testing. Эта программа иммитирует API робота и добавляет данные в базу данных модуля NeuralInterface. 

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/e1026e9a-83a3-46a4-8bd3-642ff749dc6d)

После запуска программы происходит иммитация записи данных обучения агента в базу данных модуля NeuralInterface. Дождитесь окончания процесса записи данных. 

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/325de00b-761b-42b0-9628-dc651e21af77)

После этого, можно проверить работоспособность страницы "Мониторинг". После каждого нажатия на кнопку в правой части страницы, будет отправляться запрос на агента. Информацию об этом можно увидеть в консоли.

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/17d5d939-c464-4f51-8621-1e01875254e5

# Описание каждой страницы
## Панель управления
Позволяет работать с данными из базы данных. Полностью управлять данными можно только для таблиц с агентами и группами агентов. Возможно создавать, изменять и удалять записи из соответствующих таблиц. При попытке удалить запись, которая связана с другой записью в другой таблицы посредством внешнего ключа, система выдаст предупреждение о том, что сделать это нельзя и необходимо сначала удалить все данные таким образом, чтобы у БД сохранялась структура третьей нормальной формы. Осуществляется всё посредством кнопок. При создании и изменении открывается модальное окно для заполнения или изменения данных соответственно. Таблица типов агентов статичная и содержит значения по умолчанию. Остальные таблицы, если есть необходимость, нужно заполнять через административную панель сайта, которая позволяет полностью изменять данные.

Работа с агентами:

[Работа с агентами.webm](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/bca3f481-fb6f-4aa0-bc3c-6b7be5d203b1)

Важно! Для корректной работы веб-приложения, необходимо, чтобы MAC адреса и IP адреса у агентов были уникальные. Данные в таблицах связаны внешними ключами. Вы не сможете удалить связанные данные. Например, Вы не сможете удалить агента, если есть данные в таблице с файлами для этого агента или в какой-нибудь другой таблице.

Работа с группами:

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/18a031e6-caa7-4e54-8fae-f901c9257e4e

Важно! На группы агентов действуют схожие ограничения, что и на самих агентов. Например, Вы не сможете удалить группу агентов, если к ней принадлежит хотя бы один агент.

## Мониторинг
Выводит информацию об обучении агентов, а также позволяет управлять данными агентов. По умолчанию, всегда выбирается первая запись из таблицы ошибок агентов. График отображает данные обучения агентов. При выборе необходимого агента в таблице, график перерисовывается, исходя из значений ошибок для определенного агента. Панель в правой нижней части экрана позволяет отправлять необходимые команды агентам.

Работа с графиком:

https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/fb44d64e-dca6-4530-a515-6f2d56efe3ae

Кнопки в правой нижней части страницы отвечают за прямое управление и взаимодействие с агентами. При нажатии на кнопку отправляется запрос, который в зависимости от состояния агента отправляет определенный ответ. Как показано на видео, сервер не может найти агента в локальной сети с таким адресом и присылает ошибку, которая в полном виде отображается в нижней части страницы.

Важно! График не обновляется автоматически. Для обновления данных нажмите на кнопку обновления графика в верхней части экрана или на строчку с агентом в таблице

## Панель администратора
Логин: root | Пароль: 1234

Административная панель Django - это встроенный инструмент, предоставляемый Django для управления данными вашего веб-приложения. Она обеспечивает удобный и мощный интерфейс для работы с моделями и данными в вашей базе данных без необходимости создания собственного пользовательского интерфейса. 

Вид административной панели:

![image](https://github.com/Cognitive-systems-and-technologies/NeuralInterface/assets/47759876/f22aa1a9-888e-4f31-b673-afd2f28e046a)

Вход в административную панель

1. Зайдите на страницу административной панели
   Откройте веб-браузер и введите адрес административной панели (обычно это /admin) в адресной строке сайта или нажмите в левом меню "Панель администратора"
2. Авторизуйтесь
   Вам будет предложено ввести учетные данные. Введите логин и пароль, указанные выше

Важно! С осторожностью удаляйте, изменяйте или добавляйте данные! Нарушение целостности структуры базы данных может повлечь за собой нестабильную работу всего приложения. Если же Вам всё же нужно ка-то изменить структуру базы данных, добавить новые таблицы, или изменить внешние ключи, то рекомендуем пользоваться бесплатной программой Dbeaver.

# Лицензия

Этот проект находится под лицензией [MIT License](LICENSE).
