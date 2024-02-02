<!DOCTYPE html>
<html>
<head>
    <title>Form</title>
</head>
<body>

    <h1>Form</h1>

    <form action="" method="post">
        <label for="name">Name*:</label>
        <input type="text" id="name" name="name" value="<?php echo isset($_POST['name']) ? htmlspecialchars($_POST['name']) : ''; ?>" required><br><br>

        <label for="email">Email*:</label>
        <input type="email" id="email" name="email" value="<?php echo isset($_POST['email']) ? htmlspecialchars($_POST['email']) : ''; ?>" required><br><br>

        <input type="submit" value="Submit">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST["name"];
        $email = $_POST["email"];

        // 1 voorbeeld van requirement: 
        if (empty($name) || empty($email)) {
            echo "<p style='color: red;'>Both name and email are required.</p>";
        } else {
            echo "<h2>Welcome, $name!</h2>";
            echo "<p>Your email address is: $email</p>";
        }
    }
    ?>

</body>
</html>
