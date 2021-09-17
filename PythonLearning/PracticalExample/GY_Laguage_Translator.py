userInput = input("Enter the Phrase you wish to translate:")

gy_translator = ""

for gyt in userInput:

    if gyt in "AEIOUaeiou":
        gy_translator = gy_translator + "o"

    else:
        gy_translator = gy_translator + gyt
print(gy_translator)

