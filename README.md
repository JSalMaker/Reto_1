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
    print(operacion())


Explicacion del ejercicio 2 

El problema planteado para el reto dos era desarrollar una funcion la cual revisara si la palabra era palindroma o no, el ejercicio se hizo aprovechando una propiedad de los strings y esta es que son arrays, visualizando si la primera letra coincidia con la ultima, la segunda con la penultima y asi sucesivamente se comprobo si era palindroma o no. El codigo a continuacion:

    def palindromo():
        palabra = input("Escribe una palabra para mirar si es palindroma: ")
        for i in range(len(palabra)):
            if palabra[i] != palabra[len(palabra) - 1 - i]:
                return "Esta palabra no es palindroma"
            else:
                return "Esta palabra es palindroma"
    print(palindromo())     

Explicacion del ejercicio 3

El problema para el reto 3 era desarrollar una funcion que determinara si un numero con respecto a un conjunto de datos era primo o no, el ejercicio fue posible con el operacion de modulo, esta operacion realiza la division de dos numeros y da el residuo de este, ya que los primos no son divisibles por ningun numero que no sea por ellos mismos o por uno, primero se filtra que no alla ningun numero que sea menor a 2 ya que desde aqui empiezan los primos, despues de pasar ese filtro se revisa uno por uno los numeros para saber si este es divisible por algun numero apartir de dos, si esto no es posible es primo. El codigo a continuacion:

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
    x = [13, 4, 7, 9, 13445, 73, 31]
    print(Primos(x))
