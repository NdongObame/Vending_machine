def checker(choice):
    from Inventory import snacks
    verified = "no"
    while verified != "yes":
        try:
            choice = int(choice)
            if choice not in range(len(snacks)+1):
                print("wrong input, try again")
                choice = input("Enter a number(0-" + str(len(snacks)) + ") :")
            else:
                verified = "yes"
        except ValueError:
            print("wrong input. Try again")
            choice = input("Enter a number(0-" + str(len(snacks)) + ") :")
    return choice
