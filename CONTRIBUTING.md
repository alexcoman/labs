# Cum să contribui

Pentru a contribui va trebui sa faceți in primul rand un *fork* al depozitului de cod.
Pentru acest lucru va trebui să accesați cu ajutorul unui browser web [pagina depozitului de cod][0] și să apăsați pe butonul **Fork** situat în partea dreapta sus a paginii.

![Fork al depozitului de cod alexcoman/labs](https://teaching.alexcoman.com/img/git-propunerea-unei-solutii/01-fork.png)

## Elaborarea soluției

În acest moment aveți la dispoziție toate resursele necesare pentru a putea trece la elaborarea soluției pentru problemele propuse în cadrul laboratorului.

Mai jos puteți găsi o secvență posibilă de pași pe care *Tuxy Pinguinescu* (cu numele de utilizator *tuxy_pinguinescu* pe GitHub) ar putea să îi urmeze pentru a propune o soluție.

1. Va alege un director de lucru cât mai ușor de regăsit pentru următoarele laboratoare.

    ```bash
    ~ $ cd ~/work/facultate/anul-2/semestrul-2/tweb
    ```

2.  Va face o copie locală a depozitului de cod

    ```bash
    ~ $ git clone https://github.com/tuxy_pinguinescu/labs
    ```

3. Va actualiza directorul de lucru
    ```bash
    cd labs
    ```

4. Se va asigura că *fork*-ul său conține ultima versiune a codului
    ```bash
    ~ $ # Adăugăm o referință către depozitul de cod sursă
    ~ $ git remote add upstream https://github.com/alexcoman/labs

    ~ $ # Ne poziționăm pe branch-ul `master`
    ~ $ git checkout master

    ~ $ # Obținem ultimile modificări din cadrul depozitului de cod sursă
    ~ $ # upstream - numele remote-ului pe care l-am adăugat
    ~ $ # master - branch-ul care ne interesează
    ~ $ git pull upstream master

    ~ $ # Actualizăm informațiile din cadrul fork-ului nostru
    ~ $ git push origin master
    ```

5. Va adăuga un *branch* nou special pentru acest laborator
    ```bash
    git checkout -b tweb/laborator-html
    ```

6.  Se va asigura că structura de directoare pentru soluțiile sale există(numele folder-ului de soluții va fi de tipul prenume_nume)
    ```bash
    mkdir -p web/solutii/tuxy_pinguinescu
    ```

7. Toate fișierele cu rezolvările vor fi plasate în directoarele corespunzătoare

## Cum să vă propuneți soluția

După redactarea fișierelor ce reprezintă soluția pentru unul dintre exercițiile propuse în cadrul unui laborator va trebui să încapsulați acele modificări în cadrul unui *commit*.

Pentru început trebuie să selectați și să adăugați toate modificările care vă interesează.

```bash
~ $ git status     # pentru a vedea starea curentă a depozitului de cod
~ $ git add fișier # pentru fiecare fișier pe care dorim să îl adăugăm
~ $ git status     # pentru a verifica că toate resursele pe care le dorim sunt prezente
```

Un exemplu de rezultat al comenzilor de mai sus ar putea fi:

```bash
On branch tweb/laborator-html
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   solutii/tuxy_pinguinescu/README.md
    new file:   solutii/tuxy_pinguinescu/blog/articole/bine-ati-venit.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/index.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/retele-de-calculatoare/index.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/retele-de-calculatoare/modelul-osi.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/tehnologii-web/index.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/tehnologii-web/prezentare-css.html
    new file:   solutii/tuxy_pinguinescu/blog/articole/tehnologii-web/prezentare-html.html
    new file:   solutii/tuxy_pinguinescu/blog/contact.html
    new file:   solutii/tuxy_pinguinescu/blog/despre.html
    new file:   solutii/tuxy_pinguinescu/blog/index.html
```

După ce am adăugat toate modificările pe care le dorim putem să le încapsulăm într-un commit folosind următoarea comandă:

```
~ $ git commit -m "Mesajul pe care dorim să îl atașăm acestor modificări"
```

Pentru a urca aceste modificări în cadrul depozitului de cod de pe Github puteți folosi comanda `git push`.

```bash
# origin - este referința către fork-ul nostru
# tweb/laborator-html - este numele branch-ului în cadrul căruia am redactat soluția
~ $ git push origin tweb/laborator-html
```

După ce ați trimis modificările propuse către fork-ul vostru, va trebui să deschideți un *Pull request* către [depozitul de cod sursă][0].

Pentru a face acest lucru va trebui să accesați pagina destinată branch-urilor din cadrul depozitului vostru de cod.
Pentru Tuxy Pinguinescu această pagini este `https://github.com/tuxy_pinguinescu/labs/branches`.

În cadrul acestei pagini vor fi afișate toate *branch*-urile existente în cadrul depozitului vostru de cod cu o serie de acțiuni pentru fiecare dintre ele. În cazul nostru acțiunea care ne interesează este **New pull request**.

![New pull request](https://teaching.alexcoman.com/img/git-propunerea-unei-solutii/02-new-pull-request.png)

[0]: https://github.com/alexcoman/labs