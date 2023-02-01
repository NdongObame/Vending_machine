def total(choice, treats, receipt, t):
    from Inventory import inventory

    choice -= 1

    if choice >= 0:
        receipt.append(inventory[treats][choice])
        for X in receipt:
            t += X[1]
        print("total :" + str(round(t, 2)))
