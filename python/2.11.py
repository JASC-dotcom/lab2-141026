# Exercise 2.11 - Jose Antonio Santiago Cabrera

product = input("Product name: ")
unit_price = float(input("Unit price (EUR): "))
quantity = int(input("Quantity: "))

total = unit_price * quantity

print(f"{product} {unit_price:9.2f} {quantity:3d} {total:11.2f}")