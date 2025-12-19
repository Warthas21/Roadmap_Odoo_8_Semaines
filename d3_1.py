"""
Tu vas créer une classe Ticket qui représente une demande d'assistance. Cet exercice mélange : Classes, Méthodes, Listes, Dictionnaires et Logique conditionnelle.

Consignes :
Attributs : Chaque ticket a un id (int), un title (str), un priority (choix entre "basse", "moyenne", "haute") et un status (par défaut "nouveau").

Méthodes :

assign(self, user_name) : Change le statut en "assigné" et ajoute un attribut assigned_to.

resolve(self) : Change le statut en "résolu".

get_info(self) : Retourne un dictionnaire contenant toutes les infos du ticket.

Le défi "Senior" :
Crée une liste nommée ticket_list contenant 3 objets Ticket différents. Ensuite, crée une fonction (hors de la classe) nommée show_urgent_tickets(tickets) qui parcourt la liste et affiche uniquement les titres des tickets dont la priorité est "haute".

"""


class Ticket:
    ALLOWED_PRIORITY = {"basse", "moyenne", "haute"}

    def __init__(self, id, title, priority, status="nouveau"):
        self.id = id
        self.title = title
        if priority not in self.ALLOWED_PRIORITY:
            raise ValueError(f"priorité invalide : {priority}")
        self.priority = priority
        self.status = status
        self.assigned_to = ""
    
    def assign(self, user_name):
        if self.status != "assigné":
            self.status = "assigné"
            self.assigned_to = user_name
        else:
            print(f"Le ticket était déjà assigné à {self.assigned_to}")

    def resolve(self):
        if self.status != "résolu":
            self.status = "résolu"
    def get_info(self):
        info = {}
        info["id"] = self.id
        info["title"] = self.title
        info["priority"] = self.priority
        info["status"] = self.status
        if self.status == "assigné":
            info["assigned to"] = self.assigned_to
        return info
"""
def show_urgent_tickets(tickets):
    print("ID des tickets à haute priorité :")
    for ticket in tickets:
        if ticket.priority == "haute":
           print(f"({ticket.id})", end="")
"""

def show_urgent_tickets(tickets):
    found = False # On part du principe qu'on n'en a pas trouvé
    print("\nID des tickets à haute priorité :")
    
    for ticket in tickets:
        if ticket.priority == "haute":
            print(f"({ticket.id}) ", end="")
            found = True # On a trouvé au moins un ticket !
            
    if not found: # Si après la boucle 'found' est toujours False
        print("Aucun ticket à haute priorité.")

    
ticket1 = Ticket(1, "Need help", "haute")
print(ticket1.get_info())

ticket1.assign("Alexandre")
ticket1.assign("Turbang")
print(ticket1.get_info())
ticket1.resolve()
print(ticket1.get_info())

# defi sénior

ticket2 = Ticket(2, "idk", "basse")
ticket3 = Ticket(3, "question", "moyenne")
ticket4 = Ticket(4, "urgent", "haute")

ticket_list = [ticket1, ticket2, ticket3, ticket4]

show_urgent_tickets(ticket_list)