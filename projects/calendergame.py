from datetime import datetime
import calendar
import time
import random
import math
today= datetime.now()
while True:
    ch=int(input("========WELCOME========\n1: press 1 for calender related calculations.\n2: press 2 fro clock related operations\nenter choice: "))
    match ch:
        case 1:
            print("you have chosen calender related operation")
            print("\n========== MENU =============")
            print("1.find the day of entered date.")
            print("2.Date Validator ")
            print("3.Days Between Two Dates.")
            print("4.Leap Year Checker")
            print("5.Age Calculator")
            print("6.Day Number in Year")
            print("7.Month Calendar")
            print("8.Week Number")
            print("9.back")
            
            while True:
                ch1= int(input("enter your choice: "))
                match ch1:
                    case 1:
                       dnum=input("Enter the date (DD/MM/YYYY)to know the day:")
                       d = datetime.strptime(dnum,"%d/%m/%Y")
                       print("day is ",d)
                    case 2:
                       print("Date Validator")
                       d2=input("Enter the date (DD/MM/YYYY)")
                       try:
                            d = datetime.strptime(d2,"%d/%m/%Y")
                            print("valid date") 
                       except ValueError:
                            print("invalid date")
                    case 3:
                          d1=input("Enter the first date (DD/MM/YYYY): ")
                          d2=input("Enter the second date (DD/MM/YYYY): ")
                          d1 = datetime.strptime(d1,"%d/%m/%Y")
                          d2 = datetime.strptime(d2,"%d/%m/%Y")
                          diff = abs((d2 - d1).days)
                          print("Days between two dates:", diff)
                    case 4:
                          year = int(input("Enter the year to check if it's a leap year: "))
                          if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                                print(year, "is a leap year.")
                          else: 
                                print(year, "is not a leap year.")  
                    case 5:
                            birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
                            birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
                            today = datetime.now()
                            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                            print("Your age is:", age) 
                    case 6:
                            date_input = input("Enter a date (DD/MM/YYYY): ")
                            date_obj = datetime.strptime(date_input, "%d/%m/%Y")
                            day_of_year = date_obj.timetuple().tm_yday
                            print("Day number in the year:", day_of_year)
                    case 7:
                            year = int(input("Enter the year: "))
                            month = int(input("Enter the month (1-12): "))
                            print(calendar.month(year, month))
                            pass                          
                    case 8:
                            date_input = input("Enter a date (DD/MM/YYYY): ")
                            date_obj = datetime.strptime(date_input, "%d/%m/%Y")
                            week_number = date_obj.isocalendar()[1]
                            print("Week number in the year:", week_number)
                            pass
                    case 9:
                       print("back to main menu")
                       break
                    case _:
                          print("invalid choice") 
        case 2:
            print("you have chosen clock related operations...")
            
            print("\n===== MENU =====")
            print("1.Current Time")
            print("2.Digital Clock ")
            print("3.Stopwatch")
            print("4.Countdown Timer")
            print("5.Alarm Clock")
            print("6.Time Difference")
            print("7.World Clock")
            print("8.Back")
            while True:
                ch2=int(input("enter choice: "))
                match ch2:
                    case 1:
                        print(today.time())
                    case 2:
                        print()
                    case 3:
                        press = input("press")
                    case 4:
                        print("")
                    case 5:
                        print("")
                    case 6:
                        print("")
                    case 7:
                        print("")
                    case 8:
                        print("back to main menu")
                        break
                    case _:
                        print("invalid choice")                        
        case _:
            break
                