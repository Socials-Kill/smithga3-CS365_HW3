value = input("Please enter a year:\n")

if (int(value) % 4 == 0):
    if (int(value) % 100 == 0):
        if (int(value) % 400 == 0):
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")
