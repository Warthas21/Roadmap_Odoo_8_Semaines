"""
Écris une fonction calculate_inventory_value(stock_list, category_name).

Elle doit parcourir la liste.

Si la catégorie correspond à category_name, elle calcule : prix * quantité.

Attention : Si la quantity est manquante, utilise 0 par défaut pour éviter que le calcul ne plante.

Elle doit retourner la somme totale pour cette catégorie.
"""

def calculate_inventory_value(stock_list, category_name):
    somme_total = 0

    for item in stock_list:
        category = item['category']
        quantity = item.get('quantity', 0)
        price = item['price']
        if category == category_name:
            somme_total += price * quantity
    return somme_total




stock_items = [
    {'name': 'Clavier', 'price': 50, 'quantity': 10, 'category': 'IT'},
    {'name': 'Souris', 'price': 20, 'quantity': 5, 'category': 'IT'},
    {'name': 'Bureau', 'price': 200, 'category': 'Meuble'}, # Pas de quantité ici !
    {'name': 'Chaise', 'price': 150, 'quantity': 2, 'category': 'Meuble'},
]


print(calculate_inventory_value(stock_items, 'IT'))
print(calculate_inventory_value(stock_items, 'Meuble'))
