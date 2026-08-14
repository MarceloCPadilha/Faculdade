<?php

$aluno = "Ronaldo"; // String
$idade = "50"; // int
$altura = 2.11; // float
$matriculado = True; // true - false (boolean)

echo 'Olá $aluno, bem vindo as aulas de PHP!<br>';
echo "Olá $aluno, bem vindo as aulas de PHP!<br>";

// como o php é uma linguagem fracamente tipada, se tu somar uma String e um float ele assume que o tipo é float
$x = "20";
$y = 5.3;
$soma = $x + $y;
echo "o valor é $soma e o tipo é ", var_dump($soma);

// concatenar (juntar strings)
$nome = "Ronaldo ";
$nome .= "Gaúcho";
echo "<h2>$nome</h2>";

// constantes
define("CURSO", "Programação em PHP");
echo CURSO;
// Não permite mudar o valor,
// define("CURSO", "HTML e CSS);

// Versão moderna de declarar constantes
const TESTE = "Novo     ";
echo "<br>" . TESTE;

?>