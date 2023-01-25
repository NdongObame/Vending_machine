def choose_snacks(num):
    from Goods import snacks, drinks, drinks_prices
    if num == 0:
        print("do you want any drinks ?")
    elif num == 1:
        print("which drinks do you want with your " + snacks[1] + " ?")
    elif num == 2:
        print("which drinks do you want with your " + snacks[2] + " ?")
    elif num == 3:
        print("which drinks do you want with your " + snacks[3] + " ?")
    else:
        print("not avalaible")
    print("0- none")
    print("1- " + str(drinks[1]) + " ... R" + str(drinks_prices[1]))
    print("2- " + str(drinks[2]) + " ... R" + str(drinks_prices[2]))
    print("3- " + str(drinks[3]) + " ... R" + str(drinks_prices[3]))

def drink_chosen(num2):
    from Goods import drinks
    if num2 == 0:
        return " no drinks"
    elif num2 == 1:
        return " a " + drinks[1]
    elif num2 == 2:
        return " a " + drinks[2]
    elif num2 == 3:
        return " a " + drinks[3]