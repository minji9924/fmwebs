function allowDrop(ev) {
    ev.preventDefault();

}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    alert(ev.target.childNodes.length)
    if (ev.target.childElementCount < 1) {
        ev.target.appendChild(document.getElementById(data));
    }



}




