<?php
    require_once "functions.php";
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login e senha</title>
    <link rel="stylesheet" href="./style/stylelogin.css">
</head>
<body>

    
    <div class="form">
        <form method="post">
            <div class="aviso">
                <?php login($conecta);?>
            </div>
            <input type="email" name="email" placeholder="Seu E-mail" required>
            <input type="password" name="senha" placeholder="Sua Senha" required>
            <button name="logar">Acessar</button>
        </form>
    </div>

</body>
</html>
