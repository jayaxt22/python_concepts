mode = int(input("Enter mode: "))

if mode == 1:
    current = int(input())
    destination = int(input())

    while current <= destination:
        print(current, end=" ")
        current += 1

elif mode == 2:
    current = int(input())
    destination = int(input())

    while current >= destination:
        print(current, end=" ")
        current -= 1

elif mode == 3:
    destination = int(input())

    floor = 0

    while floor <= destination:
        print(floor, end=" ")
        floor += 2

else:
    count = 1

    while count <= 4:
        print("Emergency Alarm")
        count += 1