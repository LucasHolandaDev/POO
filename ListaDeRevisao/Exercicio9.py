print("Digite uma frase: ")
frase = list(input().split())
print()
for i in range(len(frase)):
    print("".join(reversed(frase[i])))