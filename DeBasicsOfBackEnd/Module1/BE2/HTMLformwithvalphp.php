<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = htmlspecialchars($_POST["name"]);
        $email = htmlspecialchars($_POST["email"]);
        echo "<h2>Welcome, $name!</h2>";
        echo "<p>Your email address is: $email</p>";
    }
    ?>