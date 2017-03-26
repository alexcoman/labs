<?php
if(!defined("FLAG_OK")) { http_response_code(403); die();}

session_start();
$continut = '';
$ecuatie = '';

function handle_post(){
    global $continut;
    global $ok;

    $rezultat = intval($_SESSION["rezultat"]);
    unset($_SESSION["rezultat"]);

    if(!isset($_SESSION["rezultat"])) {
        $continut = 'Nu a fost generata nici o ecuatie pentru dumneavoastra.';
    }
    elseif(!isset($_POST["rezultat"])) {
        $continut = 'Pentru a trece la pasul urmator trebuie sa rezolvati ecuatia.';
    }
    elseif($_POST["rezultat"] != $_SESSION["rezultat"]) {
        $continut = 'Solutia oferita nu este valida.';
    }
    elseif(intval($_POST["rezultat"]) === $_SESSION["rezultat"]) {
        $continut = 'Felicitari soluția oferita este cea corectă.';
    }
    else {
        # Acest caz nu a fost tratat.
        http_response_code(400);
        die();
    }
}


function handle_get(){
    global $ecuatie;

    $coeficient = rand(1, 5);
    $operand = rand(1, 5);
    $necunoscuta = rand(1, 20);
    $rezultat = $coeficient * $necunoscuta + $operand;

    $_SESSION["rezultat"] = $necunoscuta;
    $ecuatie = "$coeficient x + $operand = $rezultat";
}

function main(){
    $method = $_SERVER['REQUEST_METHOD'];
    switch ($method) {
      case 'POST':
        handle_post();
        break;
      case 'GET':
        handle_get();
        break;
      default:
        die("Pentru moment aplicația nu suportă această metodă.");
        break;
    }
}

?>