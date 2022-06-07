import math

valorA = int(input("Coloque o valor de A: "))
valorB = int(input("Coloque o valor de B: "))
valorC = int(input("Coloque o valor de C: "))

deltaBhaskara = ((valorB ** 2) - 4 * valorA * valorC)
print(deltaBhaskara)

if (deltaBhaskara < 0):
    print("Essa equação não possui raízes reais.")
    
if (deltaBhaskara == 0):
    print("A raiz dessa equação é 0.")
else:
    print("As raízes dessa equação são: ", int((( -(valorB) + math.sqrt(deltaBhaskara)) / (2 * valorA))), "e", int(( - (valorB) - math.sqrt(deltaBhaskara) / (2 * valorA))))
    

