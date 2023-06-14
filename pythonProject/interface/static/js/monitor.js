graphTableClickListeners()
var agentIDGraph = parseInt(document.querySelector('.clickable-row td:first-child').textContent)
// Инициализируем график
var chartContainer = document.getElementById('chart');
var chart = echarts.init(chartContainer);


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
window.onload = graphDraw(agentIDGraph)

function graphDraw(agentIDGraph) {
    console.log(agentIDGraph)
    fetch(`http://127.0.0.1:8000/api/graphData/?agent_id=${agentIDGraph}`)
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
                });
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
        var row = event.currentTarget;
        // Toggle the "active" class on the row
        row.classList.toggle('active');
        // Get the data from each cell in the row
        var rowData = Array.from(row.cells).map(cell => cell.textContent.trim());
        // Print the captured data to the console (you can modify this part as needed)
        agentIDGraph = rowData[0]
        console.log(agentIDGraph);
        graphDraw(agentIDGraph)
    }
}




