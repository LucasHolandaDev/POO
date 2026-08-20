print("Qual valor gostaria de arredondar?")
x = float(input())
def MenorInteiro(x):
    y = int(x)
    res = 0
    if x == y or x < y:
        res = y
    elif x > y:
        res = y+1
    return res
print(MenorInteiro(x))