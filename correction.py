def completed_order(num, num2, num3):
    from choice_1 import snack_chosen,First_choice
    from choice_2 import drink_chosen, choose_snacks
    from choice_3 import sweet_chosen, choose_drinks
    from totals import return_totals,return_totals2,return_totals3
    from check import checker, checker2, checker3
    if num == 0 and num2 == 0 and num3 == 0:
        print("see you next time")
    else:
        print("so it will be " + snack_chosen(num) + " ," + drink_chosen(num2) + " and" + sweet_chosen(num3))
        print("Is your order correct ?")
        decision = input("type \"Y\" or \"N\" : ").lower()
        while decision != "y" and decision != "n":
            decision = input("wrong input. Type \"Y\" or \"N\" :")
        while decision == "n":
            print(" what do you want to change : \nSnacks(1)\ndrinks(2)\nsweets(3)")
            correction = input("Enter a number(1-3) :")
            if correction == "1":
                First_choice()
                choice1 = input("Enter a number(0-3) :")
                num = checker(choice1)
                total1 = return_totals(num) + return_totals2(num2) + return_totals3(num3)
                print("total =R" + str(round(total1, 1)))
            elif correction == "2":
                choose_snacks(num)
                choice2 = input("Enter a number(0-3) :")
                num = checker2(choice2)
                total1 = return_totals(num) + return_totals2(num2) + return_totals3(num3)
                print("total =R" + str(round(total1, 1)))
            elif correction == "3":
                choose_drinks(num2, num)
                choice3 = input("Enter a number(0-3) :")
                num3 = checker3(choice3)
                total1 = return_totals(num) + return_totals2(num2) + return_totals3(num3)
                print("total =R" + str(round(total1, 1)))
            print("so it will be " + snack_chosen(num) + " ," + drink_chosen(num2) + " and" + sweet_chosen(num3))
            print("Is your order correct ?")
            decision = input("type \"Y\" or \"N\" : ").lower()
            while decision != "y" and decision != "n":
                decision = input("wrong input. Type \"Y\" or \"N\" :")
        print("Thank you !")
