import math

def bhaskara(a,b,c):
    delta =((b ** 2) - 4 * a * c)
    if delta < 0:
        bhaskara = False
        print('Esta equação não possui raízes reais.')
    else:
        x1 = (- b + math.sqrt(delta) // 2 * a)
        x2 = (- b - math.sqrt(delta) // 2 * a)
        print ('As raízes da equação são', x1,'e',x2)
