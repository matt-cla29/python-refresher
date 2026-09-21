print("\n--- LOGICAL OPERATORS ---\n")
# logical operators are used to combine multiple conditions and return a boolean (True or False) result
# the basic logical operators in python are:
# AND (and), OR (or), NOT (not)

age = 17
has_id = True

# AND -> Both conditions must be True
print("can enter nightclub:", age >= 18 and has_id)

# OR -> only one condition needs to be True
print("Discount applies:", age < 18 or age > 60)

# NOT -> Reverses the result
print("Has no ID:", not has_id)

print("\n--------------------------------\n")