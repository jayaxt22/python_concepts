class Product:

    def __init__(self, product_id, product_name, quantity, price_per_item):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item

    def calculate_total_amount(self):
        return self.quantity * self.price_per_item

    def calculate_discount(self):
        total_amount = self.calculate_total_amount()

        if total_amount > 5000:
            return total_amount * 0.10
        else:
            return total_amount * 0.05

    def calculate_final_amount(self):
        return self.calculate_total_amount() - self.calculate_discount()

    def display_bill(self):
        print("------ Shopping Bill ------")
        print("Product ID        :", self.product_id)
        print("Product Name      :", self.product_name)
        print("Quantity          :", self.quantity)
        print("Price Per Item    :", self.price_per_item)
        print("Total Amount      : ₹" + str(self.calculate_total_amount()))
        print("Discount          : ₹" + str(self.calculate_discount()))
        print("Final Amount      : ₹" + str(self.calculate_final_amount()))


product_id = input("Enter Product ID : ")
product_name = input("Enter Product Name : ")
quantity = int(input("Enter Quantity : "))
price_per_item = float(input("Enter Price Per Item : "))

product = Product(product_id, product_name, quantity, price_per_item)
product.display_bill()