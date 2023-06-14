agentEditButtonListeners();
groupEditButtonListeners();
agentDeleteData();
groupDeleteData();

function agentAddData() {
    const checkbox = document.getElementById('agentStatusAdd');
    const checkboxValue = checkbox.checked ? 1 : 0;
    const agentData = {
        agent_name: document.getElementById('agentNameAdd').value,
        agent_mac_address: document.getElementById('AgentMacAddressAdd').value,
        agent_ip_address: document.getElementById('AgentIPAddressAdd').value,
        agent_port: document.getElementById('AgentPortAdd').value,
        agent_description: document.getElementById('agentDescriptionAdd').value,
        datetime_create: new Date().toISOString(), /*toLocaleString().replace(/[\s,]/g, ' '),*/
        agent_group_id: parseInt(document.getElementById('agentGroupAdd').value),
        agent_type_id: parseInt(document.getElementById('agentTypeAdd').value),
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
            throw new Error(`Failed to delete object with ID ${buttonId}.`);
        }
    })
        .then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Handle the error message here (e.g., display it on the UI)
            } else if (data !== undefined) {
                if (data == 'Агент успешно добавлен') {
                    location.reload();
                } else if (data != 'Агент успешно добавлен') {
                    alert(data)
                }
                // Handle response data if available
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
}


function agentEditData() {
    const checkbox = document.getElementById('agentStatusEdit');
    const checkboxValue = checkbox.checked ? 1 : 0;
    const agent_id = document.getElementById('agentIDEdit').value
    const agentData = {
        id: agent_id,
        agent_name: document.getElementById('agentNameEdit').value,
        agent_mac_address: document.getElementById('AgentMacAddressEdit').value,
        agent_ip_address: document.getElementById('AgentIPAddressEdit').value,
        agent_port: document.getElementById('AgentPortEdit').value,
        agent_description: document.getElementById('agentDescriptionEdit').value,
        datetime_change: new Date().toISOString(),
        agent_group_id: parseInt(document.getElementById('agentGroupEdit').value),
        agent_type_id: parseInt(document.getElementById('agentTypeEdit').value),
        agent_status: checkboxValue
    };
    console.log(JSON.stringify(agentData))
    const csrftoken = getCookie('csrftoken');
    fetch(`/api/editAgentData/${agent_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(agentData)
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
            throw new Error(`Failed to delete object with ID ${buttonId}.`);
        }
    })
        .then(data => {
            if (data !== undefined && data.error) {
                console.error(data.error);
                // Handle the error message here (e.g., display it on the UI)
            } else if (data !== undefined) {
                if (data == 'Агент успешно изменен') {
                    location.reload();
                } else if (data != 'Агент успешно изменен') {
                    alert(data)
                }
                // Handle response data if available
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
}


function agentDeleteData() {
    var buttons = document.querySelectorAll(".deleteAgent");

    // Add event listeners to each button
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", handleClick);
    }

    // Event handler function
    function handleClick(event) {
        // Get the ID value from the button's data-id attribute
        const buttonId = event.currentTarget.getAttribute("data-id");

        // Make a DELETE request to the Django REST API endpoint
        const tokenizers = getCookie('csrftoken');
        fetch(`/api/deleteAgentData/${buttonId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': tokenizers,
            },
            // You can include credentials if required (e.g., for authentication)
            // credentials: 'include',
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
                throw new Error(`Failed to delete object with ID ${buttonId}.`);
            }
        })
            .then(data => {
                if (data !== undefined && data.error) {
                    console.error(data.error);
                    // Handle the error message here (e.g., display it on the UI)
                } else if (data !== undefined) {
                    if (data == 'Агент успешно удален') {
                        alert(data)
                        location.reload();
                    } else if (data != 'Агент успешно удален') {
                        alert(data)
                    }
                    // Handle response data if available
                }
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    }
}


function groupAddData() {
    const groupData = {
        agent_group_name: document.getElementById('groupNameAdd').value,
        agent_group_priority: document.getElementById('groupPriorityAdd').value,
        agent_group_description: document.getElementById('groupDescriptionAdd').value,
        datetime_create: new Date().toISOString()
    };
    console.log(JSON.stringify(groupData))
    const csrftoken = getCookie('csrftoken');
    fetch('http://127.0.0.1:8000/api/addGroupData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(groupData)
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

function groupEditData() {
    const group_id = document.getElementById('groupIDEdit').value
    const groupData = {
        id: document.getElementById('groupIDEdit').value,
        agent_group_name: document.getElementById('groupNameEdit').value,
        agent_group_priority: document.getElementById('groupPriorityEdit').value,
        agent_group_description: document.getElementById('groupDescriptionEdit').value,
        datetime_change: new Date().toISOString()
    };
    console.log(JSON.stringify(groupData))
    const tokenizers = getCookie('csrftoken');
    fetch(`/api/editGroupData/${group_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokenizers,
        },
        body: JSON.stringify(groupData)
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

function groupDeleteData() {
    var buttons = document.querySelectorAll(".deleteGroup");

    // Add event listeners to each button
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", handleClick);
    }

    // Event handler function
    function handleClick(event) {
        // Get the ID value from the button's data-id attribute
        const buttonId = event.currentTarget.getAttribute("data-id");

        // Make a DELETE request to the Django REST API endpoint
        const tokenizers = getCookie('csrftoken');
        fetch(`/api/deleteGroupData/${buttonId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': tokenizers,
            },
            // You can include credentials if required (e.g., for authentication)
            // credentials: 'include',
        })
            .then(response => {
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
                    throw new Error(`Failed to delete object with ID ${buttonId}.`);
                }
            })
            .then(data => {
                if (data !== undefined && data.error) {
                    console.error(data.error);
                    // Handle the error message here (e.g., display it on the UI)
                } else if (data !== undefined) {
                    if (data == 'Группа успешно удалена') {
                        alert(data)
                        location.reload();
                    } else if (data != 'Группа успешно удалена') {
                        alert(data)
                    }
                    // Handle response data if available
                }
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    }
}


function agentEditButtonListeners() {
    // Get references to all "Edit" buttons
    var editButtons = document.getElementsByClassName("editAgent btn btn-outline-primary btn-sm");

    // Add event listeners to each "Edit" button
    for (var i = 0; i < editButtons.length; i++) {
        editButtons[i].addEventListener("click", handleEdit);
    }

    // Event handler function for "Edit" button click
    function handleEdit(event) {
        // Get the parent table row (tr)
        const row = event.target.closest("tr");
        console.log(row)
        // Populate the input field
        document.getElementById('agentIDEdit').value = row.cells[0].innerText;
        document.getElementById('agentNameEdit').value = row.cells[2].innerText;
        document.getElementById('AgentMacAddressEdit').value = row.cells[5].innerText;
        document.getElementById('agentDescriptionEdit').value = row.cells[9].innerText;
        document.getElementById('AgentIPAddressEdit').value = row.cells[10].innerText;
        document.getElementById('AgentPortEdit').value = row.cells[11].innerText;
        document.getElementById('agentGroupEdit').value = row.cells[12].innerText;
        document.getElementById('agentTypeEdit').value = row.cells[13].innerText;
        document.getElementById('agentStatusEdit').checked = parseInt(row.cells[14].innerText);
    }
}

function groupEditButtonListeners() {
    // Get references to all "Edit" buttons
    var editGroupButtons = document.getElementsByClassName("editGroup btn btn-outline-primary btn-sm");

    // Add event listeners to each "Edit" button
    for (var i = 0; i < editGroupButtons.length; i++) {
        editGroupButtons[i].addEventListener("click", handleEdit);
    }

    // Event handler function for "Edit" button click
    function handleEdit(event) {
        // Get the parent table row (tr)
        const row = event.target.closest("tr");
        console.log(row)
        // Populate the input field
        document.getElementById('groupIDEdit').value = row.cells[0].innerText;
        document.getElementById('groupNameEdit').value = row.cells[1].innerText;
        document.getElementById('groupPriorityEdit').value = row.cells[2].innerText;
        document.getElementById('groupDescriptionEdit').value = row.cells[3].innerText;
    }
}

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

function sendRequestDjango() {

    const requestData = {
        ip_address: 'http://127.0.0.1:8000/api/graphData'

    };
    console.log(JSON.stringify(requestData))
    const csrftoken = getCookie('csrftoken');
    fetch('http://127.0.0.1:8000/api/sendRequestDjango', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(requestData)
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