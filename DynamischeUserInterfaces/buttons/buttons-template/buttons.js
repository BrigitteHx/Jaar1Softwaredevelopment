
let countButton1 = 0;
let countButton2 = 0;
let countButton3 = 0;

function clickEvent(event) {
  const container = event.target.parentElement;

  // verwijder click classes behalve current one
  container.classList.remove("clickOne", "clickTwo", "clickThree");

  // click class
  if (event.target.id === 'buttonOne') {
    container.classList.add("clickOne");
    document.getElementById("imageBelow").style.backgroundImage = "url('1.jpg')";
    countButton1 += 1;
    // console.log(countButton1);
    document.getElementById('buttonOne').innerHTML = countButton1;
  } else if (event.target.id === 'buttonTwo') {
    container.classList.add("clickTwo");
    document.getElementById("imageBelow").style.backgroundImage = "url('2.jpg')";
    countButton2 += 1;
    // console.log(countButton2);
    document.getElementById('buttonTwo').innerHTML = countButton2;
  } else {
    container.classList.add("clickThree");
    document.getElementById("imageBelow").style.backgroundImage = "url('3.jpg')";
    countButton3 += 1;
    // console.log(countButton3);
    document.getElementById('buttonThree').innerHTML = countButton3;
  }
}

const button1 = document.getElementById('buttonOne');
const button2 = document.getElementById('buttonTwo');
const button3 = document.getElementById('buttonThree');

buttonOne.onclick = clickEvent;
buttonTwo.onclick = clickEvent;
buttonThree.onclick = clickEvent;

