#TechTalk

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
    
    
##Geplanter Ablauf

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
    
##PreSetup:

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

Wenn es irgendwo zwischen durch Probleme gibt, könnt ihr mir gerne eine E-Mail schicken: dario.heinsich@gmail.com

##Tipps: 

Aktivierung der venv bei Windows: {{venv}}\Scripts\activate - hab ich mir sagen lassen ;-)

Linux/Mac: source {{venv}}/bin/activate


##Pakete Sublime

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
