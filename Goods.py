snacks = ["none", "oreo", "lays", "doritos"]
snacks_prices = [0, 47.99, 30, 29.99]
drinks = ["none", "coke", "fanta", "sprite"]
drinks_prices = [0, 14.99, 12.99, 12.99]
sweets = ["none", "m&n", "mentol", "chocolate"]
sweets_prices = [0, 7, 3.99, 9.99]

def  intro() :
    print("welcome to our vendor machine!\nReady for some treats!")
    print("the available treats are :")
    print("snacks : " + str(snacks[1:]))
    print("drinks : " + str(drinks[1:]))
    print("sweets : " + str(sweets[1:]))