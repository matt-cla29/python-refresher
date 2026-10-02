
# === CODE ===

#Import our own python files.
import products
import payments

products.show_products()

# this starter version assumes valid whole-number inputs
choice = int(input("\nchoose a product number: "))
amount = int(input("enter your payment in pence: "))

# convert the menu number into a list index
index = choice - 1

product = products.names[index]
price = products.prices[index]

# call the payment-checking function
if payments.enough_money(amount, price):
    change = payments.calculate_change(amount, price)

    print("dispensing:", product)
    print("your change:", change, "p")

else:
    print("not enough money.")
    print("your payment has been returned:", amount, "p")