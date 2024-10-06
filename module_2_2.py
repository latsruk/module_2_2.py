first = int(input('Введите 1 чесло: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 чило: '))
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)