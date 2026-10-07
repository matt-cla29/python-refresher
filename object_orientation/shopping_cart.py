class Product:
    def __init__(self, price, name, amount, colour, make):
        self.price = price
        self.name = name
        self.amount = amount
        self.colour = colour
        self.make = make


shopping_cart = []

# Create a group of students
add_to_cart = input("would you like to add another product into your cart? (yes/no): ")
print(f"result: {add_to_cart}")

while add_to_cart == "yes":
    print("TELL ME ABOUT THE PRODUCT THAT YOU HAVE JUST ADDED TO YOUR SHOPPING CART")
    local_price = int(input("how much is your product (in Pence)?: "))
    local_name = input("What is it called?: ")
    local_amount = input("how many of this product are you getting today?: ")
    local_colour = input("what colour is it?: ")
    local_make = input("do you know who made this?: ")


    new_product = Product(local_price, local_name, local_amount, local_colour, local_make)
    shopping_cart.append(new_product)

    add_to_cart = input("add more products to your cart? (yes/no): ").strip().lower()


print(f"\n\nThere are {len(shopping_cart)} items in your shopping cart right now")

which_product = int(input("\n\nWhich of your product do you want to see? (number): "))


if 1 <= which_product <= len(shopping_cart):
    thisProduct = shopping_cart[which_product - 1]
    print(f"current item is {thisProduct.name}. It costs {thisProduct.price} and was made by {thisProduct.make}, "
          f"its colour is {thisProduct.colour} and comes in a amount of {thisProduct.amount} in its currency")
else:
    print("This product is not currently in your shopping cart")

remove_product = input("\ndo you want to remove a item from your shopping cart? (yes/no): ")
print(f"result: {remove_product}")
while remove_product == "yes":
    item_removed = input("what item do you want to remove?:")
if item_removed == new_product:
    print(f"you have currently removed {thisProduct.name} from your shopping cart")
