<?php
require_once "functions.php";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de usuários</title>
</head>
<body>

    <h1>Lista de Usuários</h1>

    <form action="POST">
        <input type="text" name="nome" placeholder="Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <input type="password" name="senha" placeholder="Crie uma senha" required>
        <input type="submit" name="cadastrar" value="cadastrar" >
    </form>

    <table border="1">
        <thead>
            <tr>
                <th>Nome</th>
                <th>E-mail</th>
                <th>Data cadastro</th>
            </tr>
        </thead>
        <tbody>
            <?php
                $usuarios = buscar($conecta);
                // print_r($usuarios);
                foreach ($usuarios as $usuario) : ?>
                <tr>
                    <td><?php echo $usuario["nome"];?></td>
                    <td><?php echo $usuario["email"];?></td>
                    <td>
                        <?php
                            $data = date_create($usuario["data"]);
                            echo date_format($data, "d/m/Y")
                        ?>
                    </td>
                </tr>

            <?php endforeach ?>
        </tbody>
    </table>

</body>
</html>