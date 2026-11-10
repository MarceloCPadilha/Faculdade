<?php
require_once "functions.php";
session_start();
isset($_SESSION['ativa']) ? '' : header("location: index.php");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Usuários</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>

    <?php
    $id = $_GET['id'];
    $usuario = buscarUsuarioByID($conecta, $id);
    ?>
    <h1>
        Editando o usuário <?php echo $usuario["nome"]; ?>
    </h1>

    <form>
        <div class="mb-3">
            <input type="hidden" name="id" class="form-control" id="exampleInputEmail1" value="<?php echo $usuario["usuarioID"]; ?>" aria-describedby="emailHelp" required >
        </div>
        <div class="mb-3">
            <label for="nome" class="form-label">Nome</label>
            <input type="email" name="nome" value="<?php echo $usuario["nome"]; ?>" class="form-control" id="nome" required>
        </div>
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" name="nome" class="form-control" id="exampleInputEmail1"required>
        </div>
        <div class="mb-3">
            <label for="senha" class="form-label">Password</label>
            <input type="password" name="senha" class="form-control" id="senha" placeholder="*****">
        </div>
        <div class="mb-3">
            <label for="data" class="form-label">data</label>
            <input type="date" name="data" class="form-control" id="senha" value="<?php echo $usuario["data"]?>" required>
        </div>
        <button type="submit" name="atualizar" class="btn btn-primary">Atualizar</button>
    </form>

    <?php updateUser($conecta, $id); ?>
</body>

</html>