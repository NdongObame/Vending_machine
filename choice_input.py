def Choosing(treats, receipt, t):
    from input_check import checker
    from totals import total
    from Inventory import inventory
    print("\nwhich one do you prefer ?")
    choice = input("Enter a number(0-" + str(len(inventory[treats])) + "):")
    total(checker(choice, treats), treats, receipt, t)
