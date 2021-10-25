
let arr = [];
let len = prompt("Введите длину масива!");

// Заполняем рандомными числами на заданную длину пользователем
for (let index = 0; index < len; index++) {
    arr[index] = Math.round(Math.random()*20);

}

for (let index = 0; index < len; index++) {
    console.log(arr[index]);
}
console.log('----');

let min = arr[0];
for (let index = 0; index < len; index++) {
    if (arr[index] < min) {
        min = arr[index];
    }

}
console.log("Min element: " + min);

// Записываем мин.Элемент в начало масива
arr.unshift(min);

console.log('----');
for (let index = 0; index < len; index++) {
    console.log(arr[index]);
}
console.log('----');


// Сортируем методом выбора
for (let i = 0, l = arr.length, k = l - 1; i < k; i++) {
    let indexMin = i;
    for (let j = i + 1; j < l; j++) {
        if (arr[indexMin] > arr[j]) {
            indexMin = j;
        }
    }
    if (indexMin !== i) {
        [arr[i], arr[indexMin]] = [arr[indexMin], arr[i]];
    }
}

// Отзеркаливаем массив что бы было от большего к меньшему
arr.reverse();

// Выводим в консоль
for (let index = 0; index < len; index++) {
    console.log(arr[index]);
}