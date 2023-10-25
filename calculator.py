#int
x = int(input("What's x: "))
y = int(input("what's y: "))
print(x + y)

#float
x = float(input("What's x: "))
y = float(input("what's y: "))
z = round(x + y)
print(f"{z:,}")  # number format using commas as separator = 1,000

x = float(input("What's x: "))
y = float(input("what's y: "))
z = round(x / y, 2)
print(z)

#
z = (x / y)
print(f"{z:.2f}")  # f string approach
