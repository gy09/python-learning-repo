list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [11, 12, 13, 14, 15, 156, 8]
list3 = [112, 112, 113, 114]
list1.extend(list2)
list3.append(list2)
print(list1)
print(list3)
print(list3[4][3])
list4 = list2 + ['x', 'y', 'z']
print(list4)

list4.insert(10, 'xyz')
print(list4)


print(list4.pop())
print(list4)
list1.sort()
print(list1)