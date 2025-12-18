


orders = [
    {'id': 1, 'customer': 'Alice', 'amount': 150, 'status': 'draft'},
    {'id': 2, 'customer': 'Bob', 'amount': 450, 'status': 'confirmed'},
    {'id': 3, 'customer': 'Charlie', 'amount': 50, 'status': 'confirmed'},
    {'id': 4, 'customer': 'Alice', 'amount': 200, 'status': 'cancelled'},
]

orders.append({'id': 5, 'customer': 'Eve', 'status': 'confirmed'}) # Pas de 'amount' !

confirmed_ids = []
confirmed_ids = [order['id'] for order in orders if order['status'] == "confirmed"]


total_confirmed = 0
for order in orders:
    if order['status'] == "confirmed":
        total_confirmed += order.get('amount', 0)

# Version "Senior" en une ligne
total_confirmed = sum(order.get('amount', 0) for order in orders if order.get('status') == 'confirmed')


customer_count = {}
for order in orders:
    name = order['customer']
    if name in customer_count:
        customer_count[name] += 1
    else:
        customer_count[name] = 1

print(f"IDs confirmés: {confirmed_ids}")
print(f"Total financier: {total_confirmed}")
print(f"Stats clients: {customer_count}")

