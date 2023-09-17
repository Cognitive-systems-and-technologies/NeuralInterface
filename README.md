# Интерфейс для обучения агентов

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

Для получения подобного результата, как на видео, необходимо установить оба модуля библиотеки: NeuralInterface на ПК, RoboAICore на отладочную плату STM32F4 или Raspberry pi 3 (model B). Модуль NeuralInterface необходимо настроить таким образом, чтобы запросы из веб-приложения отправлялись на агентов, принимали и отсылали ответ. Также необходимо иметь в наличии робота (указать какого) с установленными на нем ультразвуковыми датчиками определения расстояний до объектов типа HC-SR04 в количестве трех, отладочную плату STM32F4 или Raspberry pi 3 (model B) с установленной библиотекой RoboAICore на данную отладочную плату. 
В противном случае, модуль NeuralInerface будет работать в демо режиме, без связи с агентами, и при попытке отправить запрос будет выдавать ошибку, которая будет зависеть от устройств, расположенных в локальной сети и их состояний.

Характеристики агентов.

Для иллюстрации примера работы библиотеки были выбраны два робота (указать какие - их модель и характеристики, можно ссылку дать) на которые были установлены ультразвуковые датчики определения расстояний до объектов типа HC-SR04 в количестве трех, отладочные платы: одна для семейства процессоров STM32 серии STM32F4 на базе архитектуры ARM Cortex-M4 модель STM32F429ZI разрядностью 32bit, вторая - Raspberry pi 3 (model B). 
Частота работы процессора STM32F429ZI - 180MHz, размер программируемой памяти 2MB, объем оперативной памяти 256KB. 
Характеристики для raspberry pi: процессор: 64-битный четырёхъядерный ARM Cortex-A53 с тактовой частотой 1,2 ГГц на однокристальном чипе Broadcom BCM2837, оперативная память 1ГБ LPDDR2 SDRAM.

## Почему веб-приложение?
Использование веб-серверной версии модуля NeuralInterface вместо десктопного приложения позволяет развернуть данный проект не только на операционной 
системе Windows, но и на Linux, а также на любом сервере, позволяя объединять множество устройств даже вне локальной сети.

## Требования для запуска модуля NeuralInterface на ПК 
1. Операционная система на выбор:

   Windows 7/8/10 64-разрядная

   Linux (рекомендуется Ubuntu 18.04 LTS или более новая версия)

   macOS Big Sur (версия 11) или более новая
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

   Также необходимо проверить, была ли поставлена галочка в пункте "Add python.exe to path" при установке Python

## Использование

В модуле NeuralInterface на странице "Информация о проекте" есть подробная инструкция по использованию. Также она описана ниже.
Используйте ссылку: http://127.0.0.1:8000/info/ для перехода к инструкции, когда развернете проект.

Логин и пароль от панели администратора: 

Логин: root | Пароль: 1234

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
