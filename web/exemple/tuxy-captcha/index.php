<?php
    define("FLAG_OK", true);
    require('_include/_captcha.php');
    main();
?>

<!doctype html>
<html lang="ro">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Tuxy captcha</title>

    <meta name="author" content="Tuxy Pinguinescu" />
    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <header>
        <h1>Tuxy Capcha</h1>
    </header>

    <section id="continut">
        <?php if(isset($continut)) echo $continut; ?>
    </section>

    <section id="captcha">
        <?php if(!empty($ecuatie)) { ?>
            <form action="#" method="post">
                <p>Pentru a trece la pasul următor trebuie să rezolvați următoarea ecuația:</p>
                <?php echo $ecuatie; ?>
                <label for="rezultat">Rezultat:</label>
                <input type="text" name="rezultat">

                <input type="submit">
            </form>
        <?php } ?>
    </section>

    <footer>
        <h3>Toate drepturile rezervate. Tuxy Pinguinesc</h3>
    </footer>
</body>
</html>
