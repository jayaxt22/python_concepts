# 1. Positional Arguments

def customer_registration(name, email, mobile):

    print("\nCustomer Registered Successfully")

    print("Name   :", name)
    print("Email  :", email)
    print("Mobile :", mobile)


# 2. Keyword Arguments

def product_information(product_name, price, category):

    print("\nProduct Details Displayed Successfully")

    print("Product Name :", product_name)
    print("Price        :", price)
    print("Category     :", category)


# 3. Default Arguments

def generate_invoice(product_name, price, tax=18):

    tax_amount = price * tax / 100
    final_amount = price + tax_amount

    print("\nInvoice Generated Successfully")

    print("Product Name :", product_name)
    print("Price        :", price)
    print("Tax          :", tax, "%")
    print("Tax Amount   :", tax_amount)
    print("Final Amount :", final_amount)


# 4. Variable Length Arguments

def add_multiple_products(*prices):

    total = 0

    for price in prices:
        total = total + price

    return total


# 5. Arbitrary Keyword Arguments

def display_customer_profile(**details):

    print("\nCustomer Profile Displayed Successfully\n")

    for key, value in details.items():
        print(key, ":", value)


# Main Program

while True:

    print("\n*** ONLINE SHOPPING SYSTEM ***")
    print("1. Customer Registration")
    print("2. Product Information")
    print("3. Generate Invoice")
    print("4. Add Multiple Products")
    print("5. Display Customer Profile")
    print("6. Exit")

    choice = int(input("\nEnter Choice: "))

    # Choice 1 - Positional Arguments

    if choice == 1:

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")

        customer_registration(name, email, mobile)


    # Choice 2 - Keyword Arguments

    elif choice == 2:

        product_name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")

        product_information(
            product_name=product_name,
            price=price,
            category=category
        )


    # Choice 3 - Default Arguments

    elif choice == 3:

        product_name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))

        generate_invoice(product_name, price)


    # Choice 4 - Variable Length Arguments

    elif choice == 4:

        number = int(input("Enter Number of Products: "))

        prices = []

        for i in range(number):

            price = float(input(f"Enter Price {i + 1}: "))
            prices.append(price)

        total = add_multiple_products(*prices)

        print("Total Bill Amount:", total)


    # Choice 5 - Arbitrary Keyword Arguments

    elif choice == 5:

        name = input("Enter Name: ")
        city = input("Enter City: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        membership = input("Enter Membership Type: ")

        display_customer_profile(
            Name=name,
            City=city,
            Email=email,
            Mobile=mobile,
            Membership_Type=membership
        )


    # Choice 6 - Exit

    elif choice == 6:

        print("Thank You. Program Terminated.")
        break


    else:

        print("Invalid Choice!")