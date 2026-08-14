<?php

$lanches = array("Pastel", "Pizza", "Hamburger", "HotDog", "Xis", "Churrasco");

echo "$lanches[4]";

echo "<br>";

print_r($lanches);

// Vale a partir do php 5.6
$bebidas = ["Vodka", "Fanta Uva", "Suco", "Água", "Whiskey", "Coffe"];

echo "<br>";
print_r($bebidas);

// Array Association
$aluno = [
    "nome" => "Langrage",
    "data_nasc" => "01/25/1736",
    "formulas" => ["normal", "expandida", "ultra expandida"]
];

echo "<br>";

print_r($aluno);
echo "<br>";
echo "<h2>$aluno[nome], nasceu em $aluno[data_nasc]. Fórmula " . $aluno["formulas"][2] . ".</h2>";

// array multidimensional (formato usual dos dados recebidos pelo banco de dados)
$funcionarios = [
    [
        "nome" => "Marcelo",
        "setor" => "Diretoria",
        "email" => "###@gmai.com"
    ],
    [
        "nome" => "jéssica",
        "setor" => "Administrativo",
        "email" => "###@gmai.com"
    ],
    [
        "nome" => "Giovane",
        "setor" => "Existe",
        "email" => "###@gmai.com"
    ],
    [
        "nome" => "Guilherme",
        "setor" => "Existe",
        "email" => "###@gmai.com"
    ]
];

echo "<br>";

// Comandos de repetição (looping)
// Indice = de onde começa a repetição.
// Teste lógico = Lógica para terminar ou continuar o loop.
// Incremento = É o que ocorre com o índice a cada repetição.

echo "<br>";
for ($i = 0; $i < 10; $i = $i + 1 ){
    echo $i;
}
echo "<br>";
for ($i = 0; $i <= 100; $i += 5 ){
    echo "$i - ";
}

echo "<br>";

$contar = count($bebidas);
for ($i = 0; $i < $contar; $i++){
    echo $bebidas[$i] . "<br>";
};

?>