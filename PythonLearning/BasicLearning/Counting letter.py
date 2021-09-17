string1 = "HI Hello how are you doing"
string2 = string1.lower().replace(" ", "")
for n in string2:
    result = string2.count(n)
    print("The occurrence of {} in string1 is {}".format(n, result))
