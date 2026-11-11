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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>

    <?php $dados = listarProdutos($conecta); ?>

    <div class="container mt-4">
        <table border="1" class="table">

            <thead class="table-light">
                <tr>
                    <th>Produto ID</th>
                    <th>Imagem</th>
                    <th>Nome</th>
                    <th>Preço</th>
                    <th>Descrição</th>
                    <th>Data</th>
                    <th>Categoria ID</th>
                    <th>Categoria</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <?php
                foreach ($dados as $dado): ?>
                    <tr>
                        <td><?php echo $dado["produtoID"]; ?></td>
                        <td><img src="<?php echo $dado['imagem']; ?>" alt="Imagem do produto" style="max-width: 150px; max-height: 150px;"></td>
                        <td><?php echo $dado["nome"]; ?></td>
                        <td><?php echo $dado["preco"]; ?></td>
                        <td><?php echo $dado["descricao"]; ?></td>
                        <td>
                            <?php
                            $data = date_create($dado["data"]);
                            echo date_format($data, "d/m/Y");
                            ?>
                        </td>
                        <td><?php echo $dado["categoriaID"]; ?></td>
                        <td><?php echo $dado["categoria"]; ?></td>
                        <td>
                            <a style="text-decoration: none; color: red;"
                                href="deletar.php?tipo=produto&id=<?php echo $dado['produtoID']; ?>&nome=<?php echo urlencode($dado['nome']); ?>">
                                Excluir
                            </a>
                            <span style="color: black; padding: 0 4px 0 4px;">|</span>
                            <a style="text-decoration: none; color: orange;"
                                href="editarProduto.php?id=<?php echo $dado['produtoID']; ?>">
                                Editar
                            </a>
                        </td>
                    </tr>

                <?php endforeach ?>
            </tbody>
        </table>
    </div>

</body>

</html>