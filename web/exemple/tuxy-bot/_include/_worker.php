<?php
    if(!empty($_POST)) {
        # TODO: Verifică dacă datele primite sunt valide
        echo '<p>USER: '. htmlentities($_POST["command"]) .'</p>';
        
        $request = explode(" ", $_POST["command"]);
        switch ($request[0]) {
            case '/help':
                echo '/help - Afișează detalii despre toate comenzile <br>';
                # TODO: Adaugă detalii despre toate comenzile suportate
                break;
        }
    }
    else {
        echo '<p>Pentru mai multe detalii rulați comanda /help.</p>';
    }
?>
