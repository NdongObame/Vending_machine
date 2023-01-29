def Snacks():
    from check import checker
    from totals import total
    from Goods import snacks
    print("\nwhich snacks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(snacks)) + "):")
    num = checker(choice)
    total(num)


def Drinks():
    from check import checker
    from totals import total
    from Goods import drinks
    print("\nwhich drinks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(drinks)) + "):")
    num = checker(choice)
    total(num)


def Sweets():
    from check import checker
    from totals import total
    from Goods import sweets
    print("\nwhich drinks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(sweets)) + "):")
    num = checker(choice)
    total(num)
