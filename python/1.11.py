# Exercise 1.11 - Jose Antonio Santiago Cabrera

INTEREST = 0.04  # constant: 4 % per year

balance = float(input("Amount deposited (EUR): "))

year1 = balance * (1 + INTEREST)
year2 = year1 * (1 + INTEREST)
year3 = year2 * (1 + INTEREST)

print(f"Balance after year 1: {round(year1, 2)} EUR")
print(f"Balance after year 2: {round(year2, 2)} EUR")
print(f"Balance after year 3: {round(year3, 2)} EUR")