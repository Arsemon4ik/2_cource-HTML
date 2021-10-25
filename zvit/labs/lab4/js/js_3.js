const button = document.getElementById('#');
const help = document.querySelector('p')

console.log(button);
console.log(help);

button.addEventListener('mouseover',mouse_in)
button.addEventListener('mouseout',mouse_out)

function mouse_in() {
    help.style.display = 'block';

}

function mouse_out() {

    help.style.display = 'none';
}

