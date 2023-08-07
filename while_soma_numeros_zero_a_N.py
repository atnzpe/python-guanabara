N = int(input("Digite um número: "))

i = 0
soma_N = 0
    
while i <= N:
    soma_N += i
    print(f'Enquanto {i} <= {N} A soma do numero é {soma_N}')
    i += 1

print(soma_N)
