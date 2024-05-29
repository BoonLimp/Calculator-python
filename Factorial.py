def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)


num1 = int(input("Enter the number you want to calculate \n"))
print("result is", Factorial(num1))