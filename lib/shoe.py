class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        self.in_stock = True  
        self.condition = "New"  # Initialize condition

    def sell(self):
        self.in_stock = False

    def restock(self):
        self.in_stock = True

    def cobble(self):
        print("Your shoe is as good as new!")  # Print message when cobbling
        self.condition = "New"  # Set condition to "New"

    def __str__(self):
        return f"{self.brand} shoe, Size: {self.size}, Color: {self.color}. In stock: {self.in_stock}"