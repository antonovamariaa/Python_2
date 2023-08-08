import random
n = int(input('n:'))
sideUp = 0    #единицы
sideDown = 0  #нули
side = 0
for i in range(n):
    side = random.randint(0, 1)
    print (side)
    if side == 0:
        sideDown += 1
    else:
        sideUp += 1


print ("-")   #разделитель
if sideDown > sideUp:
    print (sideUp)
else:
    print (sideDown)
