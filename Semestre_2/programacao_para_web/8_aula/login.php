<?php

$emailAcesso = "admin@gmail.com";
$senhaAcesso = "admin123";

if (isset($_POST['logar'])) {
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $usuario = filter_input(INPUT_POST, 'usuario', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $senha = $_POST['senha'];
    if (!empty($senha) and !empty($email)) {
        if($emailAcesso == $email and $senhaAcesso == $senha) {
            session_start();
            $_SESSION['usuario'] = $usuario;
            $_SESSION['email'] = $email;
            $_SESSION['ativa'] = true;
            
            echo "<a href='admin.php'>Acessar Admin</a>";

        } else {
            echo "E-mail ou senha incorretos!";
        }
    } else {
        echo "E-mail ou senha inválidos";
    }
     
}

/*
// Inicia a sessão
session_start();

// Váriaveis de sessão
$_SESSION['usuario'] = "Carlos da Silva";
$_SESSION['email'] = "carlos@gmail.com";
$_SESSION['ativa'] = TRUE;

echo "<a href='admin.php'>Acessar Admin</a>";
*/

?>