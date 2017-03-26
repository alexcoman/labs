<?php
    define("FLAG_OK", true);
    require('_include/_bot.php');
?>

<!doctype html>
<html lang="ro">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Tuxy Bot</title>

        <meta name="author" content="Tuxy Pinguinescu" />
        <meta name="description" content="" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body>
        <header>
            <h1>Tuxy Bot</h1>
        </header>

        <section id="continut">
            <?php
                # FIXME(tuxy): Nu pare o idee buna.
                foreach($_SESSION["istoric"] as $comanda) {
                    echo "$comanda <br>";
                }
            ?>
        </section>

        <section id="chat">
            <form action="#" method="post">
                Comanda: <input type="text" name="command">
                <input type="submit">
            </form>
        </section>

        <footer>
            <h3>Toate drepturile rezervate. Tuxy Pinguinescu</h3>
        </footer>
    </body>
</html>
