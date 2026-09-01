<?php

// Comandos de repetição (looping)
//  - Indice = de onde começa a repetição.
//  - Teste lógico = Lógica para terminar ou continuar o loop.
//  - Incremento = É o que ocorre com o índice a cada repetição.

$i = 0;
$filmes = ["Missão impossivel", "Top Gun"];
while($i <= sizeof($filmes) - 1) {
    // $n = $i + 1;
    echo "<h2>" . $i + 1 . " - $filmes[$i]</h2>";
    // $i++;
    // $i = $i + 1;
    $i += 1;
};
echo "<hr>";

foreach ($filmes as $key => $filme) {
    echo "<h2>" . $key + 1 . " - $filme</h2>";
};

$alunos = [
    [
        "nome"      => "raimundo",
        "matricula" => 12345,
        "idade"     => 20
    ],
    [
        "nome"      => "Greg",
        "matricula" => 23456,
        "idade"     => 22
    ]
];
foreach($alunos as $aluno) {
    echo "<br>";
    foreach($aluno as $atributo) {
        echo "$atributo<br>";
    };
};

?>