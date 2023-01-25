def choose_drinks(num2, num):
    from choice_1 import snack_chosen
    from Goods import drinks, sweets, sweets_prices
    if num2 == 0:
        print("do you want any sweet ?")
    elif num2 == 1:
        print("any sweet to go with your " + snack_chosen(num) + " and your " + drinks[1] + " ?")
    elif num2 == 2:
        print("any sweet to go with your " + snack_chosen(num) + " and your " + drinks[2] + " ?")
    elif num2 == 3:
        print("any sweet to go with your " + snack_chosen(num) + " and your " + drinks[3] + " ?")
    else:
        print("not avalaible")
    print("0- none")
    print("1- " + str(sweets[1]) + " ... R" + str(sweets_prices[1]))
    print("2- " + str(sweets[2]) + " ... R" + str(sweets_prices[2]))
    print("3- " + str(sweets[3]) + " ... R" + str(sweets_prices[3]))


def sweet_chosen(num3):
    from Goods import sweets
    if num3 == 0:
        return " no sweets "
    elif num3 == 1:
        return " a " + sweets[1]
    elif num3 == 2:
        return " a " + sweets[2]
    elif num3 == 3:
        return " a " + sweets[3]
