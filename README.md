## Clase Programacion Orientada a Objetos: Reto_1

Explicacion del ejercicio 1

El problema planteado el cual esperaba que se hiciera una funcion para poder recolectar el dato de 2 numeros y un signo el cual represantaba una operacion matematica, lo primero que se hizo en el codigo fue, poner 2 bucles esto con fin de que si en algun momento llegara a tener el usuario algun error tipografico y puso una letra en vez de un numero, el programa devolvera al usuario hasta que ponga un numero, y despues de esto por medio de condicionales se determinaron cuales iban a ser los signos y como el codigo iba a reconocerlos. el codigo a continuacion:

    def operacion():
        while True:
            try:
                x = float(input("Escribe un numero para la operacion: "))
                break
            except ValueError:
                print("Primero va un numero")
        while True:       
            try:
                y = float(input("Escribe otro numero para la operacion: "))
                break
            except ValueError:
                print("Segundo va un numero")       
    
        sign = input("Escribe un signo basico para la operacion matematica: ")       
        if sign == "+":
            return x + y
        elif sign == "-":
            return x - y
        elif sign == "*":    
            return x * y
        elif sign == "/":
            if y != 0:
                return x / y
            else:
                print("Prueba otro numero")
        else: 
            return print("No puedo hacer una operacion basica con esto, nice try")


Explicacion del ejercicio 2 

El problema planteado para el ejercicio 2 era desarrollar una funcion la cual revisara si la palabra era palindroma o no, el ejercicio se hizo aprovechando una propiedad de los strings y esta es que son arrays, visualizando si la primera letra coincidia con la ultima, la segunda con la penultima y asi sucesivamente se comprobo si era palindroma o no. El codigo a continuacion:

    def palindromo():
        palabra = input("Escribe una palabra para mirar si es palindroma: ")
        for i in range(len(palabra)):
            if palabra[i] != palabra[len(palabra) - 1 - i]:
                return "Esta palabra no es palindroma"
            else:
                return "Esta palabra es palindroma"    

Explicacion del ejercicio 3

El problema para el ejercicio 3 era desarrollar una funcion que determinara si un numero con respecto a un conjunto de datos era primo o no, el ejercicio fue posible con el operacion de modulo, esta operacion realiza la division de dos numeros y da el residuo de este, ya que los primos no son divisibles por ningun numero que no sea por ellos mismos o por uno, primero se filtra que no alla ningun numero que sea menor a 2 ya que desde aqui empiezan los primos, despues de pasar ese filtro se revisa uno por uno los numeros para saber si este es divisible por algun numero apartir de dos, si esto no es posible es primo. El codigo a continuacion:

    def Primos(primo):
        primos = []
        for i in primo:
            if i < 2:    
                continue 
            Yeah_be = True
            for o in range(2, i):
                if i % o == 0:
                    Yeah_be= False
                    break
            if Yeah_be:
                primos.append(i)
        return primos

Explicacion del ejercicio 4

El problema del ejercicio 4 era escribir una funcion que con respecto a una lista de numeros retorne la suma de dos numeros consecutivos dentro de la lista, la clave en este ejercicio es aprovechar que la lista es una array y usar las posiciones de la lista y hacer la suma, esto por medio de un for i in range(len.....), este bucle revisa todas las posiciones dentro de la lista y las suma con el numero siguiente, hasta llegar al ultimo numero, despues mandara el resultado de la mayor suma.

    def mayor_suma(Numeros):
    mayor_sum = Numeros[0] + Numeros[1]
    for i in range(len(Numeros) - 1):
        suma = Numeros[i] + Numeros[i+1]
        if suma > mayor_sum:
            mayor_sum = suma
    return mayor_sum

Explicacion del ejercicio 5

El problema del ejercicicio 5 era escribir una funcion que devolviera los strings que contuvieran los mismos caracteres, en este ejercicio la solucion se encontraba en una parte en los bucles y en el otro el "sorted", el "sorted" desmantelo el string que se le enviaba y este reviso los caracteres, se hizo un if para poder comparar si el sorted de la palabra que sacamos con el i era el mismo que el de la j, El codigo a continuacion.

    def mismos_caracteres(array):
    listado = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if sorted(array[i]) == sorted(array[j]):
                if array[i] not in listado:
                    listado.append(array[i])
                if array[j] not in listado:
                    listado.append(array[j])
    return listado 
