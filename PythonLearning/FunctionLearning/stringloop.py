my_string = input("Enter the value of string")
string1 = my_string.lower()
count = 0
for val in string1:
    if val == 'i' or val == 'I':
        count = count + 1
    # else :
    #     print("No i's in the sentence")
print("Count of number of i in string is:  "+ str(count))