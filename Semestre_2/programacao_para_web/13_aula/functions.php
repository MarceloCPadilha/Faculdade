<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "ecom";
$conecta = mysqli_connect($server, $userDb, $passDb, $nameDb);

function dadosProduto($conecta) {
    $sql = "SELECT p.nome, p.preco, p.descricao, c.nome AS categoria
    FROM produto p
    INNER JOIN categoria c ON (p.categoriaID = c.categoriaID);";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}

function todosDadosDoProduto($conecta) {
    $sql = "SELECT p.produtoID, p.nome, p.preco, p.descricao, p.data, c.nome AS categoria, c.categoriaID
    FROM produto p
    INNER JOIN categoria c ON (p.categoriaID = c.categoriaID);";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}

function login($conecta) {
    if (isset($_POST['logar'])) {
        $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
        $senha = $_POST['senha'];
        if (!empty($email) and !empty($senha)) {
            $sql = "SELECT * FROM usuarios WHERE email = '$email'";
            $action = mysqli_query($conecta, $sql);
            $retorno = mysqli_fetch_assoc($action);
            if (!empty($retorno['email']) and password_verify($senha, $retorno['senha'])) {
                session_start();
                $_SESSION['email'] = $retorno['email'];
                $_SESSION['nome'] = $retorno['nome'];
                $_SESSION['ativa'] = true;
                header("location: usuarios.php");
            }else{
                echo "Usuário ou senha incorretos!";
            }
        }else{
            echo "Usuário ou senha inválidos";
        }
    }
}


?>