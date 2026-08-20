a, b = map(int, input().split())

def MMC(x, y):
    i = 2
    while True:
        if not(i%x == 0 and i%y == 0):
            i +=1
        else:
            mmc = i
            break
    return mmc
print(MMC(a, b))