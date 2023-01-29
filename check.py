def checker(choice):
    from Goods import snacks
    verified = "no"
    while verified != "yes":
        try:
            choice = int(choice)
            verified = "yes"
        except ValueError:
            print("wrong input, try again")
            choice = input("Enter a number(0-" + str(len(snacks)) + ") :")
    while choice not in range(len(snacks)):
        print("wrong input, try again")
        choice = input("Enter a number(0-" + str(len(snacks)) + ") :")
    return choice
