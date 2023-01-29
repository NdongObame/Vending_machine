def total(num):
    from Goods import snacks, drinks, sweets
    from main import treats, receipt, t
    num -= 1
    if treats == "1":
        if num < 0:
            print("total = R0")
        else:
            receipt.append(snacks[num])
            for X in receipt:
                t += X[1]
            print(str(t))
    elif treats == "2":
        if num < 0:
            print("total = R0")
        else:
            receipt.append(drinks[num])
            for X in receipt:
                t += X[1]
            print(str(t))
    elif treats == "3":
        if num < 0:
            print("total = R0")
        else:
            receipt.append(sweets[num])
            for X in receipt:
                t += X[1]
            print(str(t))