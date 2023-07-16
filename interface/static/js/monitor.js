graphTableClickListeners()
agentCommandClickListeners()
var agentIDGraph = parseInt(document.querySelector('.clickable-row td:first-child').textContent)
// Инициализируем график
var chartContainer = document.getElementById('chart');
var chart = echarts.init(chartContainer);

window.addEventListener('DOMContentLoaded', (event) => {
    // Find the first row in the table
    const firstRow = document.querySelector('table tbody tr');

    // Simulate a click event on the first row
    if (firstRow) {
        firstRow.click();
    }
});

function graphDraw(agentIDGraph) {
    fetch(`/api/graphData/?agent_id=${agentIDGraph}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                console.log(data)
                /* Формируем данные для оси X */
                const agentStepValues = data.map(obj => obj.agent_step);
                const uniqueAgentStepValues = [...new Set(agentStepValues)];
                const xAxisData = uniqueAgentStepValues.sort((a, b) => a - b);
                console.log(xAxisData)
                /* Формируем данные для графика */
                const errorValuesByAlgorithm = {};
                data.forEach(obj => {
                    const algorithmCodeName = obj.algorithm_code_name;
                    const errorValue = obj.agent_error_value;

                    if (!errorValuesByAlgorithm.hasOwnProperty(algorithmCodeName)) {
                        errorValuesByAlgorithm[algorithmCodeName] = [];
                    }

                    errorValuesByAlgorithm[algorithmCodeName].push(errorValue);
                });
                const seriesData = [];

                for (const algorithmCodeName in errorValuesByAlgorithm) {
                    const errorValues = errorValuesByAlgorithm[algorithmCodeName];

                    seriesData.push({
                        name: algorithmCodeName,
                        data: errorValues,
                        type: 'line'
                    });
                }
                console.log(seriesData);
                // Устанавливаем опции графика и загружаем данные
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
                        axisPointer: {type: 'cross'}
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
                }, true)
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = 'Данные успешно загружены';
                    footerStatus.classList.remove('text-success')
                    footerStatus.classList.remove('text-danger')
                    footerStatus.classList.add('text-success')
                }
            } else {
                // Show "No Data" text instead of the graph
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
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = 'Нет данных в базе данных';
                    footerStatus.classList.remove('text-success')
                    footerStatus.classList.remove('text-danger')
                    footerStatus.classList.add('text-danger')
                }
            }
        })
        .catch(error => console.error(error));
}


// Задаем функцию для кнопки после вызова graphDraw()
chart.on('restore', function (params) {
    graphDraw(agentIDGraph);
});

function graphTableClickListeners() {
    // Add click event listeners to each clickable row
    var rows = document.getElementsByClassName('clickable-row');
    for (var i = 0; i < rows.length; i++) {
        rows[i].addEventListener('click', handleRowClick);
    }

    // Function to handle click on a row
    function handleRowClick(event) {
        // Get the selected row
        const row = event.currentTarget;

        // Remove table-active class from all rows
        const table = row.closest('table');
        let rows = table.getElementsByClassName('clickable-row');
        for (let i = 0; i < rows.length; i++) {
            rows[i].classList.remove('table-active');
        }

        // Toggle the "table-active" class on the clicked row
        row.classList.toggle('table-active');

        // Get the data from each cell in the row
        const rowData = Array.from(row.cells).map(cell => cell.textContent.trim());

        // Print the captured data to the console (you can modify this part as needed)
        const agentIDGraph = rowData[0];

        const agentName = rowData[2];
        console.log()
        const headerStatus = document.getElementById('headerStatus');
        if (headerStatus) {
            headerStatus.value = agentIDGraph;
        }
        // Call your graphDraw function with the agent ID
        graphDraw(agentIDGraph);
    }
}


function agentCommandClickListeners() {
    // Add click event listeners to each clickable row
    const agentCommandButtons = document.querySelectorAll('.agentCommand');
    agentCommandButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const agentCommand = button.value;
            console.log(agentCommand); // Output the value of the clicked button
            SendRequestToAgent(agentCommand)
        });
    });
}

function SendRequestToAgent(agentCommand) {
    const agentId = document.getElementById('headerStatus').value;
    const requestData = {
        agent_id: agentId,
        agent_command: agentCommand,
        t: 'command'
    };
    console.log(JSON.stringify(requestData))
    const csrftoken = getCookie('csrftoken');
    fetch(`/api/SendRequestToAgent`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(requestData)
    }).then(function (response) {
        // Check if the response was successful (status 200)
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not OK.');
        }
    }).then(data => {
        console.log(data)
        if (data !== undefined && data.error) {
            console.error(data.error);
            // Handle the error message here (e.g., display it on the UI)
        } else if (data !== undefined) {
            const errorMessageCheck = data.substring(0, 6)
            if (errorMessageCheck === 'Ошибка') {
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = data;
                    footerStatus.classList.remove('text-success')
                    footerStatus.classList.remove('text-danger')
                    footerStatus.classList.add('text-danger')
                }
            } else if (errorMessageCheck !== 'Ошибка') {
                const footerStatus = document.getElementById('footerStatus');
                if (footerStatus) {
                    footerStatus.textContent = data;
                    footerStatus.classList.remove('text-success')
                    footerStatus.classList.remove('text-danger')
                    footerStatus.classList.add('text-success')
                }
            }
        }
    }).catch(function (error) {
        console.log('Error: ' + error);
    });
}

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

function deleteAgentErrors() {
    const tokenizers = getCookie('csrftoken');
    const agentIDGraph = document.getElementById('headerStatus').value;
    fetch(`api/deleteAgentErrorsData/${agentIDGraph}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokenizers
        }
    }).then(response => {
        if (response.ok) {
            // Check if the status code is 204 (No Content)
            if (response.status === 204) {
                console.log("Agent deleted");
                // Do any necessary UI updates or item removal
            } else {
                // Handle other success status codes if needed
                // Extract response data if available
                return response.json();
            }
        } else {
            throw new Error(`Failed to delete object with ID ${agentIDGraph}.`);
        }
    })
        .then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Handle the error message here (e.g., display it on the UI)
            } else if (data !== undefined) {
                if (data == 'Данные успешно удалены') {
                    graphDraw(agentIDGraph);
                } else if (data != 'Группа успешно удалена') {
                    const footerStatus = document.getElementById('footerStatus');
                    if (footerStatus) {
                        footerStatus.textContent = data;
                        footerStatus.classList.remove('text-success')
                        footerStatus.classList.remove('text-danger')
                        footerStatus.classList.add('text-danger')
                    }
                }
                // Handle response data if available
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
}