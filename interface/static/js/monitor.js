graphTableClickListeners()
agentCommandClickListeners()
var agentIDGraph = parseInt(document.querySelector('.clickable-row td:first-child').textContent)
// Получаем ID агента для отображения графика.
// Находим элемент таблицы с классом "clickable-row" и первым дочерним элементом ячейку td.
// Извлекаем текстовое содержимое ячейки и преобразуем его в целое число с помощью parseInt().

// Инициализируем контейнер для графика
var chartContainer = document.getElementById('chart');
var chart = echarts.init(chartContainer);

window.addEventListener('DOMContentLoaded', (event) => {
    // Находим первую строку в таблице
    const firstRow = document.querySelector('table tbody tr');

    // Симулируем событие клика на первой строке
    if (firstRow) {
        firstRow.click();
    }
});
// При загрузке страницы добавляем обработчик события для выполнения кода после полной загрузки контента (DOMContentLoaded).
// Находим первую строку в таблице с помощью селектора 'table tbody tr'.
// Если первая строка найдена, симулируем событие клика на этой строке.


function graphDraw(agentIDGraph) {
    // Запрос к API для получения данных графика
    fetch(`/api/graphData/?agent_id=${agentIDGraph}`)
        .then(response => response.json())
        .then(data => {
            // Проверка наличия данных
            if (data.length > 0) {
                console.log(data);

                /* Формирование данных для оси X */
                const agentStepValues = data.map(obj => obj.agent_step);
                const uniqueAgentStepValues = [...new Set(agentStepValues)];
                const xAxisData = uniqueAgentStepValues.sort((a, b) => a - b);
                console.log(xAxisData);

                /* Формирование данных для графика */
                const errorValuesByAlgorithm = {};
                data.forEach(obj => {
                    const algorithmCodeName = obj.algorithm_code_name;
                    const errorValue = obj.agent_error_value;

                    // Группировка значений ошибки по алгоритму
                    if (!errorValuesByAlgorithm.hasOwnProperty(algorithmCodeName)) {
                        errorValuesByAlgorithm[algorithmCodeName] = [];
                    }
                    errorValuesByAlgorithm[algorithmCodeName].push(errorValue);
                });

                const seriesData = [];

                // Формирование данных серий для графика
                for (const algorithmCodeName in errorValuesByAlgorithm) {
                    const errorValues = errorValuesByAlgorithm[algorithmCodeName];

                    seriesData.push({
                        name: algorithmCodeName,
                        data: errorValues,
                        type: 'line'
                    });
                }

                console.log(seriesData);

                // Установка опций графика и загрузка данных
                chart.setOption({
                    xAxis: [
                        {
                            type: 'category',
                            name: 'Шаг',
                            axisTick: {
                                alignWithLabel: true
                            },
                            data: xAxisData
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            name: 'Значение ошибки',
                            position: 'left',
                        }
                    ],
                    series: seriesData,
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: { type: 'cross' }
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataZoom: {
                                show: true,
                                yAxisIndex: 'none'
                            },
                            restore: {
                                show: true,
                                title: 'Перезагрузить график',
                                onclick: chart.on('restore', function (params) {
                                    graphDraw(agentIDGraph);
                                })
                            }
                        }
                    },
                    legend: {},
                    graphic: [{
                        type: 'text',
                        left: 'center',
                        top: 'middle',
                        style: {
                            text: '',
                            textAlign: 'center',
                            fontSize: 28
                        }
                    }]
                }, true);

                // Обновление статуса в футере
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = 'Данные успешно загружены';
                    footerStatus.classList.remove('text-success');
                    footerStatus.classList.remove('text-danger');
                    footerStatus.classList.add('text-success');
                }
            } else {
                // Отображение сообщения "Нет данных" вместо графика
                chart.setOption({
                    graphic: [{
                        type: 'text',
                        left: 'center',
                        top: 'middle',
                        style: {
                            text: 'Нет данных для данного агента',
                            textAlign: 'center',
                            fontSize: 28
                        }
                    }],
                }, true);

                // Обновление статуса в футере
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = 'Нет данных в базе данных';
                    footerStatus.classList.remove('text-success');
                    footerStatus.classList.remove('text-danger');
                    footerStatus.classList.add('text-danger');
                }
            }
        })
        .catch(error => console.error(error));
}


// Задаем функцию для кнопки после вызова graphDraw()
chart.on('restore', function (params) {
    graphDraw(agentIDGraph);
});

// Функция обработки событий нажатия на строку таблицы
function graphTableClickListeners() {
    // Добавление обработчиков событий клика к каждой кликабельной строке
    var rows = document.getElementsByClassName('clickable-row');
    for (var i = 0; i < rows.length; i++) {
        rows[i].addEventListener('click', handleRowClick);
    }

    // Функция для обработки клика по строке
    function handleRowClick(event) {
        // Получение выбранной строки
        const row = event.currentTarget;

        // Удаление класса "table-active" у всех строк
        const table = row.closest('table');
        let rows = table.getElementsByClassName('clickable-row');
        for (let i = 0; i < rows.length; i++) {
            rows[i].classList.remove('table-active');
        }

        // Переключение класса "table-active" для кликнутой строки
        row.classList.toggle('table-active');

        // Получение данных из каждой ячейки строки
        const rowData = Array.from(row.cells).map(cell => cell.textContent.trim());

        // Вывод собранных данных в консоль (эту часть можно изменить по необходимости)
        const agentIDGraph = rowData[0];

        const agentName = rowData[2];
        console.log(agentName);

        const headerStatus = document.getElementById('headerStatus');
        if (headerStatus) {
            headerStatus.value = agentIDGraph;
        }

        // Вызов функции graphDraw с использованием идентификатора агента
        graphDraw(agentIDGraph);
    }
}

// Функция обработки событий нажатия кнопок управления агентом
function agentCommandClickListeners() {
    // Добавление обработчиков событий клика к каждой кнопке
    const agentCommandButtons = document.querySelectorAll('.agentCommand');
    agentCommandButtons.forEach((button) => {
        button.addEventListener('click', () => {
            // Получение команды агента из значения кнопки
            const agentCommand = button.value;
            console.log(agentCommand); // Вывод значения кликнутой кнопки в консоль
            SendRequestToAgent(agentCommand);
        });
    });
}

// Функция отправки запроса агенту
function SendRequestToAgent(agentCommand) {
    // Получение идентификатора агента из элемента с id "headerStatus"
    const agentId = document.getElementById('headerStatus').value;

    // Формирование данных запроса
    const requestData = {
        agent_id: agentId,
        agent_command: agentCommand,
        t: 'command'
    };

    console.log(JSON.stringify(requestData));

    // Получение CSRF-токена
    const csrftoken = getCookie('csrftoken');

    // Отправка POST-запроса на сервер
    fetch(`/api/SendRequestToAgent`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(requestData)
    }).then(function (response) {
        // Проверка успешности ответа (статус 200)
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not OK.');
        }
    }).then(data => {
        console.log(data);
        if (data !== undefined && data.error) {
            console.error(data.error);
            // Обработка сообщения об ошибке (например, отображение на пользовательском интерфейсе)
        } else if (data !== undefined) {
            // Проверка наличия сообщения об ошибке
            const errorMessageCheck = data.substring(0, 6);
            if (errorMessageCheck === 'Ошибка') {
                // Обновление статуса внизу страницы при ошибке
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    /* footerStatus.textContent = data; */
                    footerStatus.textContent = 'Запрос успешно отправлен'
                    footerStatus.classList.remove('text-success');
                    footerStatus.classList.remove('text-danger');
                    footerStatus.classList.add('text-success');
                }
            } else if (errorMessageCheck !== 'Ошибка') {
                // Обновление статуса внизу страницы при успешном выполнении
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    /* footerStatus.textContent = data; */
                    footerStatus.textContent = 'Запрос успешно отправлен'
                    footerStatus.classList.remove('text-success');
                    footerStatus.classList.remove('text-danger');
                    footerStatus.classList.add('text-success');
                }
            }
        }
    }).catch(function (error) {
        console.log('Error: ' + error);
    });
}

// Функция удаления данных графика для определенного агента
function deleteAgentErrors() {
    // Получение CSRF-токена
    const tokenizers = getCookie('csrftoken');

    // Получение идентификатора агента из элемента с id "headerStatus"
    const agentIDGraph = document.getElementById('headerStatus').value;

    // Отправка DELETE-запроса на сервер для удаления данных об ошибках агента
    fetch(`api/deleteAgentErrorsData/${agentIDGraph}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokenizers
        }
    }).then(response => {
        if (response.ok) {
            // Проверка статуса ответа (204 - No Content)
            if (response.status === 204) {
                console.log("Agent deleted");
                // Выполнение необходимых обновлений пользовательского интерфейса или удаление элементов
            } else {
                // Обработка других успешных статусов кодов, если необходимо
                // Извлечение данных ответа, если доступно
                return response.json();
            }
        } else {
            throw new Error(`Failed to delete object with ID ${agentIDGraph}.`);
        }
    })
        .then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Обработка сообщения об ошибке (например, отображение на пользовательском интерфейсе)
            } else if (data !== undefined) {
                // Проверка сообщения об успешном удалении данных
                if (data == 'Данные успешно удалены') {
                    // Перерисовка графика после удаления данных об ошибках агента
                    graphDraw(agentIDGraph);
                } else if (data != 'Группа успешно удалена') {
                    // Обновление статуса внизу страницы при ошибке
                    const footerStatus = document.getElementById('footerStatus');
                    if (footerStatus) {
                        footerStatus.textContent = data;
                        footerStatus.classList.remove('text-success');
                        footerStatus.classList.remove('text-danger');
                        footerStatus.classList.add('text-danger');
                    }
                }
                // Обработка данных ответа, если доступны
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
}


function getCookie(name) {
    // Ищем значение cookie по имени с помощью регулярного выражения
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    // Если найдено значение cookie, возвращаем его
    // Используем метод pop(), чтобы получить последний элемент массива с найденным значением cookie
    return cookieValue ? cookieValue.pop() : '';
}