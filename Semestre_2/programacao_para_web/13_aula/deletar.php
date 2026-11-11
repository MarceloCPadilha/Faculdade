
<?php
require_once "functions.php";
session_start();

if (!isset($_SESSION['ativa']) || $_SESSION['ativa'] !== true) {
    header("Location: catalogo.php");
    exit;
}

$tipo = $_GET['tipo'] ?? '';
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
$nome = $_GET['nome'] ?? '';

if (!in_array($tipo, ['usuario', 'produto']) || !$id || empty($nome)) {
    echo "Dados inválidos.";
    exit;
}

if (isset($_POST['excluir'])) {
    $id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
    $tipo = $_POST['tipo'] ?? '';
    if ($tipo === 'usuario') {
        deleteUser($conecta, $id);
    } elseif ($tipo === 'produto') {
        deleteProduct($conecta, $id);
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmar Exclusão</title>
</head>
<body>
    <h1>
        Tem certeza que deseja excluir
        <?php echo $tipo === 'usuario' ? 'o usuário' : 'o produto'; ?>
        <?php echo htmlspecialchars($nome); ?>?
    </h1>
    <form method="POST">
        <input type="hidden" name="id" value="<?php echo $id; ?>">
        <input type="hidden" name="tipo" value="<?php echo htmlspecialchars($tipo); ?>">
        <button type="submit" name="excluir">
            Deletar <?php echo $tipo === 'usuario' ? 'Usuário' : 'Produto'; ?>
        </button>
    </form>
</body>
</html>
