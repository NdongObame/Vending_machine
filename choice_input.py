def Snacks(treats, receipt, t):
    from input_check import checker
    from totals import total
    from Inventory import snacks
    print("\nwhich snacks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(snacks)) + "):")
    total(checker(choice), treats, receipt, t)


def Drinks(treats, receipt, t):
    from input_check import checker
    from totals import total
    from Inventory import drinks
    print("\nwhich drinks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(drinks)) + "):")
    total(checker(choice), treats, receipt, t)


def Sweets(treats, receipt, t):
    from input_check import checker
    from totals import total
    from Inventory import sweets
    print("\nwhich drinks do you prefer ?")
    choice = input("Enter a number(0-" + str(len(sweets)) + "):")
    total(checker(choice), treats, receipt, t)
