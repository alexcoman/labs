##Tuxy-Bot

Tuxy Pinguinescu are nevoie de o unealtă web care să îi ușureze munca de zi cu zi.
Pentru că nimeni din echipa lui Tuxy nu este suficient de pregătit pentru a dezvolta **Tuxy Bot** această sarcină îți revine ție.

Tuxy Bot trebuie să știe să rezolve următoarele sarcini:

- /reține cheie valoare
    - Se va salva această informație și în toate comenzile ce vor fi trimise ulterior se va schimba orice apariție a cuvântului *cheie* cu valoarea acestuia
- /palindrom valoare
    - Verifică dacă valoarea primită este un șir palindrom
- /calculează valoare1 operator valoare2
- /evaluează expresie
- /curăță
    - Șterge toate informațiile salvate până în acest moment

Câteva exemple:

```
/reține acasă Iași
Am învățat termenul `acasă`.

/reține expresie 20 + 4 - 3 * 8
Am învățat termenul `expresie`.

/evaluează expresie
Rezultatul expresiei: '20 + 4 - 3 * 8' este 0

/palindrom acasa
Șirul 'Iași' nu este palindrom.

/curăță
Am șters toate informațiile din această sesiune.
``