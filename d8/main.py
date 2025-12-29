from odoo_pos.models import Product, User, Manager
import json

def save_users(users):
    users_to_save = []

    for user in users:
        users_to_save.append(user.to_dict())

    with open('users.json', 'w') as f:
        json.dump(users_to_save, f)

def load_users():
    loaded_users = []
    try:
        with open('users.json', 'r') as f:
            content = json.load(f)
            for item in content:
                if item.get("role") == "manager":
                    new_user = Manager(item['name'], item['email'])
                else:
                    new_user = User(item['name'], item['email'])
                loaded_users.append(new_user)
        return loaded_users
    except FileNotFoundError:
        return loaded_users

def save_data(inventory):
    data_to_save = []

    for produit in inventory:
        data_to_save.append(produit.to_dict())

    with open('products.json', 'w') as f:
        json.dump(data_to_save, f)


def load_data():
    loaded_inventory = []
    try:
        with open('products.json', 'r') as f:
            content = json.load(f)
            for item in content:
                new_product = Product(item['name'], item['price'], item['stock'])
                loaded_inventory.append(new_product)
        return loaded_inventory
    except FileNotFoundError:
        return loaded_inventory

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

    if isinstance(current_user, Manager): #isinstance vérifie le type. -> if current_user is manager = true
        print("MODE ADMINISTRATEUR ACTIVÉ")

    while True:
        for i, product in enumerate(inventory, start=1):
            print(f"{i}. {product.name} ({product.price}$ - Stock : {product.stock})")

        try:
            id_produit = int(input("Quel produit(ID)? (0 = Quitter, 99=Restock)"))
            if id_produit == 0:
                save_data(inventory)
                save_users(users)
                break
            elif id_produit == 99:
                if isinstance(current_user, Manager):
                    id_stock = int(input("Quel produit voulez-vous réapprovisionner (ID) ? "))
                    qty_stock = int(input("Combien d'unités ajouter ? "))
                    
                    product_to_restock = inventory[id_stock - 1]
                    
                    # On utilise la méthode spéciale du Manager
                    current_user.restock(product_to_restock, qty_stock)
                else:
                    print("Acces refusé : Vous n'étes pas Manager.")
            else:
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
        

inventory = load_data()

if len(inventory) == 0:
    print("Aucun fichier Produits de sauvegarde trouvé. Chargement des données par défaut...")
    p1 = Product("Laptop", 1000, 5)
    p2 = Product("Souris", 20, 10)
    p3 = Product("Chaise Gaming", 200, 15)
    inventory = [p1, p2, p3]
    # On sauvegarde tout de suite pour créer le fichier
    save_data(inventory)

list_user = load_users()

if len(list_user) == 0:
    print("Aucun fichier Utilisateurs de sauvegarde trouvé. Chargement des données par défaut...")
    u1 = User("Alex", "alex@outlook.com")
    u2 = User("Turbang", "turbang@outlook.com")
    u3_admin = Manager("Admin", "admin@outlook.com")
    list_user = [u1, u2, u3_admin]

    save_users(list_user)

start_pos(inventory, list_user)
