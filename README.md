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
