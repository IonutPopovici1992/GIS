list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])
del(list[-1])
print(list)
list.append(100)
list.append(200)
list.append(300)
print(list)

for number in list:
    print(number)

print()

number2 = 7

while number2 > 0:
    print(number2)
    number2 -= 1
