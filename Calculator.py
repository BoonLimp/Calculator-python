num = int(input("Enter first value \n"))
num2 = int(input("Enter second value \n "))
method = str(input("Enter the procedure you want to calculate \n"))

if "+" in method or "plus" in method:
    result = num + num2
    print(result)
elif "-" in method or "subtract" in method or "minus" in method:
    result = num - num2
    print(result)
elif "*" in method or "multiply" in method:
    result = num * num2
    print(result)
elif "/" in method or "divide" in method:
    result = num/num2
    print(result)
else:
    print("Enter procedure correctly")