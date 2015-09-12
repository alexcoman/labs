#Limbajul Python

---

#Obiective

- Prezentarea limbajului Python
- Pregătirea mediului de lucru
- Familiarizarea cu limbajul
    - Tipuri de date (int, float, *long*, str)
    - Operatori
    - Comentarii
    - Funcții built-in (print, input, *raw_input*, open)
    - Instrucțiuni condiționale (if - elif - else)
 
*Timp estimat: **45** de minute*

---

#Limbajul Python

---

#Implementări ale limbajului

- **CPython - [python.org](https://www.python.org/)**
- Jython - [jython.org](http://www.jython.org/)
- Python for .NET - [pythonnet.sourceforge.net](http://pythonnet.sourceforge.net/)
- IronPython - [ironpython.net](http://ironpython.net/)
- PyPy - [pypy.org](http://pypy.org/)

---

#Instalarea

Mai multe detalii pe link-urile de mai jos:

- **CPython** - [python.org/downloads/](https://www.python.org/downloads/)
- Jython - [jython.org/downloads.html](http://www.jython.org/downloads.html)
- Python for .NET - [http://sourceforge.net/projects/pythonnet/files/](http://sourceforge.net/projects/pythonnet/files/)
- IronPython - [ironpython.net/download/](http://ironpython.net/download/)
- PyPy - [pypy.org/download.html](http://pypy.org/download.html)


---

#Interpretorul

```
~ $ python3
```

    !python
    Python 3.4.0 (default, Jun 19 2015, 14:20:21) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> dir
    <built-in function dir>
    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help(dir)

    >>> 

Funcții foarte utile:  ```dir(...)``` și ```help(...)```.

---

#Interpretorul

```
~ $ python3 search.py "Python România"
```
    
    !text
    Titlu: <b>Python</b> Weekend @Iași - RoPython
        URL:https://conference.ropython.org/
    Titlu: LocalUserGroups - <b>Python</b> Wiki
        URL:https://wiki.python.org/moin/LocalUserGroups
    Titlu: <b>Romania</b> | <b>Python</b> Data Recovery
        URL:http://www.python.ro/romania
    Titlu: <b>Python</b> Data Recovery | Recover every bit
        URL:http://www.python.ro/


```
~ $ cat search.py
```

    !python
    import sys
    import requests

    def search(query):
        url = "http://ajax.googleapis.com/ajax/services/search/web"
        params = {"v": "1.0", "q": query}
        response = requests.get(url, params=params)
        data = response.json()
        for result in data["responseData"]["results"]:
            print("Titlu: {}\n\tURL:{}".format(result["title"],
                                               result["url"]))

    if __name__ == "__main__":
        search(sys.argv[1])

---

#Mediul de lucru

- Editor text:
    - Sublime Text
    - Notepad++
    - Vim

Mai multe exemple aici: [en.wikipedia.org/wiki/List_of_text_editors](https://en.wikipedia.org/wiki/List_of_text_editors).

- IDE-uri pentru Python:
    - Komodo (Windows/Linux/Mac OS X)
    - LiClipse (Linux/Mac OS X/Windows)
    - PyCharm (Linux/Mac OS X/Windows)
    - Wing IDE (Windows, Linux, Mac OS X)

Mai multe exemple aici: [wiki.python.org/moin/IntegratedDevelopmentEnvironments](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

---

#Tipuri de date

---

#Tipuri de date numerice

**Intreg**
    
    !python
    >>> 10
    10
    >>> int(100)
    100
    
    >>> dir(int(10))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    
    >>> int(10).bit_length()
    4
    
    >>> int(10).conjugate()
    10
    
    >>> int(10).denominator
    1
    
    >>> int(10).numerator
    10

---

#Tipuri de date numerice

**Float**
    
    !python
    >>> 10.0
    10.0
    >>> float(10)
    10.0
    
    >>> dir(float(10))
    ['...', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag',
     'is_integer', 'real']
    
    >>> float(10).as_integer_ratio()
    (10, 1)
    
    >>> float(10).hex()
    '0x1.4000000000000p+3'
    
    >>> float(10).is_integer()
    True

---

#Tipuri de date numerice

**Long - Python 2.x**
    
    !python
    >>> sys.maxint + 1
    9223372036854775808L
    >>> type(_)
    <type 'long'>
    >>> long(10)
    10L
    
    >>> dir(long(10))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    
    >>> (sys.maxint + 1).denominator
    1L
    
    >>> (sys.maxint + 1).imag
    0L
    
    >>> (sys.maxint + 1).real
    9223372036854775808L
    
    >>> (sys.maxint + 1).conjugate()
    9223372036854775808L
    >>> (sys.maxint + 1).bit_length()
    64

---

#Tipuri de date numerice

**Complex**
    
    !python
    >>> a = complex(10, 5)
    >>> a
    (10+5j)
    
    >>> dir(a)
    ['...', 'conjugate', 'imag', 'real']
    
    >>> a.imag
    5.0

    >>> a.real
    10.0

    >>> a.conjugate()
    (10-5j)

---

#Tipuri de date booleene
    
    !python
    >>> True
    True
    >>> False
    False
    >>> bool(1)
    True
    >>> bool(0)
    False

    >>> dir(bool(1))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    >>> bool(1).bit_length()
    1

---

#Șirurile de caractere
    
    !python
    sir1 = 'Acesta este un sir de caractere'
    sir2 = "Acesta este un sir de caractere"
    sir3 = """Acesta este un sir de caractere
    pe mai multe linii."""
    sir4 = '''Acesta este un sir de caractere
    pe mai multe linii.'''
    sir5 = (
        "Acesta este un sir de caractere foarte"
        " lung, dar care totusi este pe o singura "
        " linie."
    )
    
    >>> dir("")
    ['...', 'capitalize', 'center', 'count', 'decode', 'encode',
     'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum',
     'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper',
     'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind',
     'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
     'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
     'upper', 'zfill']

---

#Șirurile de caractere

    !python
    >>> "Ana are mere.".capitalize()
    'Ana are mere.'

    >>> "ana are mere.".center(62)
    '                        ana are mere.                         '
    >>> "ana are mere.".count("a")
    3

    >>> "ana are mere.".endswith("mere.")
    True

    >>> "ana are mere.".startswith("ana")
    True

    >>> "ana are mere.".partition("are")
    ('ana ', 'are', ' mere.')
    
    >>> "ana are mere.".upper()
    'ANA ARE MERE.'
    
    >>> "ana are mere.".title()
    'Ana Are Mere.'
    
    >>> "ana are mere.".split()
    ['ana', 'are', 'mere.']

---

#Șirurile de caractere

    !python
    >>> "%s are mere." % "Ana"
    'Ana are mere.'

    >>> "%s are %s." % ("Ana", "mere")
    'Ana are mere.'

    >>> "%(nume)s are %(fructe)s." % {"nume": "Ana", "fructe": "mere"}
    'Ana are mere.'

    >>> "{} are {}.".format("Ana", "mere")
    'Ana are mere.'

    >>> "{nume} are {fructe}.".format(nume="Ana", fructe="mere")
    'Ana are mere.'

---

#Operatori

---

#Comentarii

---

#Funcții built-in

---

#Instrucțiuni condiționale

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