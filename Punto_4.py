def mayor_suma(Numeros):
    mayor_sum = Numeros[0] + Numeros[1]
    for i in range(len(Numeros) - 1):
        suma = Numeros[i] + Numeros[i+1]
        if suma > mayor_sum:
            mayor_sum = suma
    return mayor_sum

numero = [3, 4, 7, 100, 30, 70, 239]
print(mayor_suma(numero))        