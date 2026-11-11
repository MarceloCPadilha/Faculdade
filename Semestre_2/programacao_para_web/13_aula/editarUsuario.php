<?php
require_once "functions.php";
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
    <title>Editar Usuários</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>

    <div class="container mt-5">
        <?php
        $id = $_GET['id'];
        $usuario = buscarUsuarioByID($conecta, $id);
        ?>
        <h1>
            Editando o usuário <?php echo $usuario["nome"]; ?>
        </h1>
        <form method="POST">
            <input type="hidden" name="id" value="<?php echo $usuario["usuarioID"]; ?>">
            <div class="mb-3">
                <label for="nome" class="form-label">Nome</label>
                <input type="text" name="nome" value="<?php echo htmlspecialchars($usuario["nome"]); ?>" class="form-control" id="nome" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" name="email" value="<?php echo htmlspecialchars($usuario["email"]); ?>" class="form-control" id="email" required>
            </div>
            <div class="mb-3">
                <label for="senha" class="form-label">Password</label>
                <input type="password" name="senha" class="form-control" id="senha" placeholder="Deixe vazio para manter a senha atual">
            </div>
            <div class="mb-3">
                <label for="data" class="form-label">Data</label>
                <input type="date" name="data" class="form-control" id="data" value="<?php echo $usuario["data"]; ?>" required>
            </div>
            <button type="submit" name="atualizar" class="btn btn-primary">Atualizar</button>
        </form>
    </div>


    <?php updateUser($conecta, $id); ?>
</body>

</html>