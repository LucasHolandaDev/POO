print("Digite uma frase: ")
frase = input()
frasemex = [letra for letra in frase]
print()
for i in range(len(frasemex)):
    frasemex.append(frasemex[0])
    frasemex.remove(frasemex[0])
    print("".join(frasemex))