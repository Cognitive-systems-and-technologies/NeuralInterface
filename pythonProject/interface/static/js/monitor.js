window.onload = function(e){
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

var options = {
  chart: {
    type: 'line'
  },
  series: [{
    name: 'Координата X',
    data: coordinate_x_values
  },
  {
      name: "Координата Y",
      data: coordinate_y_values
  }],
  xaxis: {
    categories: datetime_create_values
  }
}

var chart = new ApexCharts(document.querySelector("#chart"), options);

chart.render();
}


