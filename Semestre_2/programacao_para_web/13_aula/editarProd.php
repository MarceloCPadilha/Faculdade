<?php
require_once("functions.php");
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

    <?php $dados = DadosProduto($conecta);?>

    <div class="container mt-4">
        <table border="1" class="table"><?php

require_once("functions.php");

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

<style>
    body {
        height: 100vh;
    }
</style>

<body>

    <div class="d-flex justify-content-center align-items-center mt-5">
        <form method="post" class="border p-4 rounded shadow-sm bg-body-tertiary">
            <div class="aviso">
                <?php login($conecta);?>
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email</label>
                <input name="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" required>
                <div id="emailHelp" class="form-text">Compartilharemos seu e-mail com qualquer um que pagar o suficiente. <span style="opacity: 0.1;">50 centavos?</span></div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Senha</label>
                <input name="senha" type="password" class="form-control" id="exampleInputPassword1" required>
            </div>
            <button name="logar" class="btn btn-primary">Logar</button>
        </form>
    </div>

</body>

</html>
            <thead class="table-light">
                <tr>
                    <th>Produto ID</th>
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
                    foreach ($dados as $dado) : ?>
                    <tr>
                        <td><?php echo $dado["produtoID"];?></td>
                        <td><?php echo $dado["nome"];?></td>
                        <td><?php echo $dado["preco"];?></td>
                        <td><?php echo $dado["descricao"];?></td>
                        <td>
                            <?php
                                $data = date_create($dado["data"]);
                                echo date_format($data, "d/m/Y");
                            ?>
                        </td>
                        <td><?php echo $dado["categoriaID"];?></td>
                        <td><?php echo $dado["categoria"];?></td>
                        <td>
                            <a style="text-decoration: none; color: red;" href="deletar.php?id=<?php echo $dado['produtoID'];?>&nome=<?php echo $dado['nome'];?>">
                                Excluir
                            </a>
                            <span style="color: black; padding: 0 4px 0 4px;">|</span>
                            <a style="text-decoration: none; color: orange;" href="editar.php?id=<?php echo $dado['produtoID'];?>">
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