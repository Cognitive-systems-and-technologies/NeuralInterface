/* Основная страница */
function agentAddData() {
    const checkbox = document.getElementById('agentStatus');
    const checkboxValue = checkbox.checked ? 1 : 0;
    const selectGroup = document.getElementById('agentGroup');
    const agentData = {
        agent_name: document.getElementById('agentName').value,
        agent_mac_address: document.getElementById('AgentMacAddress').value,
        agent_description: document.getElementById('agentDescription').value,
        datetime_create: new Date().toISOString(), /*toLocaleString().replace(/[\s,]/g, ' '),*/
        agent_group_id: parseInt(document.getElementById('agentGroup').value),
        agent_type_id: parseInt(document.getElementById('agentType').value),
        agent_status: checkboxValue
    };
    console.log(JSON.stringify(agentData))
    const csrftoken = getCookie('csrftoken');
    fetch('http://127.0.0.1:8000/api/addAgentData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(agentData)
    })
        .then(function (response) {
            // Check if the response was successful (status 200)
            if (response.ok) {
                // Reload the page
                location.reload();
            } else {
                // Handle the error
                console.log('Error: ' + response.status);
            }
        })
        .catch(function (error) {
            console.log('Error: ' + error);
        });
}

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

/*
function selectGroupAgent() {
    var items = document.querySelectorAll("#modalChangeGroupAgentList li");

            for(var i = 0; i < items.length; i++)
            {
                items[i].onclick = function(){

                    document.getElementById("modalGroupAgent").innerHTML = this.innerHTML;
                    document.getElementById("modalGroupAgent").value = this.value;
                    console.log(this.innerHTML, this.value);
                };
            }
}
*/


/* global bootstrap: false */
/*
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()
*/