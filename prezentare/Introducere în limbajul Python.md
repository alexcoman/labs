#Introducere în limbajul Python

---

#Implementări ale limbajului

- **[CPython](https://www.python.org/)**
- [Jython](http://www.jython.org/)
- [Python for .NET](http://pythonnet.sourceforge.net/)
- [IronPython](http://ironpython.net/)
- [PyPy](http://pypy.org/)

---

#Interpretorul Python

```
~ $ python3
```

    !python
    Python 3.4.0 (default, Jun 19 2015, 14:20:21) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

---

#Interpretorul Python
    
    !python
    Python 3.4.0 (default, Jun 19 2015, 14:20:21) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    >>> 2 + 3
    5
    >>> _ + 3
    8
    >>> "Ana are mere"
    'Ana are mere'
    >>> 2 ** 32
    4294967296
    >>> 

Funcții foarte utile:  ```dir(...)``` și ```help(...)```.

---

#Tipuri și structuri de date

---

#Numere

**Intreg**
    
    !python
    >>> 10
    10
    >>> int(100)
    100
    >>> 

---

#Numere

**Float**
    
    !python
    >>> 10.0
    10.0
    >>> float(10)
    10.0

---

#Numere

**Long - Python 2.x**
    
    !python
    >>> sys.maxint + 1
    9223372036854775808L
    >>> type(_)
    <type 'long'>
    >>> long(10)
    10L

---

#Valori de adevăr
    
    !python
    >>> True
    True
    >>> False
    False
    >>> bool(1)
    True
    >>> bool(0)
    False

---

#Șirurile de caractere
    
    !python
    >>> 'Ana are mere'
    'Ana are mere'
    >>> "Ana are mere"
    'Ana are mere'
    >>> """Ana
    ... are
    ... mere
    ... """
    'Ana\nare\nmere\n'

-

    !python
    sir = 'Ana are mere'
    sir = "Ana are mere"
    sir = """Ana are mere.
    Maria are pere.
    """

---

#Lista

    !python
    # Listă cu numere întregi
    numere = [1, 2, 3, 4, 5]
    
    # Listă cu șiruri de caractere
    litere = ["a", "b", "c", "d", "e"]
    
    # Listele sunt eterogene
    informatii = [
        "De cumpărat", [10, "mere", 20, "pere"],
    ]

-

    !python
    >>> dir([])
    [... 'append', 'count', 'extend', 'index', 'insert', 'pop',
     'remove', 'reverse', 'sort']
    >>> 

---

# Listă

    !python
    >>> lista = []
    >>> lista.append(10)
    >>> lista.append("zece")
    >>> lista
    [10, 'zece']
    >>> lista.insert(0, "unu")
    >>> lista.insert(0, 1)
    >>> lista
    [1, 'unu', 10, 'zece']
    >>> lista.pop()
    'zece'
    >>> lista
    [1, 'unu', 10]
    >>> lista[1]
    'unu'
    >>> lista[-1]
    10
    >>> 

---

#Tuplă

    !python
    >>> tupla = ((1, "unu"), (2, "doi"), (3, "trei"))
    >>> tupla[0]
    (1, 'unu')
    >>> tupla[-1]
    (3, 'trei')
    >>> tupla[-1][1]
    'trei'

**Nu** pot fi modificate.

    !python
    >>> tupla[-1][1] = "trei"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

---


#Set

    !python
    >>> numere_unice = set()
    >>> numere_unice.add(1)
    >>> numere_unice.add(2)
    >>> numere_unice.add(3)
    >>> numere_unice
    set([1, 2, 3])
    >>> numere_unice.add(1)
    >>> numere_unice.add(2)
    >>> numere_unice.add(3)
    >>> numere_unice.add(4)
    >>> numere_unice
    set([1, 2, 3, 4])
    >>> 

-

    !python
    >>> dir(set())
    [..., 'add', 'clear', 'copy', 'difference', 'difference_update',
    'discard', 'intersection', 'intersection_update', 'isdisjoint',
    'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
    'symmetric_difference_update', 'union', 'update']
    >>> 

---

#Dicționar

    !python
    >>> lista_cumparaturi = {
    ...     "Kaufland": {
    ...         "fructe": {
    ...             "mere": (10, "kg"),
    ...             "pere": (10, "kg"),
    ...         },
    ...         "legume": {
    ...             "castraveți": (10, "bucăți"),
    ...             "varză": (10, "kg"),
    ...         }
    ...     },
    ...     "X-ulescu": {
    ...         "pantaloni": {
    ...             "culoare": "negri",
    ...             "mărime": "nu vrea să mă gândesc...",
    ...             "buget": (200, "RON")
    ...         }
    ...     }
    ... }
    >>> 
    >>> lista_cumparaturi["Kaufland"]["fructe"]
    {'mere': (10, 'kg'), 'pere': (10, 'kg')}
    >>> lista_cumparaturi["Kaufland"]["fructe"]["mere"]
    (10, 'kg')
    >>>

---
#Instrucțiuni condiționale

---

# if - elif - else
    
    !python
    if_stmt ::=  "if" expression ":" suite
                 ( "elif" expression ":" suite )*
                 ["else" ":" suite]

-

    !python
    >>> if numar % 5 == 0 and numar % 3 == 0: 
    ...     pass
    ... elif numar % 7 == 0:
    ...     pass
    ... else:
    ...     pass
    ... 

---

#Instrucțiuni repetitive

---

#For

    !python
    for_stmt ::=  "for" target_list "in" expression_list ":" suite
                  ["else" ":" suite]

-

    !python
    >>> for element in (1, 2, 3, 4, 5):
    ...     if element % 5 == 0:
    ...             break
    ... else:
    ...     print("Nici un element divizibil cu 5")
    ... 
    >>> 

-

    !python
    >>> for element in (1, 2, 3, 4):
    ...     if element % 5 == 0:
    ...             break
    ... else:
    ...     print("Nici un element divizibil cu 5")
    ...
    Nici un element divizibil cu 5 
    >>> 

---

#While
    
    !python
    while_stmt ::=  "while" expression ":" suite
                    ["else" ":" suite]

-

    !python
    >>> lista = [1, 2, 3, 4]
    >>> while lista:
    ...     lista.pop()
    ... else:
    ...     print("Am terminat de procesat elementele.")
    ... 
    4
    3
    2
    1
    Am terminat de procesat elementele.
    >>> 

---

#Funcții

---

#Funcții
    
    !python
    funcdef        ::=  [decorators] "def" funcname "(" [parameter_list] ")"
                        ["->" expression] ":" suite
    decorators     ::=  decorator+
    decorator      ::=  "@" dotted_name ["(" [parameter_list [","]] ")"]
                        NEWLINE
    dotted_name    ::=  identifier ("." identifier)*
    parameter_list ::=  (defparameter ",")*
                        | "*" [parameter] ("," defparameter)*
                          ["," "**" parameter]
                        | "**" parameter
                        | defparameter [","] )
    parameter      ::=  identifier [":" expression]
    defparameter   ::=  parameter ["=" expression]
    funcname       ::=  identifier

---

#Funcții

    !python
    def suma(a, b):
        return a + b

    def functie1():
        pass

    def functie2(a, b):
        pass

    def functie3(a, b, c=10):
        pass

    def functie4(*args, *kwargs):
        pass

---

#Exerciții recomandate

##Lucru cu șiruri de caractere

- 1. icao/to_icao și icao/from_icao
- 2. paranteze
- 3. caesar

##Lucru cu liste

- 1. unic
- 2. paint/fill
- 3. paint/cursor 

---
#Resurse

- www.python.org
- www.learnpython.org/
- www.learnpythonthehardway.org
- www.corepython.com
- www.codecademy.com/tracks/python
- www.checkio.org
- www.ropython.org
- www.github.com/RoPython
