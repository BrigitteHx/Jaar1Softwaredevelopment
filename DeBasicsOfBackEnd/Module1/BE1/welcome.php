<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>De ingevulde gegevens zijn:</h1>

    <?php
    if (isset($_GET['naam']) && isset($_GET['email'])) {
        $naam = $_GET['naam'];
        $email = $_GET['email'];

        echo "<p>Naam: $naam</p>";
        echo "<p>Emailadres: $email</p>";
    } else {
        echo "<p>Geen gegevens ontvangen</p>";
    }
    ?>
</body>
</html>
