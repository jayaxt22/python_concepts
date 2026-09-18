class Customer:

    def __init__(self, customer_id, customer_name, units_consumed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        return (self.units_consumed * 8) + 150

    def display_bill(self):
        print("------ Electricity Bill ------")
        print("Customer ID       :", self.customer_id)
        print("Customer Name     :", self.customer_name)
        print("Units Consumed    :", self.units_consumed)
        print("Total Bill Amount : ₹" + str(self.calculate_bill()))


customer_id = input("Enter Customer ID : ")
customer_name = input("Enter Customer Name : ")
units_consumed = int(input("Enter Units Consumed : "))

customer = Customer(customer_id, customer_name, units_consumed)
customer.display_bill()