

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


const item = document.querySelector('.lesson__block')

const getCoordFirstButton = item.getBoundingClientRect();

console.log(getCoordFirstButton);

