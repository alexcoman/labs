<?php
if(!defined("FLAG_OK")) { http_response_code(403); die();}

session_start();
require('_include/_commands.php');

init();

# TODO(tuxy): Verifică dacă datele primite sunt valide
# TODO(tuxy): Rescrie bucățile de cod redundante
# TODO(tuxy): Codul este stufos și greu de menținut, trebuie găsită
#             o altă abordare.

if (!empty($_POST)) {

    # TODO(tuxy): De verificat dacă este suficient.
    $command = htmlentities($_POST["command"]);

    $cerere = explode(" ", $_POST["command"], 2);
    var_dump($cerere);
    switch ($cerere[0]) {
        case '/curata':
            $raspuns = curata();
            break;

        case '/help':
            $raspuns = help();
            break;

        case '/retine':
            if (count($cerere) < 2) {
                $raspuns = "Numar invalid de argumente";
                break;
            }

            $argumente = explode(" ", $cerere[1], 2);
            if(count($argumente) != 2) {
                $raspuns = "Nu ati precizat valoarea.";
                break;
            }

            $raspuns = retine($argumente[0], $argumente[1]);
            break;

        case '/palindrom':
            if(count($cerere) < 2) {
                $raspuns = "Numar invalid de argumente";
                break;
            }

            $raspuns = palindrom($cerere[1]);
            break;

        default:
            $raspuns = 'Comanda nu este disponibila.';
    }

    # FIXME(tuxy): Nu pare o idee foarte strălucită.
    array_push($_SESSION["istoric"], "~ $ $command");
    array_push($_SESSION["istoric"], $raspuns);
}

?>
