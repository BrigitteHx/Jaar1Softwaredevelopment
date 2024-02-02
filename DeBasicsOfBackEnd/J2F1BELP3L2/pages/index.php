<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <title><?php include("../includes/header.php"); ?></title>
</head>
<body>
    <?php include("../includes/header.php"); ?>

    <div id="content">
        <?php
        if (isset($_GET['onderwerp']) && file_exists($_GET['onderwerp'] . '.php')) {
            include("../pages/" . $_GET['onderwerp'] . '.php');
        }
        ?>
    </div>

    <?php include("../includes/footer.php"); ?>
</body>
</html>