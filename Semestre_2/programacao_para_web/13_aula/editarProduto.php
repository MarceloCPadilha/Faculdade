<?php
require_once "functions.php";
session_start();
// Se a sessão não estiver ativa, redireciona imediatamente
if (!isset($_SESSION['ativa'])) {
    header("location: index.php");
    exit; // Importante para parar a execução do script
}
?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Produto</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>

    <div class="container mt-5">
        <?php
        $id = $_GET['id'];
        $produto = buscarProdutoByID($conecta, $id);
        
        if (!$produto) {
            echo "<div class='alert alert-danger'>Produto não encontrado.</div>";
            exit;
        }
        ?>
        
        <h1 class="mb-4">
            Editando o Produto: <?php echo htmlspecialchars($produto["nome"]); ?>
        </h1>
        <form method="POST">
            <input type="hidden" name="id" value="<?php echo $produto["produtoID"]; ?>">
            
            <div class="mb-3">
                <label for="imagem" class="form-label">Upload de Imagem (Substituir Atual)</label>
                <input type="file" name="imagem" class="form-control" id="imagem" accept="image/*">
                
                <?php if (!empty($produto["imagem"]) && $produto["imagem"] !== 'sem-foto.jpg'): ?>
                    <div class="mt-2">
                        <span class="badge bg-secondary">Já existe uma imagem salva</span>
                    </div>
                <?php endif; ?>
            </div>

            <div class="mb-3">
                <label for="nome" class="form-label">Nome</label>
                <input type="text" name="nome" value="<?php echo htmlspecialchars($produto["nome"]); ?>" class="form-control" id="nome" required>
            </div>

            <div class="mb-3">
                <label for="descricao" class="form-label">Descrição</label>
                <textarea name="descricao" class="form-control" id="descricao" rows="3" required><?php echo htmlspecialchars($produto["descricao"]); ?></textarea>
            </div>

            <div class="mb-3">
                <label for="preco" class="form-label">Preço</label>
                <input type="number" name="preco" step="0.01" class="form-control" id="preco" value="<?php echo $produto["preco"]; ?>" placeholder="R$">
            </div>

            <div class="mb-3">
                <label for="data" class="form-label">Data de Cadastro</label>
                <input type="date" name="data" class="form-control" id="data" value="<?php echo $produto["data"]; ?>" required>
            </div>
            
            <div class="mb-3">
                <label for="categoriaID" class="form-label">Categoria</label>
                <select name="categoriaID" id="categoriaID" class="form-select">
                    <?php
                    $categorias = buscarCategorias($conecta);
                    foreach($categorias as $categoria) : 
                        $selected = ($categoria["categoriaID"] == $produto["categoriaID"]) ? "selected" : "";
                    ?>
                        <option value="<?php echo $categoria["categoriaID"];?>" <?php echo $selected;?>>
                            <?php echo htmlspecialchars($categoria["nome"]); ?>
                        </option>
                    <?php endforeach; ?>
                </select>    
            </div>

            <button type="submit" name="atualizar" class="btn btn-primary">Atualizar</button>
        </form>

        <?php updateUser($conecta, $id); ?>
    </div>
</body>

</html>
