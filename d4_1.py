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

def show_urgent_tickets(tickets):
    found = False # On part du principe qu'on n'en a pas trouvé
    print("\nID des tickets à haute priorité :")
    
    for ticket in tickets:
        if ticket.priority == "haute":
            print(f"({ticket.id}) ", end="")
            found = True # On a trouvé au moins un ticket !
            
    if not found: # Si après la boucle 'found' est toujours False
        print("Aucun ticket à haute priorité.")


def create_ticket():
    while True:
        try:
            id = input("ID du ticket: ")
            title = input("Titre du ticket: ")
            priority = input("Priorité du ticket: (basse/moyenne/haute)")

            ticket = Ticket(id, title, priority)
            print("Succès : Ticket créé !")

            return ticket
        except ValueError as e:
            print(f"Erreur de saisie : {e} ")
        except Exception as e:
            print(f"Erreur Critique: {e}")
            break # on break pour sortir de la boucle ici parce que erreur critique, pas de sens de continuer
            
    
ticket1 = create_ticket()
