#leia um numero em metros e exiba em centimetros e milimetros

n_metros = float(input("Digite a quantidade em metros: "))
metros_em_centimetros = n_metros * 100
metros_em_milimetros = n_metros * 1000

print(f'{n_metros} metros\n{metros_em_centimetros} centímetros, ou\n{metros_em_milimetros} milímetros.')