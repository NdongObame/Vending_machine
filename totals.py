def total(choice, treats, receipt, t):
    from Inventory import snacks, drinks, sweets
    choice -= 1
    if treats == "1":
        if choice >= 0:
            receipt.append(snacks[choice])
            for X in receipt:
                t += X[1]
            print("total :" + str(round(t,2)))
    elif treats == "2":
        if choice >= 0:
            receipt.append(drinks[choice])
            for X in receipt:
                t += X[1]
            print("total :" + str(round(t,2)))
    elif treats == "3":
        if choice >= 0:
            receipt.append(sweets[choice])
            for X in receipt:
                t += X[1]
            print("total :" + str(round(t,2)))
