<?php

$senha = "teste";
$cripto = base64_encode($senha);

echo $senha;
echo "<hr>";
echo "base64: ", $cripto;
echo "<hr>";
echo "base64_decode: ", base64_decode($cripto);
echo "<hr>";
echo md5($senha);
echo "<hr>";
echo sha1($senha);
echo "<hr>";
// segundo parametro PASSWORD_DEFAULT
echo password_hash($senha, PASSWORD_ARGON2ID);
// PASSWORD_ARGON2ID, é o mais seguro, mas só funciona quando o php tem suporte para Argon2



?>