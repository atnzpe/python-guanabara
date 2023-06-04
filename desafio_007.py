#Leia duas notas do aluno e calcule a média

aluno = input('Digite o nome do Aluno: ')
n1 = float(input("Digite primeira note: "))
n2 = float(input("Digite a segunda note: "))
m = (n1+n2)/2

if m > 7:
    print(f'Aluno {aluno} foi aprovado com média {m}')
elif m < 7:
    print(f'Prezado {aluno} estude mais um pouco, sua média foi {m}')
