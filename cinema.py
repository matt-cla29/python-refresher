price = 0
age = int(input("please enter your age: "))
if age < 12:
    price + 5
elif age <= 12 and age >= 17:
    price + 7
elif age <= 18 and age >= 64:
    price + 10
elif age <= 65:
    price + 6
student = input("you are a student: ")
if student == True and age >= 18:
    price - 2
else:
    print(price)
