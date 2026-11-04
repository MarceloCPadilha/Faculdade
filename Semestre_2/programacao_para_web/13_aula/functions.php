<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "ecom";
$conecta = mysqli_connect($server, $userDb, $passDb, $nameDb);

function dadosProduto($conecta, $categorias = []) {
    $sql = "SELECT p.produtoID, p.nome, p.preco, p.descricao, c.nome AS categoria, c.categoriaID
            FROM produto p
            INNER JOIN categoria c ON p.categoriaID = c.categoriaID";
    if (!empty($categorias)) {
        $categorias = array_map('intval', $categorias);
        $categorias = array_unique(array_filter($categorias, function ($id) {
                return $id > 0;
            })
        );
        if (!empty($categorias)) {
            $ids = implode(',', $categorias);
            $sql .= " WHERE c.categoriaID IN ($ids)";
        }
    }
    $resultado = mysqli_query($conecta, $sql);
    if (!$resultado) {
        die("Erro na consulta: " . mysqli_error($conecta));
    }
    return mysqli_fetch_all($resultado, MYSQLI_ASSOC);
}

function cadastrarUsuario($conecta) {
    if(isset($conecta)) {
        $nome = mysqli_real_escape_string($conect, $_POST['nome']);
        $email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST["senha"], PASSWORD_DEFAULT);
        if(empty($nome) or empty($email) or empty($senha)) {
            echo "Preencha todos os campos";
        }else{
            $sql = "INSERT INTO usuarios (nome, senha, email, data)
            VALUES ('$nome', '$senha', '$email', NOW())";
            $action = mysqli_query($conecta, $sql);
            if($action) {
                echo "Usuário inserido com sucesso!";
            }else{
                echo "Ocorreu algum erro.";
             }
        }
    }
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

function getCategorias($conecta){
    $sql = "SELECT nome, categoriaID FROM categoria ORDER BY nome;";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
    }

?>