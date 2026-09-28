class Account:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount>0:
            self.__balance=amount
        
    @balance.deleter
    def balance(self):
        del self.__balance
    
    def display_account(self):
        print()
        print(f"Account Number : {self.account_number}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Balance        : {self.balance}")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        self.balance=self.balance-amount


class SavingsAccount(Account):

    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number,customer_name,balance)
        self.interest_rate = interest_rate

    def display_account(self):
        super().display_account()
        print(f"Interest Rate  : {self.interest_rate}")



class PremiumSavingsAccount(SavingsAccount):
    
    def __init__(self, account_number, customer_name, balance, interest_rate,cashback_percent):
        super().__init__(account_number, customer_name, balance, interest_rate)
        self.cashback_percent=cashback_percent

    def display_account(self):
        super().display_account()
        print(f"CashBack Percentage : {self.cashback_percent}")