print("Digite três valores: ")

a = int(input())
b = int(input())
c = int(input())
valores = [a, b, c]

def organizador(valores):
    valoresorganizados = []
    valorescopy = valores.copy()
    menorvalor = 0
    for i in range(len(valores)):
        menorvalor = min(valorescopy)
        valoresorganizados.append(menorvalor)
        valorescopy.remove(menorvalor)
    return valoresorganizados

valoresorganizados = organizador(valores)
print(f"{valoresorganizados[0]}, {valoresorganizados[1]}, {valoresorganizados[2]}")