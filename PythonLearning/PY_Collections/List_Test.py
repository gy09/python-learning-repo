list_1 = ["Jack", "Ryan", "Stacie", "Julien", "RiderOP"]
list_2 = [1, 44, 56, 2, 3, 89]

print(list_1[3])
print(list_2[2:5])
list_1[3]="SliderOP"
print(list_1)
list_3 = list_1.extend(list_2)
print(list_1)
list_2.append(999)
print(list_2)
list_2.pop()
print(list_2)
list_1.remove("RiderOP")
print(list_1)
print(list_2.index(56))
list_2.sort()
print(list_2)
list_1.reverse()
print(list_1)
list_4 = list_2.copy
print(list_4)