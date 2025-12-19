class User:
    def __init__(self, name, email):
        # Initialise les attributs ici
        self.name = name
        self.email = email
        self.is_active = True

    def display_info(self):
        # MISSION : Affiche "Utilisateur : [Nom] ([Email])"
        # Utilise f-string et self.name / self.email
        print(f"Utilisateur : [{self.name}] ([{self.email}]) ", end="")
        if self.is_active:
            print("(Active)")
        else:
            print("(Inactive)")
        pass

    def change_email(self, new_email):
        # MISSION : Remplace l'ancien email par le nouveau
        # Affiche un message de confirmation
        self.email = new_email
        print("L'email a été modifié")
        pass

    def deactivate(self):
        if self.is_active:
            self.is_active = False
        else:
            pass

# --- TEST ---
# 1. Crée un objet nommé 'user1' pour Alice (alice@odoo.com)
# 2. Appelle display_info()
# 3. Change son email pour 'alice.new@odoo.com'
# 4. Appelle display_info() à nouveau pour vérifier

user1 = User("Alice", "alice@odoo.com")

user1.display_info()
user1.change_email("alice.new@odoo.com")
user1.deactivate()
user1.display_info()



#Ajoute une méthode deactivate à ta classe User.

#Cette méthode doit passer self.is_active à False.

#Modifie display_info pour qu'il affiche (Actif) ou (Inactif) à côté du nom de l'utilisateur en fonction de cet attribut.