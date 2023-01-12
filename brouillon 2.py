choice1 = input("Enter a number(0-3) :")
def checker (choice1):
    ok = 0
    while ok == 0 :
        if len(choice1) != 1:
            choice1 = input("Enter a number(0-3) :")
        else:
            for x in choice1:
                if x in "0123":
                    ok = 1
                    return choice1
                else:
                    print("wrong input, try again")
                    choice1 = input("Enter a number(0-3) :")
checker(choice1)
num = int(checker(choice1))
print (num)