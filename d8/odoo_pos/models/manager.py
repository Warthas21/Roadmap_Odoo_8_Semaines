from .user import User

class Manager(User):
    def restock(self, product, qty):
        product.stock += qty
        print(f"Stock mis à jour ! : + {qty} à {product.name} ")

    def to_dict(self):
        data = super().to_dict() # On récupère le dict du parent
        data["role"] = "manager" # On change juste le rôle
        return data