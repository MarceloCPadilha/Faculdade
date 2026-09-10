<?php
// Cenário: Você está escrevendo um script para monitorar o tempo de resposta (latência em milissegundos) de um link WAN importante. 
// O script recebe o valor do ping e deve imprimir um alerta no painel dependendo da gravidade.

// Crie um arquivo em PHP, crie uma variável com a latência e faça a seguinte condição:

// Se a latência for 0, o script deve exibir: "CRÍTICO: Equipamento Inacessível (Time Out)"
// Se a latência for menor ou igual a 50ms, exibir: "OK: Conexão Excelente"
// Se a latência for maior que 50ms e menor ou igual a 150ms, exibir:
// "WARNING: Conexão Aceitável, mas requer atenção"
// Se a latência for maior que 150ms, exibir: "ERRO: Latência Alta! Verifique o link." 

$ms = 50;

$retorno = match (true) {
     $ms == 0 => "CRÍTICO: Equipamento Inacessível (Time Out)",
     $ms <= 50 => "OK: Conexão Excelente",
     $ms <= 150 => "WARNING: Conexão Aceitável, mas requer atenção",
     default => "ERRO: Latência Alta! Verifique o link."
};

echo $retorno;

?>