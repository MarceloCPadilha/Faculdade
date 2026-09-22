<?php

$alunos = [
    [
        "nome" => "Guilherme",
        "Curso" => "ADS",
        "Nota" => 10
    ],
    [
        "nome" => "Giovane",
        "Curso" => "ADS",
        "Nota" => 10
    ],
    [
        "nome" => "Marcelo",
        "Curso" => "ADS",
        "Nota" => 10
    ],
    [
        "nome" => "Aluno_4",
        "Curso" => "ADS",
        "Nota" => 9
    ],
    [
        "nome" => "Aluno_5",
        "Curso" => "ADS",
        "Nota" => 8
    ],
];

foreach ($alunos as $aluno) {
    echo "O aluno " . $aluno['nome'] . " do curso " . $aluno['Curso'] . " tirou nota " . $aluno['Nota'] . ".<br>\n";
};

?>