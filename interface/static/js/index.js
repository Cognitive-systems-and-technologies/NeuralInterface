// Вызов функций для прослушивания событий
agentEditButtonListeners();
groupEditButtonListeners();
agentDeleteData();
groupDeleteData();

// Функция добавления агента
function agentAddData() {
    // Получение значения флажка agentStatusAdd
    const checkbox = document.getElementById('agentStatusAdd');
    const checkboxValue = checkbox.checked ? 1 : 0;

    // Получение значений полей ввода
    const agentData = {
        agent_name: document.getElementById('agentNameAdd').value, // Имя агента
        agent_mac_address: document.getElementById('AgentMacAddressAdd').value, // MAC-адрес агента
        agent_ip_address: document.getElementById('AgentIPAddressAdd').value, // IP-адрес агента
        agent_port: document.getElementById('AgentPortAdd').value, // Порт агента
        agent_description: document.getElementById('agentDescriptionAdd').value, // Описание агента
        datetime_create: new Date().toISOString(), // Дата и время создания агента
        agent_group_id: parseInt(document.getElementById('agentGroupAdd').value), // Идентификатор группы агента
        agent_type_id: parseInt(document.getElementById('agentTypeAdd').value), // Идентификатор типа агента
        agent_status: checkboxValue // Статус агента (включен или выключен)
    };

    // Функция для проверки значения на null, "None" или ""
    function isEmpty(value) {
        return value === null || value === "None" || (typeof value === "string" && value.trim() === "");
    }

    // Проверка наличия пустых значений в объекте agentData и вывод соответствующего сообщения.
    const fieldsToCheck = ['agent_mac_address', 'agent_ip_address', 'agent_group_id', 'agent_type_id', 'agent_status'];
    let isEmptyField = false; // Флаг для отслеживания, было ли обнаружено хотя бы одно пустое поле.

    // Проходимся по каждому ключу из списка fieldsToCheck.
    for (const key of fieldsToCheck) {
        const value = agentData[key];
        let fieldName = key; // По умолчанию используем ключ как название поля.


        // Изменяем название поля для вывода сообщения на русском языке.
        switch (key) {
            case 'agent_mac_address':
                fieldName = 'MAC адрес агента';
                break;
            case 'agent_ip_address':
                fieldName = 'IP-адрес агента';
                break;
            case 'agent_group_id':
                fieldName = 'группа агента';
                break;
            case 'agent_type_id':
                fieldName = 'тип агента';
                break;
            case 'agent_status':
                fieldName = 'статус агента';
                break;
        }

        // Проверяем, является ли текущее поле "agent_group_id" или "agent_type_id" и содержит ли пустое или NaN значение.
        if ((key === 'agent_group_id' || key === 'agent_type_id') && (value === null || isNaN(value))) {
            alert(`Поле ${fieldName} не заполнено!`);
            isEmptyField = true;
            break; // Останавливаем цикл, если обнаружено пустое или NaN значение для "agent_group_id" или "agent_type_id".
        } else if (isEmpty(value)) {
            alert(`Поле "${fieldName}" не заполнено!`);
            isEmptyField = true;
            break; // Останавливаем цикл, если обнаружено пустое значение для другого поля.
        }
    }

    // Если было обнаружено хотя бы одно пустое или NaN поле, прекращаем выполнение функции.
    if (isEmptyField) {
        return;
    }
    // Вывод данных агента в формате JSON в консоль для отладки
    console.log(JSON.stringify(agentData));

    // Получение CSRF-токена из cookie
    const csrftoken = getCookie('csrftoken');

    // Отправка POST-запроса на сервер для добавления данных агента
    fetch(`/api/addAgentData`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(agentData)
    }).then(response => {
        if (response.ok) {
            // Проверка статуса ответа (204 - No Content)
            if (response.status === 204) {
                console.log("Агент удален");
                // Выполнение необходимых обновлений пользовательского интерфейса или удаление элемента
            } else {
                // Обработка других успешных кодов состояния, если необходимо
                // Извлечение данных ответа, если они доступны
                return response.json();
            }
        } else {
            throw new Error(`Не удалось удалить объект с ID ${buttonId}.`);
        }
    }).then(data => {
        if (data !== undefined && data.error) {
            console.error(data.error);
            // Обработка сообщения об ошибке здесь (например, отображение на пользовательском интерфейсе)
        } else if (data !== undefined) {
            if (data == 'Агент успешно добавлен') {
                location.reload();
            } else if (data != 'Агент успешно добавлен') {
                alert(data);
            }
            // Обработка данных ответа, если они доступны
        }
    }).catch(error => {
        console.error('Произошла ошибка:', error);
    });
}

// Функция изменения агента
function agentEditData() {
    // Получение значения флажка agentStatusEdit
    const checkbox = document.getElementById('agentStatusEdit');
    const checkboxValue = checkbox.checked ? 1 : 0;

    // Получение значения ID агента для редактирования
    const agent_id = document.getElementById('agentIDEdit').value;

    // Получение значений полей ввода
    const agentData = {
        id: agent_id, // ID агента
        agent_name: document.getElementById('agentNameEdit').value, // Имя агента
        agent_mac_address: document.getElementById('AgentMacAddressEdit').value, // MAC-адрес агента
        agent_ip_address: document.getElementById('AgentIPAddressEdit').value, // IP-адрес агента
        agent_port: document.getElementById('AgentPortEdit').value, // Порт агента
        agent_description: document.getElementById('agentDescriptionEdit').value, // Описание агента
        datetime_change: new Date().toISOString(), // Дата и время изменения агента
        agent_group_id: parseInt(document.getElementById('agentGroupEdit').value), // Идентификатор группы агента
        agent_type_id: parseInt(document.getElementById('agentTypeEdit').value), // Идентификатор типа агента
        agent_status: checkboxValue // Статус агента (включен или выключен)
    };

    // Функция для проверки значения на null, "None" или ""
    function isEmpty(value) {
        return value === null || value === "None" || (typeof value === "string" && value.trim() === "");
    }

    // Проверка наличия пустых значений в объекте agentData и вывод соответствующего сообщения.
    const fieldsToCheck = ['agent_mac_address', 'agent_ip_address', 'agent_group_id', 'agent_type_id', 'agent_status'];
    let isEmptyField = false; // Флаг для отслеживания, было ли обнаружено хотя бы одно пустое поле.

    // Проходимся по каждому ключу из списка fieldsToCheck.
    for (const key of fieldsToCheck) {
        const value = agentData[key];
        let fieldName = key; // По умолчанию используем ключ как название поля.


        // Изменяем название поля для вывода сообщения на русском языке.
        switch (key) {
            case 'agent_mac_address':
                fieldName = 'MAC адрес агента';
                break;
            case 'agent_ip_address':
                fieldName = 'IP-адрес агента';
                break;
            case 'agent_group_id':
                fieldName = 'группа агента';
                break;
            case 'agent_type_id':
                fieldName = 'тип агента';
                break;
            case 'agent_status':
                fieldName = 'статус агента';
                break;
        }

        // Проверяем, является ли текущее поле "agent_group_id" или "agent_type_id" и содержит ли пустое или NaN значение.
        if ((key === 'agent_group_id' || key === 'agent_type_id') && (value === null || isNaN(value))) {
            alert(`Поле ${fieldName} не заполнено!`);
            isEmptyField = true;
            break; // Останавливаем цикл, если обнаружено пустое или NaN значение для "agent_group_id" или "agent_type_id".
        } else if (isEmpty(value)) {
            alert(`Поле "${fieldName}" не заполнено!`);
            isEmptyField = true;
            break; // Останавливаем цикл, если обнаружено пустое значение для другого поля.
        }
    }

    // Если было обнаружено хотя бы одно пустое или NaN поле, прекращаем выполнение функции.
    if (isEmptyField) {
        return;
    }

    // Вывод данных агента в формате JSON в консоль для отладки
    console.log(JSON.stringify(agentData));

    // Получение CSRF-токена из cookie
    const csrftoken = getCookie('csrftoken');

    // Отправка PUT-запроса на сервер для редактирования данных агента
    fetch(`/api/editAgentData/${agent_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(agentData)
    }).then(response => {
        if (response.ok) {
            // Проверка статуса ответа (204 - No Content)
            if (response.status === 204) {
                console.log("Агент удален");
                // Выполнение необходимых обновлений пользовательского интерфейса или удаление элемента
            } else {
                // Обработка других успешных кодов состояния, если необходимо
                // Извлечение данных ответа, если они доступны
                return response.json();
            }
        } else {
            throw new Error(`Не удалось удалить объект с ID ${buttonId}.`);
        }
    }).then(data => {
        if (data !== undefined && data.error) {
            console.error(data.error);
            // Обработка сообщения об ошибке здесь (например, отображение на пользовательском интерфейсе)
        } else if (data !== undefined) {
            if (data == 'Агент успешно изменен') {
                location.reload();
            } else if (data != 'Агент успешно изменен') {
                alert(data);
            }
            // Обработка данных ответа, если они доступны
        }
    }).catch(error => {
        console.error('Произошла ошибка:', error);
    });
}

// Функция удаления данных агента
function agentDeleteData() {
    // Получение всех кнопок с классом deleteAgent
    var buttons = document.querySelectorAll(".deleteAgent");

    // Добавление обработчиков событий для каждой кнопки
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", handleClick);
    }

    // Функция-обработчик события клика
    function handleClick(event) {
        // Получение значения ID из атрибута data-id кнопки
        const buttonId = event.currentTarget.getAttribute("data-id");

        // Отправка DELETE-запроса на конечную точку Django REST API
        const tokenizers = getCookie('csrftoken');
        fetch(`/api/deleteAgentData/${buttonId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': tokenizers,
            },
            // Можно включить учетные данные, если требуется (например, для аутентификации)
            // credentials: 'include',
        }).then(response => {
            if (response.ok) {
                // Проверка статуса ответа (204 - No Content)
                if (response.status === 204) {
                    console.log("Агент удален");
                    // Выполнение необходимых обновлений пользовательского интерфейса или удаление элемента
                } else {
                    // Обработка других успешных кодов состояния, если необходимо
                    // Извлечение данных ответа, если они доступны
                    return response.json();
                }
            } else {
                throw new Error(`Не удалось удалить объект с ID ${buttonId}.`);
            }
        }).then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Обработка сообщения об ошибке здесь (например, отображение на пользовательском интерфейсе)
            } else if (data !== undefined) {
                if (data == 'Агент успешно удален') {
                    alert(data);
                    location.reload();
                } else if (data != 'Агент успешно удален') {
                    alert(data);
                }
                // Обработка данных ответа, если они доступны
            }
        }).catch(error => {
            console.error('Произошла ошибка:', error);
        });
    }
}

// Добавление новой группы агента
function groupAddData() {
    // Получение значений полей ввода
    const groupData = {
        agent_group_name: document.getElementById('groupNameAdd').value, // Название группы
        agent_group_priority: document.getElementById('groupPriorityAdd').value, // Приоритет группы
        agent_group_description: document.getElementById('groupDescriptionAdd').value, // Описание группы
        datetime_create: new Date().toISOString() // Дата и время создания группы
    };

    // Вывод данных группы в формате JSON в консоль для отладки
    console.log(JSON.stringify(groupData));

    // Получение CSRF-токена из cookie
    const csrftoken = getCookie('csrftoken');

    // Отправка POST-запроса на сервер для добавления данных группы
    fetch(`/api/addGroupData`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(groupData)
    }).then(function (response) {
        // Проверка успешности ответа (статус 200)
        if (response.ok) {
            // Перезагрузка страницы
            location.reload();
        } else {
            // Обработка ошибки
            console.log('Ошибка: ' + response.status);
        }
    }).catch(function (error) {
        console.log('Ошибка: ' + error);
    });
}

// Функция изменения данных группы
function groupEditData() {
    // Получение значения ID группы для редактирования
    const group_id = document.getElementById('groupIDEdit').value;

    // Получение значений полей ввода
    const groupData = {
        id: group_id, // ID группы
        agent_group_name: document.getElementById('groupNameEdit').value, // Название группы
        agent_group_priority: document.getElementById('groupPriorityEdit').value, // Приоритет группы
        agent_group_description: document.getElementById('groupDescriptionEdit').value, // Описание группы
        datetime_change: new Date().toISOString() // Дата и время изменения группы
    };

    // Вывод данных группы в формате JSON в консоль для отладки
    console.log(JSON.stringify(groupData));

    // Получение CSRF-токена из cookie
    const tokenizers = getCookie('csrftoken');

    // Отправка PUT-запроса на сервер для редактирования данных группы
    fetch(`/api/editGroupData/${group_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokenizers,
        },
        body: JSON.stringify(groupData)
    }).then(function (response) {
        // Проверка успешности ответа (статус 200)
        if (response.ok) {
            // Перезагрузка страницы
            location.reload();
        } else {
            // Обработка ошибки
            console.log('Ошибка: ' + response.status);
        }
    }).catch(function (error) {
        console.log('Ошибка: ' + error);
    });
}

// Удаление группы агентов
function groupDeleteData() {
    // Получение всех кнопок с классом deleteGroup
    var buttons = document.querySelectorAll(".deleteGroup");

    // Добавление обработчиков событий для каждой кнопки
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", handleClick);
    }

    // Функция-обработчик события клика
    function handleClick(event) {
        // Получение значения ID из атрибута data-id кнопки
        const buttonId = event.currentTarget.getAttribute("data-id");

        // Отправка DELETE-запроса на конечную точку Django REST API
        const tokenizers = getCookie('csrftoken');
        fetch(`/api/deleteGroupData/${buttonId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': tokenizers,
            },
            // Можно включить учетные данные, если требуется (например, для аутентификации)
            // credentials: 'include',
        }).then(response => {
            if (response.ok) {
                // Проверка статуса ответа (204 - No Content)
                if (response.status === 204) {
                    console.log("Группа удалена");
                    // Выполнение необходимых обновлений пользовательского интерфейса или удаление элемента
                } else {
                    // Обработка других успешных кодов состояния, если необходимо
                    // Извлечение данных ответа, если они доступны
                    return response.json();
                }
            } else {
                throw new Error(`Не удалось удалить объект с ID ${buttonId}.`);
            }
        }).then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Обработка сообщения об ошибке здесь (например, отображение на пользовательском интерфейсе)
            } else if (data !== undefined) {
                if (data == 'Группа успешно удалена') {
                    alert(data);
                    location.reload();
                } else if (data != 'Группа успешно удалена') {
                    alert(data);
                }
                // Обработка данных ответа, если они доступны
            }
        }).catch(error => {
            console.error('Произошла ошибка:', error);
        });
    }
}

// Прослушивание событий кнопки изменения агента
function agentEditButtonListeners() {
    // Получение ссылок на все кнопки "Редактировать"
    var editButtons = document.getElementsByClassName("editAgent btn btn-outline-primary btn-sm");

    // Добавление обработчиков событий для каждой кнопки "Редактировать"
    for (var i = 0; i < editButtons.length; i++) {
        editButtons[i].addEventListener("click", handleEdit);
    }

    // Функция-обработчик события клика по кнопке "Редактировать"
    function handleEdit(event) {
        // Получение родительской строки таблицы (tr)
        const row = event.target.closest("tr");
        console.log(row)
        // Заполнение полей ввода
        document.getElementById('agentIDEdit').value = row.cells[0].innerText; // Значение ID агента
        document.getElementById('agentNameEdit').value = row.cells[2].innerText; // Значение имени агента
        document.getElementById('AgentMacAddressEdit').value = row.cells[5].innerText; // Значение MAC-адреса агента
        document.getElementById('agentDescriptionEdit').value = row.cells[9].innerText; // Значение описания агента
        document.getElementById('AgentIPAddressEdit').value = row.cells[10].innerText; // Значение IP-адреса агента
        document.getElementById('AgentPortEdit').value = row.cells[11].innerText; // Значение порта агента
        document.getElementById('agentGroupEdit').value = row.cells[12].innerText; // Значение ID группы агента
        document.getElementById('agentTypeEdit').value = row.cells[13].innerText; // Значение ID типа агента
        document.getElementById('agentStatusEdit').checked = parseInt(row.cells[14].innerText); // Значение статуса агента
    }
}

// Прослушивание событий кнопки изменения группы агента
function groupEditButtonListeners() {
    // Получение ссылок на все кнопки "Редактировать"
    var editGroupButtons = document.getElementsByClassName("editGroup btn btn-outline-primary btn-sm");

    // Добавление обработчиков событий для каждой кнопки "Редактировать"
    for (var i = 0; i < editGroupButtons.length; i++) {
        editGroupButtons[i].addEventListener("click", handleEdit);
    }

    // Функция-обработчик события клика по кнопке "Редактировать"
    function handleEdit(event) {
        // Получение родительской строки таблицы (tr)
        const row = event.target.closest("tr");
        console.log(row)
        // Заполнение полей ввода
        document.getElementById('groupIDEdit').value = row.cells[0].innerText; // Значение ID группы
        document.getElementById('groupNameEdit').value = row.cells[1].innerText; // Значение названия группы
        document.getElementById('groupPriorityEdit').value = row.cells[2].innerText; // Значение приоритета группы
        document.getElementById('groupDescriptionEdit').value = row.cells[3].innerText; // Значение описания группы
    }
}

function getCookie(name) {
    // Ищем значение cookie по имени с помощью регулярного выражения
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    // Если найдено значение cookie, возвращаем его
    // Используем метод pop(), чтобы получить последний элемент массива с найденным значением cookie
    return cookieValue ? cookieValue.pop() : '';
}

