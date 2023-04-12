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
