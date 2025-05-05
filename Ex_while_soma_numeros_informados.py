# Soma todos os numeros
# Informados

soma_dos_numeros = 0
numeros_lidos = 0

while numeros_lidos < 5:  # Cria um laço while
    num_str = input("Digite um valor: ")  # Cria a variável num_str
    # Cria a variavel num_lido. Esta variavel convert num_str eme float
    num_lido = float(num_str)
    soma_dos_numeros += num_lido  # faz a soma dos numeros
    numeros_lidos += 1

#executa a funçõa print da soma dos números com o valor exibindo duas cass decimais
print(f"A soma dos números é {soma_dos_numeros:.2f}")
