print("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, input().split("/"))

anoNormal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if(((mes >= 1) and (mes <= 12)) and ((ano >= 1900) and (ano <=2100))):
    if((ano%400 == 0) or ((ano%4 == 0) and (ano%100 != 0))):
        if(mes == 2):
            if(dia >= 1 and dia <= 29):
                print("A data informada é válida!")
            else:
                print("A data informada NÃO é válida!")
        else:
            if dia >= 1 and dia <= anoNormal[mes - 1]:
                print("A data informada é válida!")
            else:
                print("A data informada NÃO é válida!")
    else:
        if((dia >= 1) and (dia <= anoNormal[mes-1])):
            print("A data informada é válida!")
        else:
            print("A data informada NÃO é válida!")
else:
    print("A data informada NÃO é válida!")