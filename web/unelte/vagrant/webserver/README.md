## Webserver

Fișierul `Vagrantfile` conține specificațiile pentru crearea unui server web ce va conține următoarele aplicații:

 - nginx
 - PHP 5
 - mysql-server

## Câteva comenzi utile

1. Creăm o nouă mașină virtuală pe baza specificațiilor descrise în fișierul `Vagrantfile`.

	```bash
	~ $ vagrant up
	```
2.  Adăugăm o nouă intrare în fișierul `/etc/hosts` pentru a fi mai ușor de accesat serverul web.

	```bash
	sudo echo "192.168.50.210	webserver.local" >> /etc/hosts
	```
3. Interacțiunea cu serverul web

	În directorul local au fost create două directoare noi:
		-  `.www` care va conține aplicația dumneavoastră
		- `.logs` care va conține fișierele de log

	```bash
	.
	├── .log
	│   ├── nginx-access.log
	│   ├── nginx-error.log
	│   └── php-access.log
	└── .www
	```
4. Verificăm dacă aplicația funcționează
	```
	~ $ echo "<?php echo 'OK.'; ?>" > .www/index.php
    ~ $ chmod 755 .www/index.php
	~ $ wget http://webserver.local/
	Resolving webserver.local (webserver.local)... 192.168.50.210
	Connecting to webserver.local (webserver.local)|192.168.50.210|:80... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: unspecified [text/html]
	Saving to: ‘index.html’
	(488 KB/s) - ‘index.html’ saved [3]

	~ $ cat index.html
	OK.
	```
5. Distruge mașina virtuală.

	```bash
	~ $ vagrant destroy
	```

Mai multe detalii puteți găsi în tutorialul [Vagrant - noțiuni introductive][0].

[0]:  https://teaching.alexcoman.com/resurse/tutorial/vagrant/2017/03/19/vagrant-notiuni-introductive/
