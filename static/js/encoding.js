'use strict';

const plaintext = document.getElementById('plaintext');

const cipherButtons = document.querySelectorAll('.cipher');

const subOpts = document.getElementById('subOpts'); 
const shiftOpts = document.getElementById('shiftOpts'); 
const vigOpts = document.getElementById('vigOpts'); 
const enigOpts = document.getElementById('enigOpts'); 

const subsitutionSubmits = document.querySelectorAll('.subSub');

for (const button of cipherButtons) {
    button.addEventListener('click', (evt) => {
        evt.preventDefault();

        const cipher = evt.target.classList;

        if (cipher.contains('sub')) {
            subOpts.classList.remove('hide');
        } else if (cipher.contains('shift')) {
            shiftOpts.classList.remove('hide');
        } else if (cipher.contains('vig')) {
            vigOpts.classList.remove('hide');
        } else if (cipher.contains('enig')) {
            enigOpts.classList.remove('hide');
        }

    });
}

for (const button of subsitutionSubmits) {
    button.addEventListener('click', (evt) => {
        evt.preventDefault();

        
    });
}

