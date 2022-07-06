def Tribonacci(numero):
    if(numero == 0):
        return 0
    elif(numero == 1 or numero ==2):
        return 1
    else:
        return Tribonacci(numero - 1) + Tribonacci(numero - 2) + Tribonacci(numero - 3)

while True:
    n = int(input("Ingrese un número: "))
    if(n >= 0):
        break

for i in range(n):
    print(Tribonacci(i))

print("El número en ma posicion n dada es: ", Tribonacci(i))
