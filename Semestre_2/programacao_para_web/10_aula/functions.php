<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "meubanco";
$conecta = mysqli_connect($server, $userDb, $passDb, $nameDb);

// BUSCAR/SELECT
function buscar($conecta) {
    $sql = "SELECT * FROM usuarios ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);

    return $dados;
}

function insertUser($conecta) {
    if(isset($_POST["cadastrar"])) {
        $nome = mysqli_real_scape_string($conecta, $_POST["nome"]);
        $email = filter_input(INPUT_POST, "email", FILTER_VALIDADE_EMAIL);
        $senha = password_hash($_POST["senha"], PASSWORD_DEFAULT);
        $erros = [];
        if (empty($nome) or empty($email) or empty($senha)) {
            $erros[] = "Preencha Corretamente todos os campos";

        }else{
            $sql = "INSERT INTO usuarios (nome, email, senha, data)
            VALUES ('$nome', '$email', '$senha', NOW())";
            $action - mysqli_query($conecta, $sql);
            if ($actio) {
                echo "Usuário inserido com sucesso";
            }else{
                echo "Erro ao inserir";
            }
        }
    }
}

?>