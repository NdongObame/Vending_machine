def checker(choice1):
    List = ["0", "1", "2", "3"]
    while choice1 not in List:
        print("wrong input, try again")
        choice1 = input("Enter a number(0-3) :")
    choice1 = int(choice1)
    return choice1


def checker2(choice2):
    List = ["0", "1", "2", "3"]
    while choice2 not in List:
        print("wrong input, try again")
        choice2 = input("Enter a number(0-3) :")
    choice2 = int(choice2)
    return choice2

def checker3(choice3):
    List = ["0", "1", "2", "3"]
    while choice3 not in List:
        print("wrong input, try again")
        choice3 = input("Enter a number(0-3) :")
    choice3 = int(choice3)
    return choice3