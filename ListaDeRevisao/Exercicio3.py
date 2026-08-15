print("Digite 4 valores inteiros: ")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

valores = [a, b, c, d]


maiorvalor = max(valores)
menorvalor = min(valores)
valores2 = valores.copy()

valores2.remove(maiorvalor)
valores2.remove(menorvalor)

segundomaior = max(valores2)
segundomenor = min(valores2)
soma = segundomaior + segundomenor

if(a != b and a != c and a != d and b != c and b != d and c != d):
    print(f"Maior valor = {maiorvalor}")
    print(f"Menor valor = {menorvalor}")
    print(f"A soma do segundo maior valor com o segundo menor = {soma}")