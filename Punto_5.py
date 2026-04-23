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

x = ["perro", "amor", "roma", "roma"]
print(mismos_caracteres(x))