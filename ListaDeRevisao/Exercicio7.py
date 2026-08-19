frase = list(map(str, input("Digite sua frase: \n").split()))
print()
for i in range(len(frase)):
    print(*frase[i:len(frase)])