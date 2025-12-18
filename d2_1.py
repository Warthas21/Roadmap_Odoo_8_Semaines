# Résultat attendu avec tes données :
# {'Alice': 100, 'Bob': 200, 'Charlie': 50}

def get_customer_report(order_list):

    report = {}

    for order in order_list:
        customer = order['customer']
        amount = order.get('amount', 0)
    
        if customer in report:
            report[customer] += amount
            pass 
        else:
            report[customer] = amount
            pass

    return report

# --- ZONE DE TEST ---
orders = [
    {'customer': 'Alice', 'amount': 100},
    {'customer': 'Bob', 'amount': 200},
    {'customer': 'Alice', 'amount': 50},
]
# Résultat attendu : {'Alice': 150, 'Bob': 200}
print(get_customer_report(orders))


