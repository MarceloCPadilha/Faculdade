
<?php

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./style/style.css">
</head>
<body>

    <!-- Mothod -> get(mostra os dados na url) ou post -->
    <form action="./actions/action.php" method="post">
        <input type="text" name="nome" placeholder="Seu nome: " minlength="3" required>
        <input type="email" name="email" placeholder="Seu email: ">
        <input type="number" name="idade" placeholder="Sua idade: ">
        <input type="submit" name="enviar">    
    </form>


    
</body>
</html>