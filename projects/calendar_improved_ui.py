from datetime import datetime
import calendar
import time
import random
import math

while True:
    ch = int(input("""
╔══════════════════════════════════════╗
║      📅⏰ DATE & TIME UTILITY                  ║
╠══════════════════════════════════════╣
║ 1️⃣  Calendar Operations                                   ║
║ 2️⃣  Clock Operations                                       ║
║ 3️⃣  Exit                                                        ║
╚══════════════════════════════════════╝
👉 Enter Choice: """))
    match ch:
        case 1:
            print("\n📅 Calendar Operations Selected")
            print("""
╔══════════════════════════════════════╗
║         📅 CALENDAR MENU                        ║
╚══════════════════════════════════════╝""")
            print("1.find the day of entered date.")
            print("2.✅ DATE VALIDATOR ")
            print("3.Days Between Two Dates.")
            print("4.Leap Year Checker")
            print("5.Age Calculator")
            print("6.Day Number in Year")
            print("7.Month Calendar")
            print("8.Week Number")
            print("9.back")

            while True:
                ch1 = int(input("👉 Enter Choice: "))
                match ch1:
                    case 1:
                        dnum = input("📅 Enter Date (DD/MM/YYYY): ")
                        d = datetime.strptime(dnum, "%d/%m/%Y")
                        print("day is ", d)
                    case 2:
                        print("✅ DATE VALIDATOR")
                        d2 = input("📅 Enter Date (DD/MM/YYYY): ")
                        try:
                            d = datetime.strptime(d2, "%d/%m/%Y")
                            print("✅ Valid Date")
                        except ValueError:
                            print("❌ Invalid Date")
                    case 3:
                        d1 = input("📅 First Date (DD/MM/YYYY): ")
                        d2 = input("📅 Second Date (DD/MM/YYYY): ")
                        d1 = datetime.strptime(d1, "%d/%m/%Y")
                        d2 = datetime.strptime(d2, "%d/%m/%Y")
                        diff = abs((d2 - d1).days)
                        print("📆 Days Between Dates:", diff)
                    case 4:
                        year = int(input("📅 Enter Year: "))
                        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                            print(year, "✅ is a Leap Year.")
                        else:
                            print(year, "❌ is not a Leap Year.")
                    case 5:
                        birthdate = input("🎂 Enter Birth Date (DD/MM/YYYY): ")
                        birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
                        today = datetime.now()
                        age = today.year - birthdate.year - (
                            (today.month, today.day) < (birthdate.month, birthdate.day)
                        )
                        print("🎉 Your Age:", age)
                    case 6:
                        date_input = input("📅 Enter Date (DD/MM/YYYY): ")
                        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
                        day_of_year = date_obj.timetuple().tm_yday
                        print("📌 Day Number:", day_of_year)
                    case 7:
                        year = int(input("📅 Enter Year: "))
                        month = int(input("📅 Enter Month (1-12): "))
                        print(calendar.month(year, month))
                    case 8:
                        date_input = input("📅 Enter Date (DD/MM/YYYY): ")
                        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
                        week_number = date_obj.isocalendar()[1]
                        print("📅 Week Number:", week_number)
                    case 9:
                        print("🔙 Returning to Main Menu...")
                        break
                    case _:
                        print("❌ Invalid Choice")
        case 2:
            print("\n⏰ Clock Operations Selected")
            print("""
╔══════════════════════════════════════╗
║           ⏰ CLOCK MENU                         ║
╚══════════════════════════════════════╝""")
            print("1.🕒 Current Time")
            print("2.🕒 Digital Clock ")
            print("3.Stopwatch")
            print("4.⏳ Countdown Timer")
            print("5.Back")
            while True:
                ch2 = int(input("enter choice: "))
                match ch2:
                    case 1:
                        today = datetime.now()
                        print(today.time())
                    case 2:
                        print("🕒 Digital Clock")
                        try:
                            while True:
                                today = datetime.now()
                                print(f"\r{today.strftime('%I:%M:%S %p')}", end="")
                                time.sleep(1)
                        except KeyboardInterrupt:
                            print("\n🛑 Clock Stopped")
                    case 3:
                        input("⏱️ Press Enter to Start Stopwatch...")
                        start = time.time()
                        try:
                            while True:
                                current = time.time()
                                elapsed = int(current - start)
                                hours = elapsed // 3600
                                remain = elapsed % 3600
                                minutes = remain // 60
                                seconds = remain % 60
                                print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="  ")
                                time.sleep(1)
                        except KeyboardInterrupt:
                            print("\n🛑 Stopwatch Stopped")
                    case 4:
                        print("⏳ Countdown Timer")
                        second = int(input("⏳ Enter Time (seconds): "))
                        while second:
                            mins, secs = divmod(second, 60)
                            timer = "{:02d}:{:02d}".format(mins, secs)
                            print(timer, end="\r")
                            time.sleep(1)
                            second -= 1
                    case 5:
                        print("🔙 Returning to Main Menu...")
                        break
                    case _:
                        print("❌ Invalid Choice")
        case _:
            break