// de slimme oppasser

// var giraf = 0;
// var struisvogel = 0;
// var zebra = 0;
// var input;

// function hoeveelDieren(){
//     while (input != "stop"){
//         input = prompt("Welk dier wilt u toevoegen? Kies uit 'giraf', 'zebra' of 'struisvogel'. Om te stoppen zeg 'stop'. ");


//     if (input == "giraf"){
//         var girafTotaal = prompt("Hoeveel Giraffen zijn er?");
//         giraf += girafTotaal;
//     }

//     else if (input == "struisvogel"){
//         var struisTotaal = prompt("Hoeveel Struisvogels zijn er?");
//         struisvogel += struisTotaal;
//     }

//     else if (input == "zebra"){
//         var zebraTotaal = prompt("Hoeveel Zebras zijn er?");
//         zebra += zebraTotaal;
//     }
// }
// }

// hoeveelDieren();

// const girafPoten = 4;
// const struisPoten = 2;
// const zebraPoten = 4;

// function totaalPoten(){

//     var totaalPotenGiraf = giraf * girafPoten;
//     var totaalPotenStruis = struisvogel * struisPoten;
//     var totaalPotenZebra = zebra * zebraPoten;
//     var totaalPoten = totaalPotenGiraf + totaalPotenStruis + totaalPotenZebra;

//     if (giraf > 0){
//         document.write("Er zijn ", giraf, " giraffen met ", totaalPotenGiraf, " poten. ");
//         document.write("<br><br>");
//     }

//     if (struisvogel > 0){
//         document.write("Er zijn ", struisvogel, " struisvogels met ", totaalPotenStruis, " poten. ");
//         document.write("<br><br>");
//     }

//     if (zebra > 0){
//         document.write("Er zijn ", zebra, " zebra's met ", totaalPotenZebra, " poten. ");
//         document.write("<br><br>");
//     }

//     document.write("Het totale aantal poten is ", totaalPoten);
// }

// totaalPoten();

function TotaalPoten(aantalGiraf,aantalStruis,aantalZebra){
    const girafPoten = 4;
    const struisPoten = 2;
    const zebraPoten = 4;
    totaalAantalPoten = parseInt((aantalGiraf * girafPoten) + (aantalStruis * struisPoten) + (aantalZebra * zebraPoten));
    return totaalAantalPoten
}

aantalGiraf = prompt("Hoeveel Giraffen zijn er?");
aantalStruis = prompt("Hoeveel Struisvogels zijn er?");
aantalZebra = prompt("Hoeveel Zebra's zijn er?");

// totaalAantalPoten = (TotaalPoten(aantalGiraf,aantalStruis,aantalZebra));

console.log("Het totaal aantal poten is ", totaalAantalPoten);




