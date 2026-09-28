from models.Account import Account, SavingsAccount, PremiumSavingsAccount

from rich.prompt import Prompt


account_num=int(input("Enter The Account No.    : "))
customer_name=input("Enter The Account Holder : ")
balance=int(input("Enter The Balance    : "))

choice = Prompt.ask(
    "Choose Account Type",
    choices=["Saving Account", "Premium Saving Account"]
)




if choice=="Saving Account":
    interest_rate=int(input("Enter Interest Rate  :"))
    c1=SavingsAccount(account_num,customer_name,balance,interest_rate)
    c1.display_account()

    print()

    print("After Deposit")
    c1.deposit(5000)
    c1.display_account()

    print()

    print("After Withdraw")
    c1.withdraw(1000)
    c1.display_account()

else:
    interest_rate=int(input("Enter Interest Rate  :"))
    cashback_percentage=int(input("Enter CashBack Percentage : "))
    p1=PremiumSavingsAccount(account_num,customer_name,balance,interest_rate,cashback_percentage)
    p1.display_account()

    print("After Deposit")
    p1.deposit(5000)
    p1.display_account()

    print("After Withdraw")
    p1.withdraw(1000)
    p1.display_account()

