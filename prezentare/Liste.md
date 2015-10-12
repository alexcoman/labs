#Limbajul Python - Liste și Tupluri

---

#Liste și Tupluri

**Lista**: Structură de date flexibilă ce poate încapsula date eterogene.

	!python
	laborator_python = [
	    ["Laboratorul 1",
	        ["interpretor", "CPython", "IronPython", "PyPy"],
	        ["exerciții", "maxim", "palindrom", "par", "putere"],
	        ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
	     ],
	]
	laborator_python[1] = ["Laboratorul 2"] 


**Tupluri**: Structură de date inflexibilă ce poate încapsula date eterogene.

	!python
	laborator_python = (
	    ("Laboratorul 1",
	        ("interpretor", "CPython", "IronPython", "PyPy"),
	        ("exerciții", "maxim", "palindrom", "par", "putere"),
	        ("note", 10, 5.4, 3.4, 10, 2, 1, 4),
	     ),
	)
	laborator_python[1] = ["Laboratorul 2"]

	Traceback (most recent call last):
  		File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

---

#Accesarea elementelor

	!python
	>>> laborator_python = [
	...     ["Laboratorul 1",
	...         ["interpretor", "CPython", "IronPython", "PyPy"],
	...         ["exerciții", "maxim", "palindrom", "par", "putere"],
	...         ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
	...      ],
	... ]

	>>> laborator_python[0]
	['Laboratorul 1', ['interpretor', 'CPython', 'IronPython', 'PyPy'],
	['exerci\xc8\x9bii', 'maxim', 'palindrom', 'par', 'putere'],
	['note', 10, 5.4, 3.4, 10, 2, 1, 4]]
	
	>>> laborator_python[0][1]
	['interpretor', 'CPython', 'IronPython', 'PyPy']
	
	>>> laborator_python[0][1][1]
	'CPython'
	
	>>> laborator_python[0][1][2]
	'IronPython'
	
	>>> laborator_python[0][1][2][3]
	'n'

---


#Indexi negativi

	!python
	>>> laborator_python = [
	...     ["Laboratorul 1",
	...         ["interpretor", "CPython", "IronPython", "PyPy"],
	...         ["exerciții", "maxim", "palindrom", "par", "putere"],
	...         ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
	...      ],
	... ]
	>>> laborator_python[-1]
	['Laboratorul 1', ['interpretor', 'CPython', 'IronPython', 'PyPy'],
	['exerci\xc8\x9bii', 'maxim', 'palindrom', 'par', 'putere'],
	['note', 10, 5.4, 3.4, 10, 2, 1, 4]]
	
	>>> laborator_python[-1][-1][0]
	'note'
	
	>>> laborator_python[-1][-1][-1]
	4
	
	>>> laborator_python[-1][-1][-2]
	1
	
	>>> laborator_python[-1][-1][-3]
	2
	
	>>> laborator_python[-1][-2][-3]
	'palindrom'

---

#List slices (lista[început:sfârșit])

	!python
	>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	>>> lista[0:3]
	[1, 2, 3]
	
	>>> lista[:3]
	[1, 2, 3]
	
	>>> lista[3:6]
	[4, 5, 6]
	
	>>> lista[3:]
	[4, 5, 6, 7, 8, 9]
	
	>>> lista[-1:]
	[9]
	
	>>> lista[-2:]
	[8, 9]
	
	>>> lista[:-1]
	[1, 2, 3, 4, 5, 6, 7, 8]
	
	>>> lista[:-2]
	[1, 2, 3, 4, 5, 6, 7]

---

#List slices (lista[început:sfârșit:pas])

	!python
	>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	>>> lista[1::2]
	[2, 4, 6, 8]
	
	>>> lista[::2]
	[1, 3, 5, 7, 9]
	
	>>> lista[::-1]
	[9, 8, 7, 6, 5, 4, 3, 2, 1]
	
	>>> lista[-1:-5:-1]
	[9, 8, 7, 6]

---

#Operații utile

	!python
	>>> lista = []
	>>> lista.append(1)
	>>> lista.append(2)
	>>> lista.append(3)
	>>> lista
	[1, 2, 3]
	
	>>> lista.extend([4, 5, 6])
	>>> lista
	[1, 2, 3, 4, 5, 6]
	
	>>> lista.reverse()
	>>> lista
	[6, 5, 4, 3, 2, 1]
	
	>>> lista.sort()
	>>> lista
	[1, 2, 3, 4, 5, 6]


Mai multe metode utile se pot găsi folosind `dir(lista)` și `help(lista.count)`.

---

#Referințe

	!python
	>>> lista = [1, 2, 3, 4, 5]
	>>> lista2 = lista
	>>>
	>>> lista.append("x")
	>>> lista2.append("y")

---

#Referințe

	!python
	>>> lista = [1, 2, 3, 4, 5]
	>>> lista2 = lista
	>>>
	>>> lista.append("x")
	>>> lista2.append("y")
	>>> 
	>>> lista
	[1, 2, 3, 4, 5, 'x', 'y']
	
	>>> lista2
	[1, 2, 3, 4, 5, 'x', 'y']

---

#Referințe

	!python
	>>> lista = [[0]] * 10
	>>> lista
	[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
	
	>>> lista[0].append(1)
	>>> lista[0].append(2)
	>>> lista[0].append(3)
	>>> lista[0].append(4)
	>>> lista[0].append(5)
	>>> lista[0].append(6)
	>>> 
	>>> for rand in lista:
	...     print(rand)
	... 

---

#Referințe

	!python
	>>> lista = [[0]] * 10
	>>> lista
	[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
	
	>>> lista[0].append(1)
	>>> lista[0].append(2)
	>>> lista[0].append(3)
	>>> lista[0].append(4)
	>>> lista[0].append(5)
	>>> lista[0].append(6)
	>>> 
	>>> for rand in lista:
	...     print(rand)
	... 
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	[0, 1, 2, 3, 4, 5, 6]
	>>> 

---

#Referințe

	!python
	>>> lista = [1, 2, 3, [1, 2, 3]]
	>>> lista2 = list(lista)
	>>> 
	>>> lista.append("x")
	>>> lista2.append("y")
	>>>
	---

	#Referințe

	>>> lista = [1, 2, 3, [1, 2, 3]]
	>>> lista2 = list(lista)
	>>> 
	>>> lista.append("x")
	>>> lista2.append("y")
	>>>

	>>> lista
	[1, 2, 3, [1, 2, 3], 'x']

	>>> lista2
	[1, 2, 3, [1, 2, 3], 'y']

---

#Referințe

	!python
	>>> lista = [1, 2, 3, [1, 2, 3]]
	>>> lista2 = list(lista)
	>>> 
	>>> lista.append("x")
	>>> lista2.append("y")
	>>> 

	>>> lista
	[1, 2, 3, [1, 2, 3], 'x']

	>>> lista2
	[1, 2, 3, [1, 2, 3], 'y']

	>>> lista[3].append(4)
	>>> lista2[3].append(4) 

---

#Referințe

	!python
	>>> lista = [1, 2, 3, [1, 2, 3]]
	>>> lista2 = list(lista)
	>>> 
	>>> lista.append("x")
	>>> lista2.append("y")
	>>> 

	>>> lista
	[1, 2, 3, [1, 2, 3], 'x']

	>>> lista2
	[1, 2, 3, [1, 2, 3], 'y']
	 
	>>> lista[3].append(4)
	>>> lista2[3].append(4) 

	>>> lista
	[1, 2, 3, [1, 2, 3, 4, 4], 'x']

	>>> lista2
	[1, 2, 3, [1, 2, 3, 4, 4], 'y'] 
