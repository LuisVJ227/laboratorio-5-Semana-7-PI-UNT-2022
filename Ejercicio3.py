# Ejercicio de laboratorio-Promedios de N estudiantes ordenados de forma Ascendente
N = int(input("ingrese el numero de estudiantes: "))
ls = []
print('-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..-.-.-.-.-')
for i in range (0,N):
    E = input(f"ingrese el nombre del estudiante {i+1}: " )
    P = float(input(f"ingrese el promedio del estudiante {i+1}: "))
    if P>20:
        print('El promedio no debe exceder los 20 puntos')
    else : print('---------------------------------')
    ls.append((P,E))

ls.sort()

print ('Lista ordenada de estudiantes según su promedio')

for i in ls:
    print(i[1],i[0],sep=' --> ')


