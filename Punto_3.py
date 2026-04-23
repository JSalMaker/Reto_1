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
        