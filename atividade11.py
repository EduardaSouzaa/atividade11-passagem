# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas
print("Calcular o preço da passagem")
dist = float(input("Digite a distância da viagem em Km: "))
if dist<=200:
    print(f"O valor da passagem é de {dist*0.50}")
else:
    print(f"O valor da passagem é de {dist*0.45}")