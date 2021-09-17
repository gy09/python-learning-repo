array_list = [
    [1, 2, 3, 4],
    ['Rina', 'Tina', 'Jina', 'Cena'],
    ['Maths', 'Chemistry', 'Physics', 'Astrology'],  
    [99, 100, 98, 100]
]

print(array_list[2][1])
print(array_list[0][3])
print(array_list[3][3])

for row in array_list:
    print(row)
    for col in row:
        print(col)