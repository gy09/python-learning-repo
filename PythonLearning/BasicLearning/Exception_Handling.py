try:
    userInput1 = input("Enter the value string Value: ")
    userInput2 = float(input("Enter the floating point value:"))
    userInput3 = int(input("Enter the integer value:"))
    userInput4 = int(input("Enter the zero value "))

    div = userInput2/userInput1

    addition = userInput1 + userInput2

    subtraction = userInput1 - userInput3

    division = userInput2/userInput4

except TypeError:
    print('User trying to match incorrect type')

except ValueError:
    print("User has entered incorrect Value")

except ZeroDivisionError:
    print("User has entered zero value for the denominator")