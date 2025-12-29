class User:
    def __init__(self, name, email):
        if name == "":
            raise ValueError("Pas de nom d'utilisateur")
        self.name = name
        self.email = email
        self.is_active = True

    def display_info(self):
        print(f"Utilisateur : [{self.name}] ([{self.email}]) ", end="")
        if self.is_active:
            print("(Active)")
        else:
            print("(Inactive)")

    def change_email(self, new_email):
        self.email = new_email
        print("L'email a été modifié")

    def deactivate(self):
        if self.is_active:
            self.is_active = False

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "role" : "user"
        }
