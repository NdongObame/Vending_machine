def total(choice, treats, receipt, t):
    from Inventory import snacks, drinks, sweets
    
    inventory = { "1": snacks, "2": drinks, "3": sweets }
    
    choice -= 1

    if choice >= 0:
        receipt.append(inventory[treats][choice])
        for X in receipt:
            t += X[1]
        print("total :" + str(round(t,2)))

