lista = list(map(int, input("Digite os números separados por espaço: ").split()))

def negador(lista):
    listacopy = []
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            listacopy.append(lista[i]*-1)
        else:
            listacopy.append(lista[i])
    return listacopy

print("Resultado :",*negador(lista))