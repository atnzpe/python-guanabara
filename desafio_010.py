# Leia quanto uma pessoa tem na carteira e ela pode comprar em dolares
# Cotação
# US$ 1.00 = R$ 3.37

v_em_real = float(input("Digite quantos reais você tem na carteira: "))
cotacao_dollar = float(input("Qual a cotação do Dollar? "))
real_convertido_dollar = v_em_real / cotacao_dollar

print(f"O valor de R$ {v_em_real} representa o valor em Dollar de US$ {round(real_convertido_dollar,3)}.")

