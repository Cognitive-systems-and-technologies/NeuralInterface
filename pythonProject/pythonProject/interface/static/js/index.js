
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