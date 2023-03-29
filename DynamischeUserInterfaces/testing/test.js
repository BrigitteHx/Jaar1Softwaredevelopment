//  test


console.log('nu zitten we in de logic!');

function clicked_button(event){
    console.log('clicked button');
    var div = document.getElementById('result');
    // console.dir(div); 
    div.innerHTML = 'Hallo vannuit de button...';
}

button = document.getElementById('start');

button.onclick = clicked_button; 
// button.onmouseover = hover_button; 

console.dir(button);    
// laat zien wat the button doet, haalt alle info 

// clicked_button(1);
