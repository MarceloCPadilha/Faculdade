<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "ecom";
$conecta = mysqli_connect($server, $userDb, $passDb, $nameDb);

function buscarUsuarioByID($conecta, $id) {
    $id = filter_var($id, FILTER_VALIDATE_INT);
    if (!$id) {
        return [];
    }
    $sql = "SELECT usuarioID, nome, email, data FROM usuarios
    WHERE usuarioID = $id";
    $action = mysqli_query($conecta, $sql);
    return mysqli_fetch_assoc($action);
}

function buscarProdutoByID($conecta, $id) {
    $id = filter_var($id, FILTER_VALIDATE_INT);
    if (!$id) {
        return [];
    }
    $sql = "SELECT p.produtoID, p.nome AS nome, p.preco,
    COALESCE(NULLIF(p.imagem, ''), 'sem-foto.jpg') AS imagem,
    p.descricao, p.data, c.nome as categoria, c.categoriaID
    FROM produto p
    INNER JOIN categoria c on p.categoriaID = c.categoriaID
    WHERE p.produtoID = $id";
    $action = mysqli_query($conecta, $sql);
    return mysqli_fetch_assoc($action);
}

function listarUsuarios($conecta) {
    $sql = "SELECT * FROM usuarios ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}
function dadosProduto($conecta, $categorias = []) {
    $sql = "SELECT p.produtoID, p.nome, p.preco, p.imagem, p.descricao, p.data, c.nome AS categoria, c.categoriaID
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


function buscarCategorias($conecta) {
    $sql = "SELECT categoriaID, nome FROM categoria ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;

}

function cadastrarUsuario($conecta) {
    if(isset($conecta)) {
        $nome = mysqli_real_escape_string($conecta, $_POST['nome']);
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

function updateProduct($conecta, $id) {
    $id = filter_var($id, FILTER_VALIDATE_INT);
    if(!empty($id) and isset($_POST['atualizar'])) {

    }
}

function updateUser($conecta, $id) {
    $id = filter_var($id, FILTER_VALIDATE_INT);
    if (!empty($id) and isset($_POST['atualizar'])) {
        $nome = mysqli_real_escape_string($conecta, $_POST["nome"]);
        $email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST["senha"], PASSWORD_DEFAULT);
        $data = mysqli_real_escape_string($conecta, $_POST["nome"]);

        if (empty($nome) or empty($email)) {
            echo "Preencha todos os campos corretamente.";
        } else {
            $sql = $sql = "UPDATE usuarios SET nome = '$nome', email = '$email', data = '$data'";
            $sql .= !empty($_POST['senha']) ? ", senha = 'senha' " : "";
            $sql .= "WHERE id = $id";
            // ------
            $action = mysqli_query($conecta, $sql);
            if ($action) {
                echo "Usuário Atualizado com sucesso!";
                header("Refresh: 3; url=usuarios.php");
            } else {
                echo "Erro ao atualizar";
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
                header("location: catalogo.php");
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

    function upadateProduto($conecta) {
        
}
?>
