def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x = float(input("Enter the first number"))
y = float(input("Enter the second number"))
z = float(input("Enter the third number"))

print(maximum(x, y, z))
