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

    $sql = "SELECT p.produtoID, p.nome, p.preco, p.imagem, p.descricao, p.data, c.nome AS categoria, c.categoriaID
            FROM produto p
            INNER JOIN categoria c ON p.categoriaID = c.categoriaID
            WHERE p.produtoID = $id";
    $action = mysqli_query($conecta, $sql);
    $produto = mysqli_fetch_assoc($action);
    if (!$produto) {
        return [];
    }
    if (!empty($produto['imagem'])) {
        $produto['imagem'] = 'data:image/jpeg;base64,' .
            base64_encode($produto['imagem']);
    } else {
        $produto['imagem'] = 'sem-foto.jpg';
    }
    return $produto;
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



function comprimirImagem($imagem) {
    // Formato esperado da array $imagem
    // Array ( 
    // [name] =>  
    // [full_path] =>  
    // [type] => 
    // [tmp_name] =>  
    // [error] => 
    // [size] => )
    if ($imagem['error'] !== UPLOAD_ERR_OK) {
        return false;
    }
    if ($imagem['size'] > 5 * 1024 * 1024) {
        return false;
    }
    $info = getimagesize($imagem['tmp_name']);
    // Formato esperado de $info 
    // Array ( 
    // [0] => 667 
    // [1] => 436 
    // [2] => 3 
    // [3] => width="667" height="436" 
    // [bits] => 8 
    // [mime] => image/png )
    if (!$info) {
        return false;
    }
    $tiposPermitidos = [
        'image/jpeg',
        'image/png',
        'image/webp'
    ];
    if (!in_array($info['mime'], $tiposPermitidos)) {
        return false;
    }
    $largura = $info[0];
    $altura = $info[1];
    if ($largura > 4000 || $altura > 4000) {
        return false;
    }
    switch ($info['mime']) {
        case 'image/jpeg':
            $imagemOriginal = imagecreatefromjpeg($imagem['tmp_name']);
            break;

        case 'image/png':
            $imagemOriginal = imagecreatefrompng($imagem['tmp_name']);
            break;

        case 'image/webp':
            $imagemOriginal = imagecreatefromwebp($imagem['tmp_name']);
            break;

        default:
            return false;
    }
    if (!$imagemOriginal) {
        return false;
    }
    $limite = 1200;
    $proporcao = min(
        $limite / $largura,
        $limite / $altura,
        1
    );
    $novaLargura = (int) round($largura * $proporcao);
    $novaAltura = (int) round($altura * $proporcao);
    $imagemFinal = imagecreatetruecolor(
        $novaLargura,
        $novaAltura
    );
    $branco = imagecolorallocate($imagemFinal, 255, 255, 255);
    imagefill($imagemFinal, 0, 0, $branco);
    imagecopyresampled(
        $imagemFinal,
        $imagemOriginal,
        0, 0, 0, 0,
        $novaLargura,
        $novaAltura,
        $largura,
        $altura
    );
    ob_start();
    imagejpeg($imagemFinal, null, 75);
    $imagemComprimida = ob_get_clean();
    return $imagemComprimida;
}

function updateProduct($conecta, $id) {

    $id = filter_var($id, FILTER_VALIDATE_INT);

    if (!$id || !isset($_POST['atualizar'])) {
        return;
    }

    $nome = mysqli_real_escape_string($conecta, trim($_POST['nome']));
    $descricao = mysqli_real_escape_string($conecta, trim($_POST['descricao']));
    $preco = filter_var($_POST['preco'], FILTER_VALIDATE_FLOAT);
    $data = mysqli_real_escape_string($conecta, $_POST['data']);
    $categoriaID = filter_var($_POST['categoriaID'], FILTER_VALIDATE_INT);

    if (
        empty($nome) || empty($descricao) ||
        $preco === false ||
        $preco < 0 ||
        !$categoriaID
    ) {
        echo "Preencha os campos corretamente.";
        return;
    }

    $imagem = null;

    if (
        isset($_FILES['imagem']) &&
        $_FILES['imagem']['error'] !== UPLOAD_ERR_NO_FILE
    ) {

        $imagem = comprimirImagem($_FILES['imagem']);

        if ($imagem === false) {
            echo "Imagem inválida, muito grande ou em formato não permitido.";
            return;
        }

        $imagem = mysqli_real_escape_string($conecta, $imagem);

        $sql = "UPDATE produto SET
                nome = '$nome',
                descricao = '$descricao',
                preco = '$preco',
                data = '$data',
                categoriaID = $categoriaID,
                imagem = '$imagem'
                WHERE produtoID = $id";

    } else {

        $sql = "UPDATE produto SET
                nome = '$nome',
                descricao = '$descricao',
                preco = '$preco',
                data = '$data',
                categoriaID = $categoriaID
                WHERE produtoID = $id";
    }

    $action = mysqli_query($conecta, $sql);

    if ($action) {
        header("Location: editarProduto.php?id=$id&sucesso=1");
        exit;
    } else {
        echo "Erro ao atualizar produto: " . mysqli_error($conecta);
    }
}

?>
