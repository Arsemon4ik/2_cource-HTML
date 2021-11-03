
const button = document.getElementById('#');

console.log(button);

button.addEventListener('mouseover',mouse_over);
button.addEventListener('mouseout',mouse_out);

function mouse_over() {
    button.style.textDecoration = 'underline';
}
function mouse_out() {
    button.style.textDecoration = 'none';
}


