

// const WindowWidth = mainElement.clientWidth;

// const WindowWidthWithLine = window.innerWidth;

// console.log(`Ширина полосы: ${WindowWidthWithLine-WindowWidth}`)

// function setScroll() {
//     window.scrollBy(0,100);
//     const windowSrollTop = window.pageYOffset;
//     console.log(windowSrollTop);
// }

// setScroll();
// setTimeout(setScroll,1000);


const but = document.getElementsByClassName('sub')
const search = document.getElementsByClassName('search');

console.log(search);
console.log(but);

document.addEventListener('mouseover', button);

function button(event){
    {
        if (event.target.closest('.sub')) {
            search.style.display = 'block';

        }
        if (!event.target.closest('.sub')) {
            search.classList.remove('.search');
        }

    }
}

