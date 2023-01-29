snacks = [["none", 0], ["oreo", 47.99], ["lays", 30], ["doritos", 29.99]]
drinks = [["none", 0], ["coke", 14.99], ["fanta", 30], ["sprite", 29.99]]
sweets = [["none", 0], ["m&n", 7], ["mental", 3.99], ["chocolate", 9.99]]

receipt = []
total = 0
num = int(input(":"))
receipt.append(snacks[num])
for T in receipt:
    total += (T[1])
print(total)