
// ------------------------------------------------------

const imageOne = document.getElementById("imageOne");
const imageTwo = document.getElementById("imageTwo");

const buttonOne = document.getElementById("buttonOne");
const buttonTwo = document.getElementById("buttonTwo");
const buttonThree = document.getElementById("buttonThree");

var button1 = 0 
var button2 = 0
var button3 = 0 

// ------------------------------------------------------

function toImage1(){

    imageOne.src = "images/bg1.jpg";
    imageTwo.src = "images/1.jpg";

    button1 += 1
    // buttonOne.innerHTML = button1

    button1.disabled = true;
    button2.disabled = false;
    button3.disabled = false;

}

function toImage2(){

    imageOne.src = "images/bg2.jpg";
    imageTwo.src = "images/2.jpg";

    button2 += 1
    // buttonTwo.innerHTML = button2

    button1.disabled = false;
    button2.disabled = true;
    button3.disabled = false;

}

function toImage3(){

    imageOne.src = "images/bg3.jpg";
    imageTwo.src = "images/3.jpg";

    button2 += 1
    // buttonThree.innerHTML = button3

    button1.disabled = false;
    button2.disabled = false;
    button3.disabled = true;

}

