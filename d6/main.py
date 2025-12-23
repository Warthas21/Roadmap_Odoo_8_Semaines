from odoo_pos.models import Product, User

def start_pos(inventory, users):

    user_input = input("Qui êtes vous? (Tapez votre nom)")
    current_user = None #par defaut on ne connait personne

    for user in users:
        if user_input == user.name:
            current_user = user # On a trouvé un utilisateur de la liste
            break # plus besoin de chercher
    
    if current_user == None: # Si on a pas trouvé d'utilisateur de la liste
            print("Accès refusé !")
            return # On quitte la fonction, fin du programme
            
    # si on arrive jusqu'ici c'est donc qu'on a trouvé un utilisateur
    print(f"Bienvenue {user.name}")

    while True:
        for i, product in enumerate(inventory, start=1):
            print(f"{i}. {product.name} ({product.price}$ - Stock : {product.stock})")

        try:
            id_produit = int(input("Quel produit(ID)? (Tapez 0 pour quitter)"))
            if id_produit == 0:
                break
            selected_product = inventory[id_produit-1]
            number = int(input("Et combien?"))
            sell_price = selected_product.sell(number)
            print(f"Vente Validée! Montant : {sell_price}")
    
        except IndexError:
            print("ID invalide")
        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Bug critique : {e}")
        

user1 = User("Alex", "alex@outlook.com")
user2 = User("Turbang", "turbang@outlook.com")
list_user = [user1, user2]
#userTestError = User("", "ok@outlook.com")
product1 = Product("Laptop", 1000, 5)
product2 = Product("Souris", 20, 10)
product3 = Product("Chaise Gaming", 200, 15)
inventory = [product1, product2, product3]

start_pos(inventory, list_user)