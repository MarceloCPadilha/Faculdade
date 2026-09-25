<?php

session_start();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem vindo ao admin do site</title>
    <link rel="stylesheet" href="./style/style.css">
</head>
<body>
    <?php if (isset($_SESSION['ativa'])) : ?>

    <h1>
        Bem vindo, <?php echo $_SESSION['usuario'];?> ao painel administrativo do site!
    </h1>

    <h2>
        Você está logado com email: <?php echo $_SESSION['email'];?>
    </h2>

    <a href="logout.php">Sair</a>

    <?php
        else:
            echo "Você não tem acesso a esta página!";
        endif;
    ?>
    
</body>
</html>