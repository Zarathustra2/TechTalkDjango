# TechTalk

Hey, bevor du zum TechTalk-django kommst, würde ich dich bitten, schonmal folgende Dinge zu testen & beachten.

Wenn du keine Kenntnisse in Python hast, ist das kein Problem. Das Meiste lernt man so wie so beim Programmieren.
Ledglich OOP sollte dir kein Fremdwort sein.

1. Python3 installiert
2. Verbindung mit dem Eduroam-Wifi
3. Ich empfehle den Editor Pycharm von Jetbrains - gibt keinen besseren Editor für Django - , 
als Student müsst ihr auch nichts zahlen - gilt auch für
 alle anderen Editoren von denen für z.B. Java(Intellij), SQL(DataGrip), C++(Clion), Go(Goland) etc. 
 
    Alternativ VS-Code oder Sublime. 
    Dort könnt ihr durch das Installieren von Paketen den Editor in einen Django-Editor verwandeln. 
    
    
## Geplanter Ablauf

1. Was ist Django & Bootstrap? - 10Min

2. Wie kommt Django zum Einsatz? - 5Min

3. Meine Erfahrung mit Django - Vorteil & Nachteile - 5Min

4. Programmieren - Hauptteil

    - CBV vs Func Views
    - Template Language
    - Models & Forms
    - Bootstrap Grid System
    - context processors
    - Common Mistakes/Bugs/Errors
    
5. Abschluss, Verweis auf Projekt der Freitagsrunde: Community der Fakultät IV - 5Min   
    
## PreSetup:

Stell sicher, dass du Python3 installiert hast. Dazu öffne dein Terminal und gib ein ```python -V```. Es mag sein, dass manche von euch sowhol Python 2 als 
auch PYthon3 installiert haben. Falls das der Fall ist, dann einfach ```python3 -V``` eingeben im Terminal.

Anschließend installiert ihr das paket virtualenv.

Einfach eingeben im Terminal ```pip3 install --user virtualenv```

Anschließend könnt ihr schonmal folgendes testen:

1. Erstellt einen neuen Ordner 
2. Navigiert zum Order mit dem Terminal und dann führt diesen Befehl aus: ```python3 -m venv myEnv```
3. Jetzt müssen wir die neue Virtualenv mit dem folgenden Befehl aktivieren: ```source myEnv/bin/activate```
4. Wenn alles gut gelaufen ist, dann steht jetzt in eurem Terminal (myEnv) vor jeder Zeile
5. Anschließend installieren wir django. ```pip3 install Django```
6. Lauft dann folgenden Command: ```django-admin.py startproject techtalk .```
7. Ganz wichtig ist der Punkt am Ende, der sorgt für Ordnung im Ordner. Bitte nicht vergessen!
8. ```python3 manage.py migrate``` eingeben
9. ```python3 manage.py runserver``` eingeben
10. Jetzt öffnet euren Browser und ruft 127.0.0.1:8000 auf.
11. Wenn alles geklappt habt, solltet ihr eine Willkommensseite sehen.

Wenn es irgendwo zwischen durch Probleme gibt, könnt ihr mir gerne eine E-Mail schicken: dario.heinisch@gmail.com

## Tipps: 

Aktivierung der venv bei Windows: {{venv}}\Scripts\activate - hab ich mir sagen lassen ;-)

Linux/Mac: source {{venv}}/bin/activate


## Pakete Sublime

- Anaconda
- Sublime Code Intel
- Djaneiro


## Coole Django Packages

- Channels
- Rest Framework
- django-cleanup
- django-polymorphic
- django-boostrap3 oder 4
- django-heroku
- django-allauth



## Django Models

| Method  | Beschreibung  | Code  |
| ------------- | ------------- | ------------- |
| get | Gibt ein Objekt zurück, Error wenn mehrere oder keins | user = User.objects.get(id=1) |
| get_or_create  | Gibt Objekt und bool zurück, falls das Objekt erstellt wurde  | User, created = User.objects.get_or_create(id=1, username=“tuberlin“) |
| filter  | Gibt eine Queryset zurück  | users = User.objects.filter(id__gte=1) # id__gte = 1 == id >= 1  |
| create | Erstellt ein neues Objekt und gibt es zurück  | user = User.objects.create(username=“freitagsrunde“)  |
| delete | Löscht Objekt oder Objekte. Kann aufgerufen werden auf einzelnes Objekt oder Queryset  | User.objects.filter(id__gte=1).delete() User.objects.get(id=1).delete()  |
| update  | Updated ein Feld. Kann nur auf queryset aufgerufen werden | Articles.objects.filter(headline=“Clinton won Election“).update(headline=”Trump won Election”) |



##Django Template Syntax



 Method  | Beschreibung  | Code  |
| ------------- | ------------- | ------------- |
| extends | Template erweitert ein anderes Template, kann nur einmal verwendet werden und muss erste Zeile sein | {% extends "base.html" %} |
| include | Template fügt dein Code eines anderen Templates mit ein | {% include "sidebar.html" %} |
| if | if statement im template | {% if request.user.is_authenticated %} Welcome {% else %} Register {% endif %} |
| with | Speichert Wert/Objekt in einer variable | {% with request.user.username as username %} Hi, {{ username }}, Wie geht es dir {{ username }} {% endwith %} |
| for | For-Loop über ein Queryset | {% for user in users %} {{ user.username }} {% endfor %} |


## Django Terminal Commands

base command: python3 manage.py some_command

| Command | Beschreibung  | Code  |
| ------------- | ------------- | ------------- |
| runserver | startet den server auf 127.0.0.1:8000 | python3 manage.py runserver |
| startapp | Erstellt eine neue App | python3 manage.py startapp users |
| shell | Python-Shell mit Zugriff auf alle Modelle im Projekt | python3 manage.py shell |
| makemigrations | Erstellt migration-files für die Datenbank | python3 manage.py makemigrations |
| migrate | migration-files werden ausgeführt, Datenbank wird angepasst | python3 manage.py migrate |
| createsuperuser | Erstellt einen Superuser, hat zugriff auf alles auf der Adminseite | python3 manage.py createsuperuser |
| collectstatic | Sammelt alle static Files, und deployed sie z.B. zu Amazon  | python3 manage.py collectstatic |


## Bootstrap

| Code  | Beschreibung  | 
| ------------- | ------------- |
| col-lg-12 | 12 = 100%, 1 = 100%*1/12 |
| btn | button |
| panel | "Tafel" |
| text-center | Zentriert Text, kann auch Text färben mit text-success z.B. |
| table | Table class, häufig im Zusammenspiel mit 'table class="table borderless table-hover"' |
| hidden-xs | display:none; für Smartphones, für tablets z.B. hidden-sm |

 
