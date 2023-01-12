def checker4(choice2):
    ok = 0
    while ok == 0:
        if len(choice2) != 1:
            choice2 = input("Enter a number(0-3) :")
        else:
            for x in choice2:
                if x in "yn":
                    ok = 1
                    return choice2
                else:
                    print("wrong input, try again")
                    choice2 = input("Enter a number(0-3) :")


checker2(choice2)
num2 = int(checker2(choice2))