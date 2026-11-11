<?php
require_once "functions.php";
session_start();

if (!isset($_SESSION['ativa']) || $_SESSION['ativa'] !== true) {
    header("Location: catalogo.php");
    exit;
}

$id = $_GET['id'] ?? null;

$produto = buscarProdutoByID($conecta, $id);

if (!$produto) {
    echo "Produto não encontrado.";
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    updateProduct($conecta, $id);
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Produto</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <?php if (isset($_GET['sucesso'])): ?>
            <div class="alert alert-success">
                Produto atualizado com sucesso!
            </div>
        <?php endif; ?>
        <h1 class="mb-4">Editando o Produto: <?php echo htmlspecialchars($produto['nome']); ?></h1>

        <form method="POST" enctype="multipart/form-data">
            <input type="hidden" name="id" value="<?php echo $produto['produtoID']; ?>">
            <div class="mb-3">
                <label for="imagem" class="form-label">Imagem do Produto</label>
                <input type="file" name="imagem" class="form-control" id="imagem" accept="image/jpeg, image/png, image/webp">
                <div class="mt-3">
                    <img src="<?php echo htmlspecialchars($produto['imagem']); ?>" alt="Imagem do produto" style="max-width: 200px; max-height: 200px;">
                </div>
            </div>
            <div class="mb-3">
                <label for="nome" class="form-label">Nome</label>

                <input type="text" name="nome" value="<?php echo htmlspecialchars($produto['nome']); ?>"
                    class="form-control" id="nome" required>
            </div>
            <div class="mb-3">
                <label for="descricao" class="form-label">Descrição</label>

                <textarea name="descricao" class="form-control" id="descricao" rows="3"
                    required><?php echo htmlspecialchars($produto['descricao']); ?></textarea>
            </div>
            <div class="mb-3">
                <label for="preco" class="form-label">Preço</label>
                <input type="number" name="preco" step="0.01" class="form-control" id="preco" value="<?php echo $produto['preco']; ?>" required>
            </div>

            <div class="mb-3">
                <label for="data" class="form-label">Data de Cadastro</label>
                <input type="date" name="data" class="form-control" id="data" value="<?php echo $produto['data']; ?>" required>
            </div>

            <div class="mb-3">
                <label for="categoriaID" class="form-label">Categoria</label>

                <select name="categoriaID" id="categoriaID" class="form-select" required>
                    <?php
                    $categorias = buscarCategorias($conecta);
                    foreach ($categorias as $categoria):
                        $selected = (
                            $categoria['categoriaID'] == $produto['categoriaID']
                        ) ? "selected" : "";
                        ?>
                        <option value="<?php echo $categoria['categoriaID']; ?>" <?php echo $selected; ?>> 
                            <?php echo htmlspecialchars($categoria['nome']); ?>
                        </option>

                    <?php endforeach; ?>
                </select>
            </div>
            <button type="submit" name="atualizar" class="btn btn-primary">
                Atualizar
            </button>
        </form>
    </div>
</body>
</html>