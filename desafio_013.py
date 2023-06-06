#Leia o salário e mostre um novo preço com o acrescimo de 15%

wage = float(input("Digite o Salário Atual: "))
new_wage =  wage+(wage * 0.15)

print(f"Salário Antigo: R$ {wage}\nSalário Atual: R$ {new_wage}")