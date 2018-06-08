# TechTalk

Hey, bevor du zum TechTalk-django kommst, würde ich dich bitten, schonmal folgende Dinge zu testen & beachten.

Wenn du keine Kenntnisse in Python hast, ist das kein Problem. Das Meiste lernt man so wie so beim Programmieren.
Ledglich OOP sollte dir kein Fremdwort sein.

1. Python3 installiert
2. Verbindung mit dem Eduroam-Wifi
3. Ich empfehle den Editor Pycharm von Jetbrains - gibt keinen besseren Editor für Django - ,
als Student müsst ihr auch nichts zahlen - gilt auch für
 alle anderen Editoren von denen für z.B. Java(Intellij), SQL(DataGrip), C++(Clion), Go(Goland) etc.

    Alternativ VS-Code, Sublime oder [Atom](https://atom.io/).
    Dort könnt ihr durch das Installieren von Paketen den Editor in einen Django-Editor verwandeln.
    Atom ist auf allen Plattformen verfügbar und ist opensource.


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

Falls du nicht sicher bist ob du auf deinem Rechner Dinge umkonfiguerieren oder installieren möchtest, kannst du eine virtuelle Maschine einrichten und eine frische Installation von Ubuntu benutzten. Dafür kannst du [VirtualBox](https://www.virtualbox.org/wiki/Downloads) verwenden und [Ubuntu](https://www.ubuntu.com/desktop) auf deiner virtuellen Maschine installieren.

Stell sicher, dass du Python3 installiert hast. Dazu öffne dein Terminal und gib ein ```python -V```. Es mag sein, dass manche von euch sowhol Python 2 als
auch PYthon3 installiert haben. Falls das der Fall ist, dann einfach ```python3 -V``` eingeben im Terminal.

Stellt mit ```pip3 -V```sicher, dass ihr pip3 installiert habt. Falls nicht, könnt ihr unter Ubuntu mit ```sudo apt install python3-pip```.  
Unter Ubuntu werdet ihr noch das python3-venv Paket benötigen. Führt folgendes im Terminal aus um diesen Paket zu innstallieren: ```sudo apt install python3-venv```.


Anschließend installiert ihr das Paket virtualenv.

Einfach im Terminal ```pip3 install --user virtualenv``` eingeben

Anschließend könnt ihr schonmal folgendes testen:

1. Erstellt einen neuen Ordner
2. Navigiert zum Order mit dem Terminal und führt dann diesen Befehl aus: ```python3 -m venv myEnv```
3. Jetzt müssen wir die neue Virtualenv mit dem folgenden Befehl aktivieren: ```source myEnv/bin/activate```
4. Wenn alles gut gelaufen ist, dann steht jetzt in eurem Terminal (myEnv) vor jeder Zeile
5. Anschließend installieren wir Django: ```pip3 install Django``` (Django wird in der Version 2.0.6 installiert)
6. Führt folgenden Befehl aus (Ganz wichtig ist der Punkt am Ende, der sorgt für Ordnung im Ordner. Bitte nicht vergessen!): ```django-admin.py startproject techtalk .```
7. ```python3 manage.py migrate``` eingeben
8. ```python3 manage.py runserver``` eingeben
9. Jetzt öffnet euren Browser und ruft 127.0.0.1:8000 auf.
10. Wenn alles geklappt habt, solltet ihr eine Willkommensseite sehen.

Wenn es irgendwo zwischen durch Probleme gibt, könnt ihr mir gerne eine E-Mail schicken: dario.heinisch@gmail.com

## Tipps:

Aktivierung der venv bei Windows: {{venv}}\Scripts\activate - hab ich mir sagen lassen ;-)

Linux/Mac: source {{venv}}/bin/activate


## Pakete für Sublime

- Anaconda
- Sublime Code Intel
- Djaneiro

## Pakete für atom
- atom-django

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


## Django Model Fields

| Field  | Beschreibung  | 
| ------------- | ------------- |
| IntegerField | ganze Zahlen |
| PositivIntegerField | natürliche Zahlen |
| DecimalField | Dezimal Zahlen |
| CharField | Text, max_length required |
| TextField | Text |
| OneToOneField* | Beziehung zu einem anderen Model, ein User hat genau ein Profil und ein Profil genau einen User |
| ForeignKey* | Beziehung zu einem anderen Model, ein User kann mehrer Autos haben, aber ein Auto nur einen User(Käufer) |
| ManyToManyField* | Beziehung zu einem anderen Model, ein User kann mehrer Facebookposts liken und ein Facebookpost kann mehrere Likes haben |
| DateTimeField | speichert ein Datum inklusive der Zeit |
| DateField | speichert ein Datum exklusive der Zeit |
| SlugField | Slugs |

1. Alle Beziehungsfelder benötigen auch eine on_delete-Definition.
2. Wenn ein Feld nicht ausgefüllt werden muss, dann null=True hinzufügen.
3. Es ist möglich choices für einige Felder zu definieren.
4. DateTimeField werden häufig mit auto_now_add=True oder auto_now=True benutzt, 
    auto_now_add fügt nur das Datum beim ersten Erstellen des Objektes hinzu, auto_now aktualisert jedes mal die Zeit bei jedem Speichervorgang.


## Django Template Syntax


 Method  | Beschreibung  | Code  |
| ------------- | ------------- | ------------- |
| extends | Template erweitert ein anderes Template, kann nur einmal verwendet werden und muss erste Zeile sein | {% extends "base.html" %} |
| include | Template fügt dein Code eines anderen Templates mit ein | {% include "sidebar.html" %} |
| if | if statement im template | {% if request.user.is_authenticated %} Welcome {% else %} Register {% endif %} |
| with | Speichert Wert/Objekt in einer variable | {% with request.user.username as username %} Hi, {{ username }}, Wie geht es dir {{ username }} {% endwith %} |
| for | For-Loop über ein Queryset | {% for user in users %} {{ user.username }} {% endfor %} |
| load | lädt Templatetags & -filter in das Template, nötig um diese zu benutzen | {% load bootstrap3 %} |


## Django Terminal Commands

base command: python3 manage.py some_command

| Command | Beschreibung  |
| ------------- | ------------- | 
| runserver | startet den server auf 127.0.0.1:8000 |
| startapp | Erstellt eine neue App |
| shell | Python-Shell mit Zugriff auf alle Modelle im Projekt | 
| makemigrations | Erstellt migration-files für die Datenbank | 
| migrate | migration-files werden ausgeführt, Datenbank wird angepasst | 
| createsuperuser | Erstellt einen Superuser, hat zugriff auf alles auf der Adminseite | 
| collectstatic | Sammelt alle static Files, und deployed sie z.B. zu Amazon  | 


## Bootstrap

| Code  | Beschreibung  | 
| ------------- | ------------- |
| col-lg-12 | 12 = 100%, 1 = 100%*1/12 |
| btn | button |
| panel | "Tafel" |
| text-center | Zentriert Text, kann auch Text färben mit text-success z.B. |
| table | Table class, häufig im Zusammenspiel mit 'table class="table borderless table-hover"' |
| hidden-xs | display:none; für Smartphones, für tablets z.B. hidden-sm |



 
