def palindromo():
    palabra = input("Escribe una palabra para mirar si es palindroma: ")
    for i in range(len(palabra)):
        if palabra[i] != palabra[len(palabra) - 1 - i]:
            return "Esta palabra no es palindroma"
        else:
            return "Esta palabra es palindroma"
print(palindromo())     