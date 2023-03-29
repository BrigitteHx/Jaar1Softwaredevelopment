0// M01.O4 - Horeca App

// var bier = 0;
// var wijn = 0;
// var fris = 0; 

// var input; 

// function bestelling(){
//     while (input != "stop"){
//         input = prompt("Wat wilt u drinken? Kies uit 'bier, wijn, fris'.")

//     if (input == "bier"){
//         var bierTotaal = prompt("Hoeveel bier wilt u bestellen?");
//         bier += bierTotaal;
//         // console.log(bier, "x", bierPrijs);
//     }

//     else if (input == "wijn"){
//         var wijnTotaal = prompt("Hoeveel wijn wilt u bestellen?");
//         wijn += wijnTotaal;
//         // console.log(wijn, "x", wijnPrijs);
//     }

//     else if (input == "fris"){
//         var frisTotaal = prompt("Hoeveel fris wilt u bestellen?");
//         fris += frisTotaal;
//         // console.log(fris, "x", frisPrijs);
//     }
// }
// }

// bestelling();

// // ---------------------------------------------------------------------------------------------------------------

// // prijzen:
// const bierPrijs = 5;
// const wijnPrijs = 6;
// const frisPrijs = 3;

// function prijsBerekenen(){

//     var totaalBierPrijs = bier * bierPrijs;
//     var totaalWijnPrijs = wijn * wijnPrijs;
//     var totaalFrisPrijs = fris * frisPrijs;
//     var totaal = totaalBierPrijs+totaalWijnPrijs+totaalFrisPrijs;

//     if (bier > 0){
//         document.write("U heeft", bier, "bier.", "Voor", totaalBierPrijs); 
// 		document.write("<br><br>");	
//     }

//     if (wijn > 0){
//         document.write("U heeft", wijn, "wijn.", "Voor", totaalWijnPrijs);
// 		document.write("<br><br>");	
//     }

//     if (fris > 0){
//         document.write("U heeft", fris, "fris.", "Voor", totaalFrisPrijs);
// 		document.write("<br><br>");	
//     }

//     document.write("De totale prijs is", totaal)
// }

// prijsBerekenen(); 

// ----------------------------------------------------------------------------------------------------------------------------------------------

// var bestelling = true 
// var hoeveel = 0 

// var drankMenu = {
//     "bier" : {naam: "bier", prijs : 5, hoeveel: 0},
//     "wijn" : {naam: "wijn", prijs : 6, hoeveel: 0},
//     "fris" : {naam: "fris", prijs : 3, hoeveel: 0},
// }

// while (bestelling){
//     inputDrank = prompt("Wat wilt u bestellen van het drank menu? ");

//     if (inputDrank in drankMenu){
//         inputHoeveel = parseInt(prompt("Hoeveel van uw gekozen drank wilt u?"));
//         // hoeveel += drankMenu[inputDrank].inputHoeveel;
//         drankMenu[inputDrank].hoeveel += inputHoeveel;
//         // voegt toe aan hoeveel in drank menu 
//     }
//     else if (inputDrank == "stop"){
//         var bestelling = false;
//     }
//         // else if (!(inputDrank in drankMenu)){
//     else {
//         console.log("Dit ken ik niet, kies AUB tussen bier wijn of fris.");
//         // var bestelling = true;
//     }
// }

// // var totaalPrijsBier = (drankMenu.bier.prijs * drankMenu.bier.hoeveel);
// // // console.log(totaalPrijsBier);
// // var totaalPrijsWijn = (drankMenu.wijn.prijs * drankMenu.wijn.hoeveel);
// // var totaalPrijsFris = (drankMenu.fris.prijs * drankMenu.fris.hoeveel);

// // var totaalPrijs = (totaalPrijsBier + totaalPrijsWijn + totaalPrijsFris);

// // console.log("U heeft ",drankMenu.bier.naam," voor ", totaalPrijsBier );
// // console.log("U heeft ",drankMenu.wijn.naam," voor ", totaalPrijsWijn );
// // console.log("U heeft ",drankMenu.fris.naam," voor ", totaalPrijsFris );
// // console.log("De totaal prijs is ", totaalPrijs.toFixed(2));

// var totaalPrijs = (drankMenu.bier.prijs * drankMenu.bier.hoeveel + drankMenu.wijn.prijs * drankMenu.wijn.hoeveel + drankMenu.fris.prijs * drankMenu.fris.hoeveel);
// console.log("U heeft ",drankMenu.bier.naam," voor ", (drankMenu.bier.prijs * drankMenu.bier.hoeveel) );
// console.log("U heeft ",drankMenu.wijn.naam," voor ", (drankMenu.wijn.prijs * drankMenu.wijn.hoeveel) );
// console.log("U heeft ",drankMenu.fris.naam," voor ", (drankMenu.fris.prijs * drankMenu.fris.hoeveel) );
// console.log("De totaal prijs is ", totaalPrijs.toFixed(2));


// ----------------------------------------------------------------------------------------------------------------------------------------------

var drankMenu = {
    "bier": { naam: "bier", prijs: 5, hoeveel: 0 },
    "wijn": { naam: "wijn", prijs: 6, hoeveel: 0 },
    "fris": { naam: "fris", prijs: 3, hoeveel: 0 }
};

function bestellenDrank(drankMenu){
    var bestelling = true;
    while (bestelling) {
        var inputDrank = prompt("Wat wilt u bestellen van het drank menu?");

        if (inputDrank in drankMenu) {
            var inputHoeveel = parseInt(prompt("Hoeveel van uw gekozen drank wilt u?"));
            drankMenu[inputDrank].hoeveel += inputHoeveel;
            // inputHoeveel += drankMenu[inputDrank].hoeveel;
        } else if (inputDrank == "stop") {
            bestelling = false;
        } else {
            console.log("Dit ken ik niet, kies AUB tussen bier, wijn of fris.");
        }
    }
    return drankMenu;
}

drankMenu = bestellenDrank(drankMenu);

function printenBonnetje(drankMenu){
    var totaalPrijs = 0;
    for (var key in drankMenu) {
        console.log("U heeft " + drankMenu[key].hoeveel, drankMenu[key].naam + " voor " + (drankMenu[key].prijs * drankMenu[key].hoeveel) + " euro.");
        totaalPrijs += drankMenu[key].prijs * drankMenu[key].hoeveel;
    }
    console.log("De totaal prijs is " + totaalPrijs.toFixed(2));
    return drankMenu;
}

drankMenu = printenBonnetje(drankMenu)