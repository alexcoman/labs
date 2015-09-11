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

#Structuri de date

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