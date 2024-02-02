<?php 

// <!-- voorbeeld opgave -------------------------------------------------------------------->

// function lijst_optellen($nummers) {
//     $sum = 0;
//     foreach ($nummers as $number) {

//         $sum += $number;

//     }
//     return $sum;
// }
// $result = lijst_optellen($getallenLijst);
// $getallenLijst = [1, 2, 3, 4];
// echo $result; // Output: 10

// <!-- opgave 1 ---------------------------------------------------------------------------->

function evenEvenGetallen($getallenLijst) {
    $sum = 0;
  
    foreach ($getallenLijst as $getal) {
      if ($getal % 2 === 0) {
        $sum += $getal;
      }
    }
  
    return $sum;
  }
  
$getallenLijst = [1, 2, 3, 4];
$result = evenEvenGetallen($getallenLijst);
echo $result; // moet output 6 zijn 

// <!-- opgave 2 ---------------------------------------------------------------------------->

function langsteWoordEruit($woorden) {
    $woordLengte = 0;
    $langsteWoord = '';

    foreach ($woorden as $woorden) {
        if (strlen($woorden) > $woordLengte) {
            $woordLengte = strlen($woorden);
            $langsteWoord = $woorden;
        }
    }
    return $langsteWoord;
}

$woorden =  ['kat', 'hond', 'olifant'];
$result = langsteWoordEruit($woorden);
echo $result; // moet output olifant zijn 

// <!-- opgave 3 ---------------------------------------------------------------------------->

// SORT:
// function sorteerNummer($nummers) {
//     rsort($nummers);
//     return $nummers;
// }

// $nummers = [3, 1, 4, 2];
// $result = sorteerNummer($nummers);
// print_r($result);

// GOEDE:
function sorteerNummer($nummers){
    $lengte = count($nummers);

    for ($i = 0; $i < $lengte - 1; $i++) {
        for ($j = 0; $j < $lengte - $i - 1; $j++) {
            if ($nummers[$j] > $nummers[$j + 1]) {
                // switch nummer naar goede volgorde/ plaats vanaf hier
                $nummers2 = $nummers[$j];
                $nummers[$j] = $nummers[$j + 1];
                $nummers[$j + 1] = $nummers2;
            }
        }
    }
    return $nummers;
}

$nummers = [3, 1, 4, 2];
$result = sorteerNummer($nummers);
print_r($result);

// bubble sort algoritme 
// algoritme dat door een lijst gaat en aangrenzende elementen vergelijkt/ omwisselt
// stappen:
// 1) vergelijk element 1 en 2, als 1 groter is dan 2 wissel ze om anders laat ze staan
// 2) ga zo de hele lijst door tot het grootste element naar de laatste plek is 

// <!-- opgave 4 ---------------------------------------------------------------------------->

function grootsteDeler($getal1, $getal2) {

    while ($getal1 != $getal2) {
        if ($getal1 > $getal2) {
            $getal1 -= $getal2;
        } else {
            $getal2 -= $getal1;
        }
    }
    return $getal1;
}

$result = grootsteDeler(20,25);
echo "De grootste deler is " . $result;

?>

<!-- ------------------------------------------------------------------------------------->

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>syntax</title>
        <style></style>
    </head>

    <body>
        <h1> <?php ?> </h1>
    </body>
    
</html>