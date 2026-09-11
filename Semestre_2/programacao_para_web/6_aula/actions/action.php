<?php
    // No PHP  os dados
    //os dados enviados via
    //print_r($_POST);
    if ( isset($_POST['enviar']) ) {
        //print_r($_POST);
        $erros=[];
        $nome = filter_input(INPUT_POST,'nome', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $email = filter_input(INPUT_POST,'email', FILTER_VALIDATE_EMAIL);
        //$idade = filter_input(INPUT_POST,'idade', FILTER_SANITIZE_NUMBER_INT);
        $idade = filter_input(INPUT_POST,'idade', FILTER_VALIDATE_INT);





        if (strlen(trim($nome)) <3) {
            $erros[] = "Preencha seu nome completo";
        }
        if (empty($email)) {
            $erros[] = "Preencha seu e-mail corretamente";
        }
        if ($idade < 18) {
            $erros[] = "cadastro somente para maiores de 18 anos.";
        }
        if (empty($erros)) {
            echo "<h2>Confira seus dados:</h2>";
            echo "Nome:  $_POST[nome]  <br>";
            echo "E-mail:  $_POST[email]  <br>";
            echo "Idade:  $_POST[idade]";
        }else{
            foreach($erros as $erro){
                echo "$erro <br>";
            }
        }
    }
    ?>