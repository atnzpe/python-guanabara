# Escreva um algoritimo ue leia o numero e escreva sua tabuada

n = int(input("Digite um numro: "))

print(f"Tabuada de {n}!")
for i in range(11):
    print(f'{n} x {i} = {(n * i)}')