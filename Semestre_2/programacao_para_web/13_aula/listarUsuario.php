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
    <title>Lista de usuários</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>User ID</th>
                <th>Nome</th>
                <th>E-mail</th>
                <th>Data cadastro</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <?php
                $usuarios = listarUsuarios($conecta);
                // print_r($usuarios);
                foreach ($usuarios as $usuario) : ?>
                <tr>
                    <td><?php echo $usuario["usuarioID"]?></td>
                    <td><?php echo $usuario["nome"];?></td>
                    <td><?php echo $usuario["email"];?></td>
                    <td>
                        <?php
                            $data = date_create($usuario["data"]);
                            echo date_format($data, "d/m/Y");
                        ?>
                    </td>
                    <td>
                        <a style="text-decoration: none; color: red;"
                                href="deletar.php?id=<?php echo $usuario['usuarioID']; ?>&nome=<?php echo $usuario['nome']; ?>">
                                Excluir
                            </a>
                            <span style="color: black; padding: 0 4px 0 4px;">|</span>
                            <a style="text-decoration: none; color: orange;"
                                href="editar.php?id=<?php echo $usuario['usuarioID']; ?>">
                                Editar
                            </a>
                    </td>
                </tr>

            <?php endforeach ?>
        </tbody>
    </table>

</body>
</html>