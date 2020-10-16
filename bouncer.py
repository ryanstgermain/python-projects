age = input("Enter you age: ")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink.")
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You are too young to enter.")
else:
    print("Please enter an age.")

