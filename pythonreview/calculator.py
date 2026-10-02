calculatorcheck = input("what math would you like to do?: ")
if calculatorcheck == "multiply":
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    print(num1 * num2)
elif calculatorcheck == "divide":
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    print(num1 / num2)
elif calculatorcheck == "plus":
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    print(num1 + num2)
elif calculatorcheck == "minus":
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        print(num1 - num2)
else:
     print("that is not a choice we can do")
