print("with this calulator you can do addition(+), subtraction(-), multiplication(*) and division(/)")
num1 = input("enter first number:")
computation_sign = input("computation sign:")
num2 = input("enter second number:")
def con ():
    if computation_sign == "+":
        return float(num1) + float(num2)
    elif computation_sign == "-":
        return float(num1) - float(num2)
    elif computation_sign == "*":
        return float(num1) * float(num2)
    elif computation_sign == "/":
        return float(num1) / float(num2)
print("the result is :" + str(con()))