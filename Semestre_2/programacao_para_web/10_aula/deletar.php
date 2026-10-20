<?php
require_once "functions.php";
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        if (isset($_GET['id']) and !empty($_GET['nome'])) :
        $id = $_GET['id'];
    ?>
    <h1>
        Tem certeza que deseja excluir o usuário 
        <?php echo $_GET['nome']?>?
    </h1>
    <form action="post">
        <input type="hidden" name="id" id="<?php echo $id ?>">
        <button name="excluir">Deletar Usuário</button>
    </form>
    
    <?php
        if(isset($_POST['excluir'])) {
            $id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
            delete($conecta, $id);
        }
    ?>
    
    <?php endif ?>
</body>
</html>