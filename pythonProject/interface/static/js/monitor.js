// Инициализируем график
var chart = echarts.init(document.getElementById('chart'));

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
            myDarkModeSwitch: {
                show: true,
                title: 'Сменить тему',
                icon: 'img/darkmode.png',
                onclick: function (params) {
                    if (chart.getOption().darkMode) {
                        chart.setOption({ darkMode: false });
                    } else {
                        chart.setOption({ darkMode: true });
                    }
                }
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
window.onload = graphDraw

function graphDraw() {
    fetch('http://127.0.0.1:8000/api/graphData')
        .then(response => response.json())
        .then(data => {
            agentStep = Object.values(data).map(item => parseInt(item['agent_step']));
            agentError = Object.values(data).map(item => parseInt(item['agent_error_value']));
            // Устанавливаем опции графика и загружаем данные
            chart.setOption({
                xAxis: {
                    data: agentStep
                },
                series: [{
                    data: agentError
                }]
            });
        })
        .catch(error => console.error(error));
}
// Задаем функцию для кнопки после вызова graphDraw()
chart.on('restore', function(params) {
    graphDraw();
});


/*
// Загружаем данные графика при загрузке страницы
fetch('http://127.0.0.1:8000/api/graphData')
  .then(response => response.json())
  .then(data => {
    // Устанавливаем опции графика и загружаем данные
    chart.setOption({
      xAxis: {
        type: 'category',
        data: data.agent_step
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        type: 'line',
        data: data.agent_error_value
      }]
    });
  })
  .catch(error => console.error(error));
*/
/*
// Обновляем данные графика при клике на кнопку
document.getElementById('buttonUpdate').addEventListener('click', function() {
  fetch('http://example.com/data.json')
    .then(response => response.json())
    .then(data => {
      // Обновляем данные графика
      chart.setOption({
        series: [{
          data: data.yData
        }]
      });
    })
    .catch(error => console.error(error));
});
*/

/*
var url = 'http://127.0.0.1:8000/api/graphData';

axios({
  method: 'GET',
  url: url,
}).then(function(response) {
  chart.updateSeries([{
    name: 'agent_step',
    data: response.data
  }])
})
*/


/*
   const agent_port = document.querySelectorAll('td:nth-child(1)');
   const coordinate_x = document.querySelectorAll('td:nth-child(2)');
   const coordinate_y = document.querySelectorAll('td:nth-child(3)');
   const datetime_create = document.querySelectorAll('td:nth-child(4)');

   const agent_port_values = []
   agent_port.forEach(function(singleCell) {
   agent_port_values.push(singleCell.innerText);
   });
   const coordinate_x_values = []
   coordinate_x.forEach(function(singleCell) {
   coordinate_x_values.push(singleCell.innerText);
   });
   const coordinate_y_values = []
   coordinate_y.forEach(function(singleCell) {
   coordinate_y_values.push(singleCell.innerText);
   });
   const datetime_create_values = []
   datetime_create.forEach(function(singleCell) {
   datetime_create_values.push(singleCell.innerText);
   });
console.log(agent_port_values);
console.log(coordinate_x_values);
console.log(coordinate_y_values);
console.log(datetime_create_values);
*/

/*
const url = 'http://127.0.0.1:8000/api/graphData';


function renameKey ( obj, oldKey, newKey ) {
  obj[newKey] = obj[oldKey];
  delete obj[oldKey];
}

let updatedJson;

const getData = async () => {
  const response = await fetch(url);
  const data = await response.json();
  console.log(typeof data)

  data.forEach( obj => renameKey( obj, 'id', 'x' ));
  data.forEach( obj => renameKey( obj, 'agent_error_value', 'y' ));
  updatedJson = data;

  return data;
};

(async () => {
  await getData();
  console.log(updatedJson);

var options = {
  chart: {
    type: 'line'
  },
    series: [{
          name: 'Агент 1',
          data: updatedJson
        }, {
          name: 'Агент 2',
          data: updatedJson
         }],
    xaxis: {
      type: 'number'
    }
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
})();
*/
