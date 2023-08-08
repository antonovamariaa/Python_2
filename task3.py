n = int(input('n:'))
num = 2
power = 0
temp = 0
for _ in range (n):
    temp = pow(num, power)
    if temp > n:
        break
    else:
        print (temp)
        power += 1
