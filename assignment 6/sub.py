sub = input("Subscription: ")
progress = int(input("Progress: "))
score = int(input("Test Score: "))

if sub == "premium":
    if progress >= 80:
        if score >= 70:
            print("Access Status = Certificate Unlocked")
        else:
            print("Access Status = Retry Test")
    else:
        print("Access Status = Complete Course")
elif sub == "basic":
    if progress >= 50:
        print("Access Status = Limited Access")
    else:
        print("Access Status = Content Locked")
else:
    print("Access Status = Denied")