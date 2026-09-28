# ===== code ======

#store product names and prices
# prices are in pense to keep calculations in whole numbers
names = ["crisps", "chocolate", "water"]
prices = [100, 120, 80]

def show_products():
    print("\nvending machine")

    for number in range(len(names)):
        print(number + 1, "-", names[number], "-", prices[number], "p")