class Guest:

    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_days = number_of_days
        self.room_charge_per_day = room_charge_per_day

    def calculate_room_bill(self):
        return self.number_of_days * self.room_charge_per_day

    def calculate_gst(self):
        return self.calculate_room_bill() * 0.12

    def calculate_final_bill(self):
        return self.calculate_room_bill() + self.calculate_gst()

    def display_bill(self):
        print("------ Hotel Bill ------")
        print("Guest ID              :", self.guest_id)
        print("Guest Name            :", self.guest_name)
        print("Number of Days        :", self.number_of_days)
        print("Room Charge Per Day   : ₹" + str(self.room_charge_per_day))
        print("Room Bill             : ₹" + str(self.calculate_room_bill()))
        print("GST (12%)             : ₹" + str(self.calculate_gst()))
        print("Final Bill            : ₹" + str(self.calculate_final_bill()))


guest_id = input("Enter Guest ID : ")
guest_name = input("Enter Guest Name : ")
number_of_days = int(input("Enter Number of Days : "))
room_charge_per_day = float(input("Enter Room Charge Per Day : "))

guest = Guest(guest_id, guest_name, number_of_days, room_charge_per_day)
guest.display_bill()