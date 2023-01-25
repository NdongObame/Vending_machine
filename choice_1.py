def First_choice():
    from Goods import snacks, snacks_prices
    print("which snacks do you prefer ?")
    print("0- none")
    print("1- " + str(snacks[1]) + " ... R" + str(snacks_prices[1]))
    print("2- " + str(snacks[2]) + " ... R" + str(snacks_prices[2]))
    print("3- " + str(snacks[3]) + " ... R" + str(snacks_prices[3]))

def snack_chosen(num):
    from Goods import snacks
    if num == 0:
        return "no snacks"
    elif num == 1:
        return snacks[1]
    elif num == 2:
        return snacks[2]
    elif num == 3:
        return snacks[3]