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