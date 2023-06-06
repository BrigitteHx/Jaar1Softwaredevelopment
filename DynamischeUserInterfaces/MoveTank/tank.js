// get image and demo elements 
var image = document.getElementById("image");
var demo = document.getElementById("demo");

// window width/ heigh
var width = window.innerWidth - 100;
var height = window.innerHeight - 100;

// onkey event 
document.onkeydown = checkKey;

// rotation tank 90 degrees
image.style.transform = "rotate(90deg)";

// left right up down position
let position = 0;
let leftAndRight = 5;
let upAndDown = 5;

// function werkt wanneer click op key 
function checkKey(e) {
    // position start + 164
    position = position + 164;

    // clicked key
    console.log("key nr = " + e.keyCode);

    // event object  
    e = e || window.event;

    // welke key was clicked
    if (e.keyCode == 32) {
        // if spacebar geklikt
        console.log("spacebar");
        
        // draai 90 degrees
        image.style.transform = "rotate(90deg)";
        
        // update position tank
        image.style.backgroundPosition = `-${parseInt(move)}px 0px`;

    } else if (e.keyCode == '38') {
        // if up arrow geklikt
        console.log("Up arrow");
        
        
        upAndDown = upAndDown - 5;
        
        // draai 360 degrees
        image.style.transform = "rotate(360deg)";
        
        // update background position
        image.style.backgroundPosition = `-${parseInt(position)}px 0px`;
        
        // update top position
        demo.style.top =`${parseInt(upAndDown)}px`;

    } else if (e.keyCode == '40') {
        // if down arrow geklikt
        console.log("down arrow");
        
        
        upAndDown = upAndDown + 5;
        
        // draai 180 degrees
        image.style.transform = "rotate(180deg)";
        
        // update background position
        image.style.backgroundPosition = `-${parseInt(position)}px 0px`;
        
        // update top position
        demo.style.top =`${parseInt(upAndDown)}px`;

    } else if (e.keyCode == '37') {
        // if left arrow key geklikt 
        console.log("left arrow");
        
        
        leftAndRight = leftAndRight - 5;
        
        // draai 90 degrees
        image.style.transform = "rotate(-90deg)";
        
        // update background position
        image.style.backgroundPosition = `-${parseInt(position)}px 0px`;
        
        // update left position (demo)
        demo.style.left =`${parseInt(leftAndRight)}px`;

    } else if (e.keyCode == '39') {
        // if right arrow geklikt
        console.log("right arrow");
        
       
        leftAndRight = leftAndRight + 5;
        
        // draai 90 degrees
        image.style.transform = "rotate(90deg)";
        
        // update background position
        image.style.backgroundPosition = `-${parseInt(position)}px 0px`;
        
        // update left position
        demo.style.left =`${parseInt(leftAndRight)}px`;

    }
    
    // check position minder dan 1312
    if (position < 1312) {
        // position +256
        position = position + 256;
    } else {
        // reset position
        position = 256;
    }
    
    // check up/down kleiner dan 0 & up/down groter dan height
    if (upAndDown < 0 || upAndDown > height){
        // reset up/down
        upAndDown = 0;
    }
    
    // check left/right  kleiner dan 0 & up/down groter dan width 
    if (leftAndRight < 0 || leftAndRight > width ){
        // reset left/right
        leftAndRight = 0;
    }
    
    // log left/right 
    console.log(`left or right: ${leftAndRight}`);
}
