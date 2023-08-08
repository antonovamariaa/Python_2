from math import sqrt
s = int(input('Введите сумму:'))
m = int(input('Введите произведение:'))

if (s*s)-(4*m) < 0:
    print("Отрицательный корень")
else: 

    x1 = ((-s)+sqrt((s*s)-(4*m))) // -2
    x2 = ((-s)-sqrt((s*s)-(4*m))) // -2

    if (x1+x2 == s) and (x1*x2 == m):
        print(int(x1))
        print(int(x2))
    else:
        print("Такой пары не существует")
