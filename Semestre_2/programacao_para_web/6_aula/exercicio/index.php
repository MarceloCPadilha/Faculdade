<!-- 
Crie um sistema para calcular a quantidade de BTUs necessária para cada ambiente de acordo com os Metros quadrados e se o ambiente é residencial ou comercial.

Segue em anexo imagem com uma tabela de BTUs necessária para fazer o exercícios.
No frontend será necessário um campo para inserir a largura e outro para inserir o comprimeto do ambiente em metros. E mais um campo para o usuário selecionar se o ar condicionado é para ambiente residencial ou comercial.
No Backend é necessário criar uma lógica para, seguindo a TABELA EM ANEXO, mostrar os m² e a quantidade de BTUs necessária para o ambiente.

Exibir na tela após o envio do formulário a seguinte frase:
Para seu ambiente de XXm² é necessário um ar condicionado de XX BTUs. 
-->

<?php

$mensagem = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $area = filter_input(INPUT_POST, "area", FILTER_VALIDATE_FLOAT);
    $tipo_ambiente = filter_input(INPUT_POST, "tipo", FILTER_SANITIZE_FULL_SPECIAL_CHARS);

    if ($area && $tipo_ambiente) {
        $array_ambiente = [
            9  => ["residencial" => 7000,  "comercial" => 7000],
            12 => ["residencial" => 7000,  "comercial" => 9000],
            15 => ["residencial" => 9000,  "comercial" => 12000],
            20 => ["residencial" => 12000, "comercial" => 16000],
            25 => ["residencial" => 15000, "comercial" => 20000],
            30 => ["residencial" => 18000, "comercial" => 24000],
            35 => ["residencial" => 21000, "comercial" => 28000],
            40 => ["residencial" => 24000, "comercial" => 32000],
            45 => ["residencial" => 27000, "comercial" => 36000],
            50 => ["residencial" => 30000, "comercial" => 40000],
            60 => ["residencial" => 36000, "comercial" => 48000],
            70 => ["residencial" => 42000, "comercial" => 56000]
        ];

        $area_referencia = 70;
        foreach ($array_ambiente as $metragem => $btus) {
            if ($area <= $metragem) {
                $area_referencia = $metragem;
                break;
            }
        }

        $btu = $array_ambiente[$area_referencia][$tipo_ambiente];

        $mensagem = "Para seu ambiente de {$area}m² é necessário um ar condicionado de {$btu} BTUs.";
    } else {
        $mensagem = "Por favor, informe uma área válida e selecione o tipo de ambiente.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <form method="post">
        <label for="area">Área:</label>
        <input type="number" name="area" id="area">
        <br>
        <select name="tipo" id="tipo">
            <option value="" selected disabled>Selecionar tipo de ambiente</option>
            <option value="residencial">Residencial</option>
            <option value="comercial">Comercial</option>
        </select>
        <br>
        <button>Calcular</button>
    </form>

    <?php
    
    echo($mensagem);
    
    ?>
    
</body>
</html>