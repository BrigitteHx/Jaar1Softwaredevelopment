let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n"+
"Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

alert(uitleg);
let gewenste_aantal_autos = prompt("Hoeveel autos wilt u kwijt in de parkeergarage?");
// Berekenen hier het aantal verdiepingen

if (gewenste_aantal_autos <= 0){
    alert('Het is niet mogelijk om minder dan 0 autos in the vullen.')
} else if (gewenste_aantal_autos <= 80){
    var verdieping= 1; 
    parkeren = true; 
} else if (gewenste_aantal_autos >80){
    var verdieping = Math.ceil(gewenste_aantal_autos/120 + 1); // +1 van begane grond 
    parkeren = true; 
}

// let antwoord = "Ik heb nog geen idee hoeveel verdiepingen er moeten komen :-( ";
// document.getElementById("antwoord").innerText = antwoord;

if (parkeren==true){
    let antwoord = "Om het gewenste aantal autos kwijt te kunnen heb ik " + verdieping + "x verdieping(en) nodig.";
    document.getElementById("antwoord").innerText = antwoord; // manier 1
    // document.write("antwoord").innerText = antwoord; // manier 2
    // console.log("antwoord").innerText = antwoord; // manier 3
}

console.log("Om het gewenste aantal autos kwijt te kunnen heb ik" + verdieping + "nodig.")
