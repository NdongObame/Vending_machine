from Inventory import inventory

print("welcome to our vending machine!\nReady for some treats!\n")
# "t" is the temporary total while "T" is the final total
t = 0
receipt = []
order = "y"

while order == "y":
    treats = input("which treats do you want ?\n0- Exit\n1- Snacks\n2- drinks\n3- sweets"
                   "\nEnter a number 1-3:")
    if treats == "0":
        input("Bye, bye")
        exit()
    # "n" correspond to the number of element in each list of inventory is initial state is 0 cause it counts
    # from 0 + n elements there is in each list

    n = 0
    print("The available ones are :"
          "\n0 - to cancel")
    from choice_input import Choosing
    for each in inventory[treats]:
        n += 1
        print(str(n) + " - " + each[0] + "......." + str(each[1]))
    Choosing(treats, receipt, t)
    order = input("do you want to add something else ? (y or n):")

print("so it will be :")
T = 0
for each in receipt:
    print(each[0] + "......." + str(each[1]))
    T += each[1]
print("total :" + str(round(T, 2)))
input("Is your order correct ?")
