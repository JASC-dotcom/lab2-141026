# Exercise 2.4 - Jose Antonio Santiago Cabrera

phone = input("Phone number (+34-xxxxxxxxx-xx): ")

parts = phone.split("-")   # ['+34', '123456789', '56']
print(parts[1])            # only the number without country code and without extension