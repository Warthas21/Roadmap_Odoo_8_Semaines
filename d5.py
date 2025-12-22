"""
L'Exercice : Le Mini Point de Vente (POS)
Imagine que tu codes le module de caisse d'un magasin. Tu as des produits en stock. Le caissier doit entrer l'ID du produit et la quantité vendue.

Ton programme ne doit jamais accepter de vendre plus que le stock disponible, et ne doit jamais planter si le caissier tape n'importe quoi.

Étape 1 : La Classe Product (Le Modèle)
Crée une classe Product avec :

Attributs : name (str), price (float), stock (int).

Méthode sell(self, qty) :

Cette méthode tente de soustraire qty au stock.

Règle métier (raise) : Si la quantité demandée (qty) est supérieure au stock disponible, tu dois lever une ValueError avec le message "Stock insuffisant".

Sinon, tu diminues le stock et tu retournes le prix total de la ligne (prix * qty).

Étape 2 : Les Données
Crée une liste inventory contenant 3 objets Product (ex: "Laptop" à 1000€ stock 5, "Souris" à 20€ stock 10, etc.).

Étape 3 : L'Interface de Caisse (Le Contrôleur)
Crée une fonction start_pos(inventory) qui lance une boucle infinie :

Affiche la liste des produits (avec leur index comme ID).

Demande à l'utilisateur : "Quel produit (ID) ?" et "Combien ?".

Sécurité 1 (try/except) : Gère le cas où l'utilisateur tape du texte au lieu d'un nombre (IndexError ou ValueError).

Sécurité 2 (try/except) : Appelle la méthode sell() du produit choisi. Si le stock est insuffisant (ton raise de l'étape 1), attrape l'erreur et affiche le message sans planter.

Si la vente réussit, affiche : "Vente validée ! Montant : X€".

(Bonus) Ajoute une option pour taper "exit" et quitter la boucle.
"""

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock    

    def sell(self, qty):

        if qty > self.stock:
            raise ValueError(f"Stock insuffisant (Reste : {self.stock})")
        self.stock -= qty
        return self.price * qty
    
def start_pos(inventory):
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


product1 = Product("Laptop", 1000, 5)
product2 = Product("Souris", 20, 10)
product3 = Product("Chaise Gaming", 200, 15)
inventory = [product1, product2, product3]

start_pos(inventory)

