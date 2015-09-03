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


```
~ $ pypy
```

    !python
    Python 2.7.3 (2.2.1+dfsg-1ubuntu0.2, Dec 02 2014, 23:00:55)
    [PyPy 2.2.1 with GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    And now for something completely different: ``well, it's wrong but not
    so "very wrong" as it looked``
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

##Intreg
    
    !python
    >>> 10
    10
    >>> int(100)
    100
    >>> 

##Float
    
    !python
    >>> 10.0
    10.0
    >>> float(10)
    10.0

##Long - Python 2.x
    
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

#Resurse

- www.python.org
- www.learnpython.org/
- www.learnpythonthehardway.org
- www.corepython.com
- www.codecademy.com/tracks/python
- www.checkio.org
- www.ropython.org
- www.github.com/RoPython
