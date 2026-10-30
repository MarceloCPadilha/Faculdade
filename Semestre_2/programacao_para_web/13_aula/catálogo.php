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

<body>

    <div class="container mx-5 mt-5">
        <a class="btn btn-danger" href="logout.php">LOGOUT</a>
    </div>
    <?php
    $dado = dadosProduto($conecta);
    ?>
    <div class="container mx-auto">
        <div class="row row-cols-1 row-cols-md-3 row-cols-lg-4 g-4 mx-5 mt-4">
        <?php foreach($dado as $dados) :?>
            <div class="col">
                <div class="card h-100">
                    <img src="produtoplaceholder.png" class="card-img-top img-fluid" alt="...">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title"><?php echo $dados["nome"];?></h5>
                        <p class="card-text">Descrição: <?php echo $dados["descricao"]?></p>
                        <p class="mb-1">Categoria: <?php echo $dados["categoria"]?></p>
                        <p class="fw-bold text-success">Preço: R$ <?php echo $dados["preco"]?></p>
                        
                        <div class="d-flex gap-2 mt-auto">
                            <button class="btn btn-primary flex-grow-1" type="button">Adicionar</button>
                            
                            <div class="input-group" style="width: 105px; flex-shrink: 0;">
                                <button class="btn btn-outline-secondary px-2 btn-menos" type="button">-</button>
                                <input type="number" class="form-control text-center px-1 qtd-input" value="1" min="1" max="99" readonly>
                                <button class="btn btn-outline-secondary px-2 btn-mais" type="button">+</button>
                            </div>
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
