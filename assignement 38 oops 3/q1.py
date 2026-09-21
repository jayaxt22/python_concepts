

class bankaccount:
    def __init__(self,
                 account_number,
                 customer_name,
                 account_balance):

        self.account_number=account_number
        self.customer_name=customer_name
        self.account_balance=account_balance
        self.d_amount=0
        self.t_amount=0
        self.w_amount=0

    bank_name="IDBI Bank"
    interest_rate=10

    def deposit(self, amount):
        self.account_balance+=amount
        return self.account_balance
        
    def withdraw(self,w_amount):
        self.account_balance-=w_amount
        return self.account_balance


        

    def transfer_money(self,receiver, t_amount):
        receiver.account_balance+=t_amount
        self.account_balance-=t_amount
        return self.account_balance
        
    
    def display_balance(self):
        print("------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Balance        :", self.account_balance)



    @classmethod

    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
        return cls.interest_rate
    
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        return cls.bank_name
    
    @classmethod

    def display_bank_info(cls):
        print("------ Bank Information ------")
        print("Bank Name     :", cls.bank_name)
        print("Interest Rate :", cls.interest_rate, "%")




    @staticmethod

    def validate_account_number(account_number):
        if 10000>account_number >0:
            return "valid"
        else:
            return "invalid"

    @staticmethod
    def calculate_interest(amount ,interest_rate):
        interest=(amount*interest_rate)/100
        return interest
    @staticmethod
    def generate_transaction_id():
        return "TXN1025"

c1=bankaccount(8152,"deepika",150000)
c2=bankaccount(5656,"priya",250000)
print("account number validation check:",bankaccount.validate_account_number(8152))
print("account number validation check:",bankaccount.validate_account_number(5656))


c1.display_balance()
c2.display_balance()

print()
print("deposit amount:",15000)
print("balance after Deposit :", c1.deposit(15000))
c1.display_balance()

print()

print("Withdrawal Amount :", 5000)
print("Balance After Withdrawal :", c1.withdraw(5000))
c1.display_balance()

print()

print("Transfer Amount :", 5000)
print("Balance After Transfer :", c1.transfer_money(c2, 5000))
print("transaction ID:",bankaccount.generate_transaction_id())
print()
c1.display_balance()
c2.display_balance()

print()

bankaccount.display_bank_info()
print()
print("new name for bank:","HDFC bank")
bankaccount.change_bank_name("HDFC Bank")
print("new interst rate:",7.5)
bankaccount.change_interest_rate(7.5)
bankaccount.display_bank_info()
print()
print(f"calculate interest rate for amount {75000} on interest rate of {bankaccount.interest_rate}%")
print("interest amount:",bankaccount.calculate_interest(75000,bankaccount.interest_rate))





        