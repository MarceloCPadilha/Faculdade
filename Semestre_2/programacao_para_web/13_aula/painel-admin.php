<?php

require_once("./functions.php");
session_start();
if (!isset($_SESSION['ativa']) || $_SESSION['ativa'] !== true) {
    header("Location: catalogo.php");
    exit;
}

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
<body class="d-flex justify-content-center align-items-center vh-100"> 

    <div class="d-flex flex-column gap-3 p-4 bg-secondary-subtle border border-secondary rounded shadow-sm" style="min-width: 300px;"> 
        <a class="btn btn-success w-100" href="listarProdutos.php">Editar Produtos</a> 
        <a class="btn btn-success w-100" href="listarUsuarios.php">Editar Usuários</a> 
        <a class="btn btn-danger w-100 mt-2" href="./logout.php">LOGOUT</a> 
    </div> 

</body> 
</html>