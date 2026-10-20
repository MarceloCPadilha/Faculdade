<?php
require_once "functions.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Usuários</title>
</head>
<body>

    <?php
        $id = $_GET['id'];
        $usuario = buscaID($conecta, $id);
    ?>
    <h1>
        Editando o usuário <?php echo $usuario["nome"]; ?>
    </h1>

    <form method="post">
        <input type="hidden" name="id" value="<?php echo $usuario["id"]; ?>" required>
        <input type="hidden" name="nome" value="<?php echo $usuario["nome"]; ?>" required>
        <input type="hidden" name="email" value="<?php echo $usuario["email"]; ?>" required>
        <input type="hidden" name="senha" value="<?php echo $usuario["senha"]; ?>" placeholder="******">
        <input type="hidden" name="data" value="<?php echo $usuario["data"]; ?>" required>
        <button name="atualizar">Atulaizar</button>
    </form>

    <?php updateUser($conecta, $id);?>
    
</body>
</html>