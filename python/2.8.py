# Exercise 2.8 - Jose Antonio Santiago Cabrera

price = float(input("Price (EUR, 2 decimals): "))

total_cents = round(price * 100)   # avoids floating-point errors (0.1 + 0.2...)
euros = total_cents // 100         # integer division
cents = total_cents % 100          # remainder

print(f"Euros: {euros}")
print(f"Cents: {cents}")