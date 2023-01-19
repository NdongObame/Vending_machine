snacks = ["none", "oreo", "lays", "doritos"]
snacks_prices = [0, 47.99, 30, 29.99]

drinks = ["none", "coke", "fanta", "sprite"]
drinks_prices = [0, 14.99, 12.99, 12.99]

sweets = ["none", "m&n", "mentol", "chocolate"]
sweets_prices = [0, 7, 3.99, 9.99]

# introduction
print("welcome to our vendor machine!\nReady for some treats!")
print("the available treats are :")

# treats available
print("snacks : " + str(snacks[1:]))
print("drinks : " + str(drinks[1:]))
print("sweets : " + str(sweets[1:]))


# first choice (snacks)
def First_choice():
    print("which snacks do you prefer ?")
    print("0- none")
    print("1- " + str(snacks[1]) + " ... R" + str(snacks_prices[1]))
    print("2- " + str(snacks[2]) + " ... R" + str(snacks_prices[2]))
    print("3- " + str(snacks[3]) + " ... R" + str(snacks_prices[3]))


First_choice()
choice1 = input("Enter a number(0-3) :")

List = ["0", "1", "2", "3"]


def checker(choice1):
    while choice1 not in List:
        print("wrong input, try again")
        choice1 = input("Enter a number(0-3) :")
    return choice1


checker(choice1)
num = int(checker(choice1))


# total first order :
def total():
    if num == 0:
        print("total =R" + str(snacks_prices[0]))
    elif num == 1:
        print("total =R" + str(snacks_prices[1]))
    elif num == 2:
        print("total =R" + str(snacks_prices[2]))
    elif num == 3:
        print("total =R" + str(snacks_prices[3]))


total()


def return_totals():
    if num == 0:
        return snacks_prices[0]
    elif num == 1:
        return snacks_prices[1]
    elif num == 2:
        return snacks_prices[2]
    elif num == 3:
        return snacks_prices[3]


###

def choose_snacks():
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


choose_snacks()


def snack_chosen():
    if num == 0:
        return "no snacks"
    elif num == 1:
        return snacks[1]
    elif num == 2:
        return snacks[2]
    elif num == 3:
        return snacks[3]


# second choice (drinks)
def Second_choice():
    print("0- none")
    print("1- " + str(drinks[1]) + " ... R" + str(drinks_prices[1]))
    print("2- " + str(drinks[2]) + " ... R" + str(drinks_prices[2]))
    print("3- " + str(drinks[3]) + " ... R" + str(drinks_prices[3]))


Second_choice()
choice2 = input("Enter a number(0-3) :")


def checker2(choice2):
    while choice2 not in List:
        print("wrong input, try again")
        choice1 = input("Enter a number(0-3) :")
    return choice2


checker2(choice2)
num2 = int(checker2(choice2))


# total : first + second order :
def return_totals2():
    if num2 == 0:
        return drinks_prices[0]
    elif num2 == 1:
        return drinks_prices[1]
    elif num2 == 2:
        return drinks_prices[2]
    elif num2 == 3:
        return drinks_prices[3]


total = return_totals() + return_totals2()
print("total =R" + str(round(total, 2)))


###
def choose_drinks():
    if num2 == 0:
        print("do you want any sweet ?")
    elif num2 == 1:
        print("any sweet to go with your " + snack_chosen() + " and your " + drinks[1] + " ?")
    elif num2 == 2:
        print("any sweet to go with your " + snack_chosen() + " and your " + drinks[2] + " ?")
    elif num2 == 3:
        print("any sweet to go with your " + snack_chosen() + " and your " + drinks[3] + " ?")
    else:
        print("not avalaible")


choose_drinks()


def drink_chosen():
    if num2 == 0:
        return " no drinks"
    elif num2 == 1:
        return " a " + drinks[1]
    elif num2 == 2:
        return " a " + drinks[2]
    elif num2 == 3:
        return " a " + drinks[3]


# third choice (sweets)
def Third_choice():
    print("0- none")
    print("1- " + str(sweets[1]) + " ... R" + str(sweets_prices[1]))
    print("2- " + str(sweets[2]) + " ... R" + str(sweets_prices[2]))
    print("3- " + str(sweets[3]) + " ... R" + str(sweets_prices[3]))


Third_choice()
choice3 = input("Enter a number(0-3) :")


def checker3(choice3):
    while choice3 not in List:
        print("wrong input, try again")
        choice3 = input("Enter a number(0-3) :")
    return choice3


checker3(choice3)
num3 = int(checker3(choice3))


def sweet_chosen():
    if num3 == 0:
        return " no sweets "
    elif num3 == 1:
        return " a " + sweets[1]
    elif num3 == 2:
        return " a " + sweets[2]
    elif num3 == 3:
        return " a " + sweets[3]


def return_totals3():
    if num3 == 0:
        return sweets_prices[0]
    elif num3 == 1:
        return sweets_prices[1]
    elif num3 == 2:
        return sweets_prices[2]
    elif num3 == 3:
        return sweets_prices[3]


###
def completed_order():
    if num == 0 and num2 == 0 and num3 == 0:
        print("see you next time")
    else:
        print("so it will be " + snack_chosen() + " ," + drink_chosen() + " and" + sweet_chosen())
        print("Is your order correct ?")


# total : first + second + third order :


total1 = return_totals() + return_totals2() + return_totals3()
print("total =R" + str(round(total1,1)))


###


def finalising():
    completed_order()
    decision = input("type \"Y\" or \"N\" : ").lower()
    while decision != "y" and decision != "n":
        decision = input("wrong input. Type \"Y\" or \"N\" :")
    return decision


while finalising() == "n":
    print(" what do you want to change : \nSnacks(1)\ndrinks(2)\nsweets(3)")
    correction = input("Enter a number(1-3) :")
    if correction == "1":
        First_choice()
        choice1 = input("Enter a number(0-3) :")
        checker(choice1)
        num = int(choice1)
        total1 = return_totals() + return_totals2() + return_totals3()
        print("total =R" + str(total1))
    elif correction == "2":
        Second_choice()
        choice2 = input("Enter a number(0-3) :")
        checker2(choice2)
        num2 = int(choice2)
        total1 = return_totals() + return_totals2() + return_totals3()
        print("total =R" + str(total1))
    elif correction == "3":
        Third_choice()
        choice3 = input("Enter a number(0-3) :")
        checker3(choice3)
        num3 = int(choice3)
        total1 = return_totals() + return_totals2() + return_totals3()
        print("total =R" + str(total1))
print("Thank you !")
