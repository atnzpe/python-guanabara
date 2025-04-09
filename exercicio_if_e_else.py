

# 1- Crie um programa que receba o seu saldo bancário e o quanto você deve.
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

saldo_conta = float(input("Digite o seu saldo: "))

saldo_devedor = float(input("Digite o seu saldo devedor: "))

saldo_atual = saldo_conta - saldo_devedor

resultado = "Saldo Positivo!" if saldo_atual > 0 else "Saldo Negativo" if saldo_atual < 0 else saldo_atual

print(f"Saldo da conta: R$ {saldo_atual} |", resultado)

# 2- Crie um programa que possui uma variável
# que guarde seu CPF
# e que guarde uma senha de sua escolha.
# Em seguida receba por input uma senha do usuário.
# Caso a senha recebida seja a correta mostre o CPF,
# caso não diga que a senha esta incorreta.

CPF_USER = 12345678900

KEY_USER = 123456

input_user = int(input("Digite sua senha de 6 numeros: "))

print(f"Seja bem vindo {CPF_USER}!" if input_user == KEY_USER else "Senha Incorreta!")


# 3- Crie um programa que fale sobre sua idade.
# As regras são a seguinte, você deve receber por input sua idade,
# se você tiver ate três anos printe que é um bebe, ate 13 anos uma criança,
# ate 18 anos adolescente, até 65 adulto.
# Em nenhum deste casos é um idoso

age_user = int("Digite sua idade: ")

print('É um bêbê' if )

# 4- Crie um programa que receba dois números,
# e também receba do usuário a operação que deve ser feita, as possibilidades são
# soma(+), subtração (-), divisão(/) e multiplicação(*).
# Realize a operação escolhida sobre os dois números.
