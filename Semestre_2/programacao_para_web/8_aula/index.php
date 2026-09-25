<?php



?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login e senha</title>
</head>
<body>

    <form method="post" action="login.php">
        <input type="text" name="usuario" placeholder="Nome de usuário" required>
        <input type="email" name="email" placeholder="Seu e-mail" required>
        <input type="password" name="senha" placeholder="Sua Senha" required>
        <button name="logar">Acessar</button>
    </form>
    
</body>
</html>