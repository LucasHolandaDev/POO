print("Digite o número do mês: ")
mes = int(input())
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Novembro", "Dezembro"]
trimestre = ["Primeiro", "Segundo", "Terceiro", "Quarto"]
mesAtual = meses[mes - 1]
if(mes <= 3):
    trimestreAtual = trimestre[0]
elif((mes > 3) and (mes <= 6)):
    trimestreAtual = trimestre[1]
elif((mes > 6) and (mes <= 9)):
    trimestreAtual = trimestre[2]
elif((mes > 9) and (mes <= 12)):
    trimestreAtual = trimestre[3]

print(f"O mês de {mesAtual} é do {trimestreAtual} trimestre do ano.")