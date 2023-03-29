

function handleClick(clickEvent){

    // alert("hello from JS");

    // console.dir(clickEvent);

    // clickEvent.target.classList.add("blue");              > laat class/button na click blauw worden

    // clickEvent.target.classList.toggle("blue");           > laat class/button na clikc blauw worden, click not een keer en kleur gaat terug naar begin

    if (clickEvent.target.id == "button1"){                      
        clickEvent.target.classList.add("blue") ;             
    }
    else {
        clickEvent.target.classList.toggle("blue");
    }
    result.innerHTML = `Button met id <strong> ${clickEvent.target.id} </strong> was geklikt`;  // > text veranderen wanneer geklikt 
}

// handleClick({name:'this is my clickEvent', id: 1234})

button1.onclick = handleClick;
button2.onclick = handleClick; 
fakeButton.onclick = handleClick;

