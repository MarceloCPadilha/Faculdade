<?php

session_start();

// Limpar os caches da sessão
session_unset();

// Encerra a session(desloga)
session_destroy();

header("location: index.php");

?>