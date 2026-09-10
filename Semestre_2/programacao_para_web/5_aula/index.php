<?php



?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurante - Ratão</title>
    <link rel="stylesheet" href="./style/style.css">
</head>
<body>
    
    <?php
    include "./layout/topo.php"
    ?>
    <section class="banner">
        <div class="infos">
            <h2>Conheça nossas</h2>
            <h1>Receitas Especiais</h1>
            <p>Venha conhecer nossos pratos com receitas exclusivas direto da
                ilha das cabras e dos gatos localizados na Malásia.
            </p>
        </div>
        <div class="imagem"></div>
    </section>
    <section class="sobre">
        <div class="infos">
            <h2>Conheça nossa história</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui non iure nemo aspernatur distinctio molestias nam dolore, perferendis excepturi quae tenetur exercitationem delectus.</p>
        </div>
        <div class="imagem">
            <img src="../img/prato.jpg" alt="">
        </div>
    </section>
    <section class="pratos">
        <div class="container">
            <div class="coluna">
                <div class="imagem">
                    <img src="../img/prato.jpg" alt="">
                </div>
                <h3>Receita um</h3>
            </div>
            <div class="coluna">
                <div class="imagem">
                    <img src="../img/prato.jpg" alt="">
                </div>
                <h3>Receita dois</h3>
            </div>
            <div class="coluna">
                <div class="imagem">
                    <img src="../img/prato.jpg" alt="">
                </div>
                <h3>Receita três</h3>
            </div>
            <div class="coluna">
                <div class="imagem">
                    <img src="../img/prato.jpg" alt="">
                </div>
                <h3>Receita quatro</h3>
            </div>
        </div>
    </section>
    <footer class="rodape">
        <?php
            include "./layout/menu.php"
        ?>
        <p>todos os direitos reservados - 2026</p>
    </footer>

</body>
</html>