function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data))
}

// const draggables = document.querySelectorAll(".col-1");
// const containers = document.querySelectorAll(".col-1-");
//
// draggables.forEach(draggable => {
//
//   draggable.addEventListener("dragstart", () => {
//     draggable.classList.add("dragging");
//   });
//
//   draggable.addEventListener("dragend", () => {
//     draggable.classList.remove("dragging");
//   });
// });
//
// containers.forEach(container => {
//   container.addEventListener("dragover", e => {
//     e.preventDefault();
//     const afterElement = getDragAfterElement(container, e.clientX);
//     const draggable = document.querySelector(".dragging");
//     if (afterElement === undefined) {
//       container.appendChild(draggable);
//     } else {
//       container.insertBefore(draggable, afterElement);
//     }
//   });
// });
//
// function getDragAfterElement(container, x) {
//   const draggableElements = [
//     ...container.querySelectorAll(".draggable:not(.dragging)"),
//   ];
//
//   return draggableElements.reduce(
//     (closest, child) => {
//       const box = child.getBoundingClientRect();
//       const offset = x - box.left - box.width / 2;
//       // console.log(offset);
//       if (offset < 0 && offset > closest.offset) {
//         return { offset: offset, element: child };
//       } else {
//         return closest;
//       }
//     },
//     { offset: Number.NEGATIVE_INFINITY },
//   ).element;
// }