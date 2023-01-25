def total(num):
    from Goods import snacks_prices
    if num == 0:
        print("total =R" + str(snacks_prices[0]))
    elif num == 1:
        print("total =R" + str(snacks_prices[1]))
    elif num == 2:
        print("total =R" + str(snacks_prices[2]))
    elif num == 3:
        print("total =R" + str(snacks_prices[3]))


def return_totals(num):
    from Goods import snacks_prices
    if num == 0:
        return snacks_prices[0]
    elif num == 1:
        return snacks_prices[1]
    elif num == 2:
        return snacks_prices[2]
    elif num == 3:
        return snacks_prices[3]


# drinks

def return_totals2(num2):
    from Goods import drinks_prices
    if num2 == 0:
        return drinks_prices[0]
    elif num2 == 1:
        return drinks_prices[1]
    elif num2 == 2:
        return drinks_prices[2]
    elif num2 == 3:
        return drinks_prices[3]


# sweets
def return_totals3(num3):
    from Goods import sweets_prices
    if num3 == 0:
        return sweets_prices[0]
    elif num3 == 1:
        return sweets_prices[1]
    elif num3 == 2:
        return sweets_prices[2]
    elif num3 == 3:
        return sweets_prices[3]
