
const button = document.querySelector('input');
const paragraph = document.querySelector('p');

button.addEventListener('click', updateButton);

function updateButton() {
    if (button.value === 'Start machine') {
        button.value = 'Stop machine';
        paragraph.textContent = 'The machine has started!';
    } else {
        button.value = 'Start machine';
        paragraph.textContent = 'The machine is stopped.';
    }
}


function myFunction() {
    var x = document.getElementById("frm1");
    var text = "";
    var i;
    for (i = 0; i < x.length; i++) {
        text += x.elements[i].value + "<br>";
    }
    document.getElementById("demo").innerHTML = text;
}