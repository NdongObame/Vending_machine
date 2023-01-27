
# you should use a dictionary, like this (or even better, classes)
# snacks = { "oreo": 47.99, "lays": 30, "doritos": 29.99 }...
# it's not ideal to have none as a snack
# the vending machine should handle the case where nothing is selected

snacks = ["none", "oreo", "lays", "doritos"]
snacks_prices = [0, 47.99, 30, 29.99]
drinks = ["none", "coke", "fanta", "sprite"]
drinks_prices = [0, 14.99, 12.99, 12.99]
sweets = ["none", "m&n", "mentol", "chocolate"]
sweets_prices = [0, 7, 3.99, 9.99]

# i added the return type, it is not required because it's a small function and it returns nothing
# but you should add it on long/important functions
def intro() -> None:
    print("welcome to our vendor machine!\nReady for some treats!")
    print("the available treats are :")
    print("snacks : " + str(snacks[1:]))
    print("drinks : " + str(drinks[1:]))
    print("sweets : " + str(sweets[1:]))
