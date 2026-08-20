import math

print("Digite a base e a altura do seu retângulo: ")
b, h = map(int, input().split())

def Diagonal(b, h):
    diagonal = math.sqrt(math.pow(b, 2) + math.pow(h, 2))
    return diagonal

print(f"Diagonal: {Diagonal(b, h):.2f}")