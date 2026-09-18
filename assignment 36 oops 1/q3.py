class bankaccount:
    def __init__(self,acc_number,h_name,open_balance,depsit,withdrw):
      
       self.acc_number=acc_number
       self.h_name=h_name
       self.open_balance=open_balance
       self.depsit=depsit
       self.withdrw=withdrw
       self.final_balance=0
       

    def deposit(self):
        self.open_balance=self.open_balance+self.depsit
        return self.open_balance


    def withdraw(self):
        self.final_balance=self.open_balance-self.withdrw
        return self.final_balance



    def display(self):
        print("=============== account details ============")
        print("Account number            :",self.acc_number)
        print("holder name               :",self.h_name)
        print("opening balance           :",self.open_balance)
        print("deposit amount            :",self.depsit)
        print("withdrawn amount          :",self.withdrw)
        print("====================== END =======================")
        print()
        print("final balance             :",self.final_balance)
        print()

E1 = bankaccount(12,"rahul",25000,10000,5000)

E1.deposit()
E1.withdraw()
E1.display()
