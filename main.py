from Goods import snacks, drinks, sweets

print("welcome to our vending machine!\nReady for some treats!\n")
t = 0
receipt = []

order = "y"
while order == "y":

    treats = input('''which treats do you want ?
1-Snacks
2-drinks
3-sweets

Enter a number 1-3:''')
    n = 0
    print("\n"
          "The available snacks are :"
          "\n0 - to cancel")
    if treats == "1":
        from choice_1 import Snacks
        for S in snacks:
            n += 1
            print(str(n) + " - " + S[0] + "......." + str(S[1]))
        Snacks()
        order = input("do you want to add something else ? (y or n):")

    elif treats == "2":
        from choice_1 import Drinks
        for D in drinks:
            n += 1
            print(str(n) + " - " + D[0] + "......." + str(D[1]))
        Drinks()
        order = input("do you want to add something else ? (y or n):")
        if order == "y":
            treats = input('''which treats do you want ?
            1-Snacks
            2-drinks
            3-sweets
            type 1-3: ''')
    elif treats == "3":
        from choice_1 import Sweets
        for w in sweets:
            n += 1
            print(str(n) + " - " + w[0] + "......." + str(w[1]))
        Sweets()
        order = input("do you want to add something else ? (y or n):")
        if order == "y":
            treats = input('''which treats do you want ?
            1-Snacks
            2-drinks
            3-sweets
            type 1-3: ''')



print("so it will be :")
T = 0
for each in receipt:
    print(each[0] + "......." + str(each[1]))
    T += each[1]
print("total :" + str(T))
input("Is your order correct ?")
