<?php

session_start();

session_unset();

session_destroy();

echo "Logout realizado com sucesso!";

header("Refresh: 3; url=index.php");

?>