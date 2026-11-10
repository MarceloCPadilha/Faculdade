<?php

require_once("./functions.php");
session_start();
isset($_SESSION['ativa']) ? '' : header("location: login.php");


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../../bootstrap-5.3.8-dist/css/bootstrap.min.css">
    <script src="../../../bootstrap-5.3.8-dist/js/bootstrap.min.js"></script>
</head>
<body class="flex justify-content-center align-itens-center">

    <div class="flex ">
        <a class="btn btn-success" href="listarProduto.php">Editar Produtos</a>
        <a class="btn btn-success" href="listarUsuario.php">Editar Usuários</a>
        <a class="btn btn-danger" href="./logout.php">LOGOUT</a>
    </div>

</body>
</html>