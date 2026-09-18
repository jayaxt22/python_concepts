class ElectricityBill:

    def __init__(self, consumer_number, consumer_name, units_consumed,
                 rate_per_unit, fixed_charge):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed
        self.rate_per_unit = rate_per_unit
        self.fixed_charge = fixed_charge
        self.final_bill=0
        self.total_bill=0

    def calculate_energy_charge(self):
        self.final_bill=self.units_consumed*self.rate_per_unit
        return self.final_bill

    def calculate_total_bill(self):
        self.total_bill=self.fixed_charge+self.final_bill
        return self.total_bill

    def display_bill(self):
        print("============ bill ============")
        print("consumer number      :",self.consumer_number)
        print("consumer name        :",self.consumer_name  )   
        print("unit consumed        :",self.units_consumed )  
        print("rate per unit        :",self.rate_per_unit  ) 
        print("fixed charge         :",self.fixed_charge   )
        print()
        print("TOTAL bill           :",self.total_bill)
        print()
        print("============================================")
        # Display total bill
        


# Create object
bill = ElectricityBill(501, "Amit", 250, 6, 100)

# Call display method
bill.calculate_energy_charge()
bill.calculate_total_bill()
bill.display_bill()