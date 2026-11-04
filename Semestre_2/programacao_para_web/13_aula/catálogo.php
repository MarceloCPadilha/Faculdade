<?php
require_once("functions.php");

$categorias = getCategorias($conecta);
$filtro = $_GET['categorias'] ?? [];
$dado = dadosProduto($conecta, $filtro);
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
    * {
        padding: 0;
    }

    /* 
    Remove o "step" nos inputs do tipo numero com a classe .qtd-input
    As stpes são as flechas pra cima e pra baixo que aumentam ou diminuem
    o número dentro do input
    botões desnecessários já que eu crieo novos
    */
    .qtd-input::-webkit-outer-spin-button,
    .qtd-input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
    }

    /* Firefox */
    .qtd-input[type=number] {
    -moz-appearance: textfield;
    }
</style>
<body>

    <div class="mx-5 mt-4 d-flex justify-content-center">
    <div class="d-inline-flex gap-2 align-middle">
        <a class="btn btn-success" href="login.php">LOGIN</a>
        <a class="btn btn-danger" href="logout.php">LOGOUT</a>
    </div>
</div>
    <div class="container-fluid row px-5">

        <div class="col-md-3">
            <div class="mt-5 ms-5">
                <form method="get">
                <?php foreach($categorias as $categoria) : ?>
                <div class="mb-1">
                    <input type="checkbox" name="categorias[]" id="categoria_<?php echo $categoria['categoriaID']; ?>" value="<?php echo $categoria['categoriaID']; ?>" <?php if (in_array($categoria['categoriaID'], array_map('intval', $filtro))) {echo 'checked';}?>>
                    <label for="categoria_<?php echo $categoria['categoriaID']; ?>">
                        <?php echo htmlspecialchars($categoria['nome']); ?>
                    </label>
                </div>
                <?php endforeach;?>
                <button class="btn btn-primary" type="submit">
                    Aplicar Filtro
                </button>
                </form>
            </div>
        </div>
        <div class="row col-md-9 g-4 m-0">
            <?php foreach($dado as $dados) : ?>
            <div class="col-md-3 mt-4">
                <div class="card h-100">
                    <img src="produtoplaceholder.png" class="card-img-top img-fluid" alt="...">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title"><?php echo $dados["nome"];?></h5>
                        <p class="card-text">Descrição: <?php echo $dados["descricao"]?></p>
                        <p class="mb-1">Categoria: <?php echo $dados["categoria"]?></p>
                        <p class="fw-bold text-success">Preço: R$ <?php echo $dados["preco"]?></p>
                        
                        <div class="d-flex gap-2 mt-1">
                            <div class="input-group" style="width: 75px; flex-shrink: 0;">
                                <button class="btn btn-outline-secondary px-2 btn-menos" type="button">-</button>
                                <input type="number" class="form-control text-center px-1 qtd-input" value="1" min="1" max="99" max-lenght="2" min-lenght="1">
                                <button class="btn btn-outline-secondary px-2 btn-mais" type="button">+</button>
                            </div>
                            <button class="btn btn-primary flex-grow-1" type="button">Adicionar</button>
                            
                        </div>
                    </div>
                </div>
            </div>
            <?php endforeach ?>
        </div>
    </div>

    <script>
        document.querySelectorAll('.card').forEach(card => {
            const btnMenos = card.querySelector('.btn-menos');
            const btnMais = card.querySelector('.btn-mais');
            const inputQtd = card.querySelector('.qtd-input');

            if (btnMenos && btnMais && inputQtd) {
                btnMenos.addEventListener('click', () => {
                    let atual = parseInt(inputQtd.value) || 1;
                    let min = parseInt(inputQtd.min) || 1;
                    if (atual > min) {
                        inputQtd.value = atual - 1;
                    }
                });

                btnMais.addEventListener('click', () => {
                    let atual = parseInt(inputQtd.value) || 1;
                    let max = parseInt(inputQtd.max) || 99;
                    if (atual < max) {
                        inputQtd.value = atual + 1;
                    }
                });
            }
        });
    </script>
</body>

</html>
