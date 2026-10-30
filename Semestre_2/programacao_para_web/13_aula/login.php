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