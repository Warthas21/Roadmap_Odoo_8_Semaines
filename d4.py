def calculate_unit_price(total_amount, quantity):
    try:
        # MISSION : Convertis les entrées en float pour être sûr
        # MISSION : Calcule le prix unitaire (total / quantité)
        price = float(total_amount) / float(quantity)
        return price
    except ZeroDivisionError:
        # Que faire si la quantité est 0 ?
        return "Erreur : La quantité ne peut pas être nulle."
    except ValueError:
        # Que faire si l'utilisateur écrit "dix" au lieu de 10 ?
        return "Erreur : Veuillez entrer des chiffres valides."
    except Exception as e:
        # Le filet de sécurité final pour les erreurs imprévues
        return f"Une erreur inattendue est survenue : {e}"

# --- TESTS ---
print(calculate_unit_price(100, 5))    # Cas normal : 20.0
print(calculate_unit_price(100, 0))    # Cas critique : division par zéro
print(calculate_unit_price("cent", 5)) # Cas critique : mauvais type