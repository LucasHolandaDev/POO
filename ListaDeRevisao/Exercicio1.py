print("Digite quatro valores inteiros: ")
# O usuário deve digitar quatro valores inteiros separados por espaço

numeros = list(map(int, input().split()))
# O código acima lê quatro valores inteiros digitados pelo usuário e os armazena em uma lista chamada 'numeros'.

def contadorpar(valores):
    pares = 0
    for i in range(len(valores)):
        if valores[i] % 2 == 0:
            pares += valores[i]
    return pares;
# A função 'contadorpar' recebe uma lista de valores e retorna a soma dos números pares presentes nessa lista. Ela inicializa uma variável 'pares' com zero, percorre cada elemento da lista e verifica se é par (usando o operador módulo). Se for par, adiciona o valor à variável 'pares'. No final, retorna a soma dos números pares.

def contadorimpar(valores):
    impares = 0
    for i in range(len(valores)):
        if valores[i] % 2 == 1:
            impares += valores[i]
    return impares;
# A função 'contadorimpar' funciona de maneira semelhante à função 'contadorpar', mas em vez de somar os números pares, ela soma os números ímpares presentes na lista. Ela inicializa uma variável 'impares' com zero, percorre cada elemento da lista e verifica se é ímpar (usando o operador módulo). Se for ímpar, adiciona o valor à variável 'impares'. No final, retorna a soma dos números ímpares.

total_pares = contadorpar(numeros)
total_impares = contadorimpar(numeros)
# As duas linhas acima chamam as funções 'contadorpar' e 'contadorimpar', passando a lista 'numeros' como argumento. O resultado da soma dos números pares é armazenado na variável 'total_pares', e o resultado da soma dos números ímpares é armazenado na variável 'total_impares'.

print(f"Soma dos pares = {total_pares}")
print(f"Soma dos impares = {total_impares}")
# As duas linhas acima imprimem na tela a soma dos números pares e a soma dos números ímpares, utilizando f-strings para formatar a saída.1 2 3 4 5 6 7 8 9 0