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


// Устанавливаем опции графика
var options = {
    title: {
        text: 'График ошибок'
    },
    legend: {
        data: ['Ошибки']
    },
    xAxis: {
        data: []
    },
    yAxis: {},
    series: [{
        name: 'Агент 1',
        type: 'line',
        data: []
    }],
    darkMode: true,
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                show: true,
                yAxisIndex: 'none'
            },
            restore: {
                show: true,
                title: 'Перезагрузить данные'
            }
        }
    },
};

// Устанавливаем опции графика
chart.setOption(options);

function graphDraw(agentIDGraph) {
    console.log(agentIDGraph)
    fetch(`/api/graphData/?agent_id=${agentIDGraph}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                agentStep = Object.values(data).map(item => parseInt(item['agent_step']));
                agentError = Object.values(data).map(item => parseInt(item['agent_error_value']));
                agentName = data[0].agent_name
                // Устанавливаем опции графика и загружаем данные
                chart.setOption({
                    xAxis: {
                        data: agentStep
                    },
                    series: [{
                        name: agentName,
                        data: agentError
                    }],
                    tooltip: {
                        trigger: 'axis', // Set the trigger type to show tooltips on data points
                        formatter: function (params) {
                            // Customize the content of the tooltip
                            let agentStep = params[0].axisValue; // Get the agent step value
                            let agentError = params[0].data; // Get the agent error value
                            let agentName = params[0].seriesName; // Get the agent name

                            // Construct the tooltip content
                            let tooltipContent = 'Шаг Агента: ' + agentStep + '<br />' +
                                'Ошибка агента: ' + agentError + '<br />' +
                                'Название агента: ' + agentName;

                            return tooltipContent;
                        }
                    },
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
                })
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
                    xAxis: {
                        data: 0
                    },
                    series: [{
                        name: '',
                        data: 0
                    }],
                });
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
            headerStatus.textContent = 'Выбрано: ' + agentName;
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
        agent_command: agentCommand
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



