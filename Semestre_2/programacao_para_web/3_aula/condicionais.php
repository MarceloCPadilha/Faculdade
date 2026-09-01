<?php

$idade = 19;
// comandos condicionais
if ($idade >= 18) {
    echo "<p>Maior de idade!</p>";
} else if ($idade < 0) {
    echo "<p>Digite uma idade válida!</p>";
} else {
    echo "<p>Menor de idade!</p>";
}

$aluno = "Guilherme";

// OU: or - ||(barras retas, mas como é comentário fica em itálico)
if ($aluno == "Guilherme" or $aluno == "Giovane" || $aluno == "Marcelo") {
    echo "<p>Passar na coordenação.</p>";
} else {
    echo "<p>Entrada autorizada!</p>";
}

$login = "admin";

// E: and - &
$senha = 123486134; // senha númerica (Obrigatório ser um INT)
if ($login == "admin" and $senha === 123486134 /* === verifica o valor e o tipo */) {
    echo "<h2>Bem vindo ao sistema!</h2>";
} else {
    echo "<h2>Usuário ou sena inválidos.</h2>";
}

$nota1 = 5;
$nota2 = 8;
$nota3 = 10;
$media = ($nota1 + $nota2 + $nota3) / 3;
if ($media < 0 or $media > 10) {
    echo "<p>O aluno está APROVADO com média $media.</p>";
} else if ($media >= 7) {
    echo "<p>Média invalida: $media</p>";
} else {
    echo "<p>O aluno está REPROVADO com média $media.</p>";
}

?>