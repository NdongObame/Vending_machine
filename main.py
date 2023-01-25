from Goods import snacks, drinks, drinks_prices, sweets, sweets_prices, intro
from choice_1 import First_choice
from check import checker
from totals import total, return_totals

intro()

# first choice (snacks)
First_choice()
choice1 = input("Enter a number(0-3) :")
num = checker(choice1)
total(num)

###

# second choice (drinks)
from choice_2 import choose_snacks
from check import checker2
from totals import return_totals2

choose_snacks(num)
choice2 = input("Enter a number(0-3) :")
num2 = checker2(choice2)
total = return_totals(num) + return_totals2(num2)
print("total =R" + str(round(total, 2)))

###

# third choice (sweets)
from choice_3 import choose_drinks
from check import checker3
from totals import return_totals3
choose_drinks(num2, num)
choice3 = input("Enter a number(0-3) :")
num3 = checker3(choice3)
total1 = return_totals(num) + return_totals2(num2) + return_totals3(num3)
print("total =R" + str(round(total1, 1)))

from correction import completed_order
completed_order(num,num2,num3)
