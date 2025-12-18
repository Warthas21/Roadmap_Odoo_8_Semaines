def get_total_by_status(order_list, status_name):
    """
    Retourne la somme des montants pour un statut spécifique.
    """

    total_by_status = sum(order.get('amount', 0) for order in order_list if order.get('status') == status_name)
    return total_by_status


orders = [
    {'id': 1, 'customer': 'Alice', 'amount': 100, 'status': 'confirmed'},
    {'id': 2, 'customer': 'Bob', 'amount': 200, 'status': 'draft'},
    {'id': 3, 'customer': 'Charlie', 'amount': 50, 'status': 'confirmed'},
]


print(f"Total Confirmé : {get_total_by_status(orders, 'confirmed')}")


