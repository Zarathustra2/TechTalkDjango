from django.contrib.auth.models import User

"""
    Context Processoren ermöglichen es uns Objekte/Variablen allen Templates zur Verfügung zu stellen.
    Dies ist hilfreich, wenn wir z.B. eine Navbar/Sidebar haben mit Statistiken. So müssen wir
    diese Daten nicht in jeder einzelnen View neu "queryen".
"""

"""
    Context Processoren benötigen wie eine View immer einen Parameter mitgeliefert. Egal ob wir den in
    unserer Funktion benutzen oder nicht, er muss da stehen.
    Context Processoren müssen weitergehend in unserer settings.py registriert werden:
    settings.py -> TEMPLATES - > OPTIONS -> context_processors
    
    Außerdem brauchen sie ein return statement, in dem sie den context wieder zurückgeben
    
"""


def amount_users(request):
    # count liefert uns die Anzahl der Objekte in der Datenbank
    c_users = User.objects.count()
    
    return {'amount_users': c_users}


def latest_registration(request):
    # latest gibt uns das letzte Objekt zurück, in dem Fall die 'neuste' id
    # falls es aber noch keinen User in der DB gibt, dann wird eine DoesNotExist-Exception geworfen
    try:
        l_user = User.objects.latest('id')
    except User.DoesNotExist:
        l_user = "Keine Registrationen bisher"
    
    return {'latest_user': l_user}
