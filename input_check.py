def checker(choice,treats):
    from Inventory import inventory
    verified = "no"
    while verified != "yes":
        try:
            choice = int(choice)
            if choice not in range(len(inventory[treats])+1):
                print("wrong input, try again")
                choice = input("Enter a number(0-" + str(len(inventory[treats])) + ") :")
            else:
                verified = "yes"
        except ValueError:
            print("wrong input. Try again")
            choice = input("Enter a number(0-" + str(len(inventory[treats])) + ") :")
    return choice
