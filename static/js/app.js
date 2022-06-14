'use strict';
let admin = 'niaz';

function gradColor() {
    let elemmas = document.getElementsByTagName('tr');
    for (let i = 0; i < elemmas.length; i++) {
        if (i % 2 == 0) {
            elemmas[i].style.backgroundColor = '#303e3a';
        }
        else {
            elemmas[i].style.backgroundColor = '#3b4f3c';
        }
    }
}

function defPhAdd() {
    document.getElementById('id_name').setAttribute('placeholder', 'Название товара');
    document.getElementById('id_type').setAttribute('placeholder', 'Измерение(шт, кв.м и т.д.)');
}

function getElemVals() {
    let listInputs = document.getElementsByClassName('inputstr');
    let vals = '';
    for (let i = 0; i < listInputs.length; i++) {
        let value = listInputs[i].value;
        if (value != '') {
            vals += `${value} `
        }
        else {
            vals += `0 `
        }
    }
    document.getElementById('id_mas').value = vals;
}
function resetElemVals() {
    let listInputs = document.getElementsByClassName('inputstr');
    let vals = '';
    for (let i = 0; i < listInputs.length; i++) {
        vals += '0 '
    }
    document.getElementById('id_mas').value = vals;
}