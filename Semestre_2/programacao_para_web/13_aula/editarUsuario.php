<?php
require_once "functions.php";
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
        $usuario = buscaID($conecta, $id);
    ?>
    <h1>
        Editando o usuário <?php echo $usuario["nome"]; ?>
    </h1>

<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    
    <form method="mb-3">
        <div class="mb-3">
            <input type="hidden" name="id" value="<?php echo $usuario["id"]; ?>" required>
        </div>
        <div class="mb-3">
            <input type="text" name="nome" value="<?php echo $usuario["nome"]; ?>" required>
        </div>
        <div class="mb-3">
            <input type="email" name="email" value="<?php echo $usuario["email"]; ?>" required>
        </div>
        <div class="mb-3">
            <input type="password" name="senha" placeholder="******">
        </div>
        <div class="mb-3">
            <input type="date" name="data" value="<?php echo $usuario["data"]; ?>" required>
        </div>    
        <button name="atualizar">Atualizar</button>
    
    </form>

    <?php updateUser($conecta, $id);?>
    
</body>
</html>