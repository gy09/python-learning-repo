class calci:

    def sum(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b

    def multiple(self, a, b):
        return a * b

    def divis(self, a, b):
        if b != 0:
            return a / b
        else:
            print("The Denominator cannot be zero")

    def remainder(self, a, b):
        if a != -0 or b != 0:
            return a % b
        else:
            print("The number cannot be zero")


obj = calci()

num1 = float(input("Enter the First Number:"))
num2 = float(input("Enter the Second Number:"))
operator = input("Enter the Operator : '+','-','*','/' ,'%':")

if operator == '+':
    print(obj.sum(num1, num2))
elif operator == '-':
    print(obj.diff(num1, num2))
elif operator == '*':
    print(obj.multiple(num1, num2))
elif operator == '/':
    print(obj.divis(num1, num2))
elif operator == '%':
    print(obj.remainder(num1, num2))
else:
    print("Invalid Operator Entered")
