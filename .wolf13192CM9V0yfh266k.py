"""
Escreva um programa que pergunte a quantidade de KM percorrido por um
carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o Preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

"""


def calcula_diaria(valor, qtd_dias):
    return valor * qtd_dias


def valor_por_km(valor_km, km_rodado):
    return valor_km * km_rodado


valor_diaria = float(input("Digite o valor da diária: R$ "))
dias_de_aluguel = int(input("Digite a quantidade de dias de aluguel: "))
valor_km = float(input("Digite o valor por quilometro: "))
km_rodado = float(input("Total km rodados: "))


total_diaria = calcula_diaria(valor_diaria, dias_de_aluguel)
valor_total_km = valor_por_km(valor_km, km_rodado)
total = total_diaria + valor_total_km

print(f"O valor da é R$ {total_diaria:.2f}\n")
