class MobilePlan:

    def __init__(self, customer_name, mobile_number, total_data,
                 used_data, validity):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.total_data = total_data
        self.used_data = used_data
        self.validity = validity
        self.remain_data=0
        self.usage_percentage=0


    def calculate_remaining_data(self):
        self.remain_data=self.total_data-self.used_data
        return self.remain_data

    def calculate_usage_percentage(self):
        self.usage_percentage=(self.used_data / self.total_data) * 100
        return self.usage_percentage

    def display_plan(self):
        print("customer name     :",self.customer_name)
        print("mobile number     :",self.mobile_number)
        print("total data        :",self.total_data)
        print("used data         :",self.used_data)
        print("validity          :",self.validity)
        print("remaining data    :",self.remain_data)
        print("usage percentage  :",self.usage_percentage,"%") 
        


# Create object
plan = MobilePlan("Amit", "9866284285", 50, 18, 28)

plan.calculate_remaining_data()
plan.calculate_usage_percentage()
plan.display_plan()