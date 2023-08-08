s = int(input('Введите сумму:'))
m = int(input('Введите произведение:'))

x = 0
y = 0
for x in range (1000):
    y = s - x
    if (x + y == s) and (x * y == m):
        print (x, y)
        break
