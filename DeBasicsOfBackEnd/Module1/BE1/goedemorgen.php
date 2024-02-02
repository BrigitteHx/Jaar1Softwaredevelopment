<!-- goedemorgen -->

<?php 
// function greeting() {
//     $currentTime = date('H:i');

//     if ($currentTime >= '06:00' && $currentTime < '12:00') {
//         return 'Goede morgen';
//     } elseif ($currentTime >= '12:00' && $currentTime < '18:00') {
//         return 'Goede middag';
//     } elseif ($currentTime >= '18:00' && $currentTime < '00:00') {
//         return 'Goede avond';
//     } else {
//         return 'Goede nacht';
//     }
// }

// function getCurrentTime() {
//     return date('H:i');
// }
// ?>  

<!-- <html>
<head>
    <title>Goedemorgen</title>
    <style>.container {
    text-align: center;
    margin-top: 200px;
}

body {
    background-image: url(morning.png);
}

h1 {
    font-size: 36px;
}

p {
    font-size: 18px;
}

body.morning {
    background-image: url(morning.png);
}

body.afternoon {
    background-image: url(afternoon.png);
}

body.evening {
    background-image: url(evening.png);
}

body.night {
    background-image: url(night.png);
}
</style>

</head>

<body>
    <div class="container">
    </div>
</body>
</html>  -->

<!-- ------------------------------------------------------------------------------------------ -->

<?php
    function greeting(){
        $currentTime = date('H:i'); 
        if($currentTime >= '06:00' && $currentTime < '12:00'){
            $greet = 'Goedemorgen! <br> Het is nu: '.$currentTime;

        }else if($currentTime >= '12:00' && $currentTime < '18:00'){
            $greet = 'Goedemiddag! <br> Het is nu: '.$currentTime;

        }else if($currentTime >= '18:00' && $currentTime < '00:00'){
            $greet = 'Goedenavond! <br> Het is nu: '.$currentTime;

        }else if($currentTime >= '00:00' && $currentTime < '06:00'){
            $greet = 'Goedenacht! <br> Het is nu: '. $currentTime;
        }

    return $greet;

    } 
    function pictures(){
         $currentTime = date('H:i'); 
            if( $currentTime >= '06:00' && $currentTime < '12:00'){
                return 'morning.png';

            }else if ($currentTime >= '12:00' && $currentTime < '18:00'){
                return 'afternoon.png';

            }else if ($currentTime >= '18:00' && $currentTime < '00:00'){
                return 'evening.png';

            }else if ($currentTime >= '00:00' && $currentTime < '06:00'){
                return 'night.png';
            }
        }
?>  

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Goedemorgen</title>

        <style>
            body {
                background-image: url('<?php echo pictures(); ?>');
                background-repeat: no-repeat;
                background-size: 100%;
            }
            .containter {
                color: white;

                /* midden */
                width: 250px;
                margin: auto;

            }
        </style>
    </head>

    <body>
        <div class="containter">

            <h1><?php echo greeting();?></h1>
            
        </div>
    </body>
    
</html>