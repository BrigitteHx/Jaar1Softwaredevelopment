<!DOCTYPE html>
<html>
<head>
    <title>Mad Libs</title>
    <style>
        body {
            background-color: #333;
            color: white;
            font-family: Arial, sans-serif;
        }
        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            margin: 20px auto;
            width: 80%;
            max-width: 600px;
            color: black;
        }
        .menu {
            text-align: center;
        }
        .menu a {
            margin: 10px;
            text-decoration: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="menu">
        <a href="?page=paniek">Er heerst paniek...</a>
        <a href="?page=onkunde">Onkunde</a>
    </div>

    <?php
    function generateFunnyStory($answers) {
        $vraag1 = $answers["vraag1"];
        $vraag2 = $answers["vraag2"];
        $vraag3 = $answers["vraag3"];
        $vraag4 = $answers["vraag4"];
        $vraag5 = $answers["vraag5"];
        $vraag6 = $answers["vraag6"];
        $vraag7 = $answers["vraag7"];

        if ($_GET['page'] === 'paniek') {
            return "Er heerst paniek in het koninkrijk Gallifrey. Koning $vraag2 is ten einde raad en als koning $vraag2 ten einde raad is, dan roept hij zijn ten-einde-raadsheer $vraag6!<br><br>\"$vraag6! Het is een ramp! Het is een schande!\"<br><br>\"Sire, Majestet Uwe Luidruchtigheid, wat is er aan de hand?\"<br><br>\"Min $vraag1 is verdwenen. Zo maar, zonder waarschuwing. En ik had net $vraag5 voor hem gekocht.\"<br><br>\"Majestet, uw $vraag1 komt vast vanzelf weer terug?\"<br><br>\"Ja, da's leuk en aardig, maar hoe moet ik in de tussentijd $vraag8 leren?\"<br><br>\"Maar Sire, daar kunt u toch uw $vraag7 voor gebruiken.\"<br><br>\"$vraag6, je hebt helemaal gelijk! Wat zou ik doen als ik jou niet had.\"<br><br>\"Mi $vraag4, Sire.\"";
        } elseif ($_GET['page'] === 'onkunde') {
            return "Er zijn veel mensen die niet kunnen $vraag1. Neem nou meneer $vraag2. Zelfs met de hulp van een $vraag4 of zelfs $vraag3 kan meneer $vraag2 niet $vraag1. Dat heeft niet te maken met een gebrek aan $vraag5, maar met een te veel aan $vraag6. Te veel $vraag6 leidt tot $vraag7 en dat is niet goed als je wilt $vraag1. Helaas voor meneer $vraag2.";
        } else {
            return "Oeps! Ongeldige pagina.";
        }
    }

    $currentPage = isset($_GET['page']) ? $_GET['page'] : 'paniek';

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $answers = array(
            "vraag1" => $_POST["vraag1"],
            "vraag2" => $_POST["vraag2"],
            "vraag3" => $_POST["vraag3"],
            "vraag4" => $_POST["vraag4"],
            "vraag5" => $_POST["vraag5"],
            "vraag6" => $_POST["vraag6"],
            "vraag7" => $_POST["vraag7"],
        );

        $funnyStory = generateFunnyStory($answers);


        echo "<div class='form-container'>$funnyStory</div>";
    } else {

        include($currentPage . '.php');
    }
    ?>

    <footer>
        &copy; <?php echo date("Y"); ?> Brigitte Heijkoop
    </footer>
</body>
</html>
