function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}

function dclick(ev) {
    // ev.preventDefault();
    // ev.dataTransfer.setData("text", ev.target.id);
    // var data = ev.dataTransfer.getData("text");
    alert(ev.target.id);
    if (1 < ev.target.id < 8) {
        ev.target.appendChild(document.getElementById());
    }

}
