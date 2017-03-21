<?php

/**
 * Mysqli initial code
 *
 * User permissions of database
 * Create, Alter and Index table, Create view, and Select, Insert, Update, Delete table data
 * 
 * @package         PhpFiddle
 * @link            http://phpfiddle.org
 * @since           2012
*/

require "util/public_db_info.php";
 
//Obținem o conexiune către baza de date           
$conexiune = new mysqli($host_name, $user_name, $pass_word, $database_name, $port);

/**
//Informații referitoare la baza de date

$rezultat = $conexiune->query("SHOW TABLES");
if($rezultat && $rezultat->num_rows > 0){
    echo '<ul>Table existente în baza de date:';
    while($rand = $rezultat->fetch_row()){
        foreach($rand as $cheie){
            echo "<li>{$cheie}</li>";
        }
    }
    echo '</ul>';
    $rezultat->free();
}
**/

/**
//Informații referitoare la structura unui table

$rezultat = $conexiune->query("SELECT COLUMN_NAME, COLUMN_TYPE ".
                              "FROM information_schema.COLUMNS ".
                              "WHERE TABLE_NAME = 'books'");
if($rezultat && $rezultat->num_rows > 0){
    echo '<ul>Câmpurile din tableul books:';
    while($rand = $rezultat->fetch_object()){
        echo "<li>{$rand->COLUMN_NAME} - {$rand->COLUMN_TYPE}</li>";
    }
    echo '</ul>';
    $rezultat->free();
}
**/ 

$rezultat = $conexiune->query("SELECT title, year
                               FROM books
                               WHERE id > 10 AND CHAR_LENGTH(title) > 5
                               LIMIT 10");

if($rezultat && $rezultat->num_rows > 0){
    while ($carte = $rezultat->fetch_assoc()){
       echo "Cartea {$carte['title']} a apărut în anul {$carte['year']}.<br>";;
    }
    $rezultat->free();
}

//Inchidem conexiunea
$conexiune->close();

?>
