#Desafio 011 - Escreva um programa que progama que leia a altura e largura  de uma parede,
# calcule a área e a quantidade de tinta para pintá-la.
# Um litro pinta 2m²

print("Um litro pinta 2m²\n")
altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))
area = altura*largura
qtd_tinta = area / 2

print(f'A parede tem {round(area,2)} m², e você irá precisar de {round(qtd_tinta,2)} litro(s) de tinta.')


