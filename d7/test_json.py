import json

produits = [
    {"name": "Laptop", "price": 1000},
    {"name": "Souris", "price": 50},
    {"name": "Chaise Gaming", "price": 200}
]


# ÉCRITURE (Mode 'w' pour Write)
with open('test_stock.json', 'w') as f:
    json.dump(produits, f) # dump = décharger dans le fichier

# LECTURE (Mode 'r' pour Read)
with open('test_stock.json', 'r') as f:
    content = json.load(f) # load = charger depuis le fichier
    for produit in content:
        print(produit['name'])