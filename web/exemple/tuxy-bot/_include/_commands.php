<?php
if(!defined("FLAG_OK")) { http_response_code(403); die();}

function init(){
    if(!isset($_SESSION["istoric"])) {
        $_SESSION["istoric"] = array();
    }

    if(!isset($_SESSION["dictionar"])) {
        $_SESSION["dictionar"] = array();
    }

}

function retine($cheie, $valoare){
    $_SESSION["dictionar"][$cheie] = $valoare;
    return "Am invatat termenul `$cheie`";
}

function palindrom($valoare) {
    if(isset($_SESSION["dictionar"][$valoare])){
        $valoare = $_SESSION["dictionar"][$valoare];
    }

    # FIXME(tuxy): Funcția ar trebui să returneze o valoare booleană.
    if(strrev($valoare) == $valoare) {
        return "$valoare este palindrom.";
    }
    else {
        return "$valoare nu este palindrom.";
    }
}

function calculeaza($argument1, $operator, $argument2) {
    return 0;
}

function evalueaza($expresie) {
    return 0;
}

function curata(){
    # FIXME(tuxy): Nu pare okay abordarea.
    session_destroy();
    init();
}

function help(){
    # TODO(tuxy): Găsește o metodă să generezi lista de mai jos.
    return '/calculează valoare1 operator valoare2<br>' .
           '/curăță<br>' .
           '/evaluează expresie<br>' .
           '/help - Afișează detalii despre toate comenzile<br>' .
           '/palindrom valoare<br>' .
           '/reține cheie valoare<br>';
}

?>