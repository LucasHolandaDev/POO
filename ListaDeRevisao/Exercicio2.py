print("Digite o número do mês: ")
mes = int(input())
# O usuário deve digitar o número do mês desejado;

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Novembro", "Dezembro"]
trimestre = ["Primeiro", "Segundo", "Terceiro", "Quarto"]
# O nome dos meses e os trimestres são armazenados em listas;

def localizador(mes):
    # Função para localizar o trimestre;
    if(mes <= 3):
        trimestreAtual = trimestre[0]
    elif((mes > 3) and (mes <= 6)):
        trimestreAtual = trimestre[1]
    elif((mes > 6) and (mes <= 9)):
        trimestreAtual = trimestre[2]
    elif((mes > 9) and (mes <= 12)):
        trimestreAtual = trimestre[3]
    return trimestreAtual

mesAtual = meses[mes - 1]
# O mes atual é definido através da lista;
trimestreAtual = localizador(mes)
# Chama a função para definir o trimestre;

print(f"O mês de {mesAtual} é do {trimestreAtual} trimestre do ano.")
# Mostra na tela o mês e o Trimestre do mesmo;