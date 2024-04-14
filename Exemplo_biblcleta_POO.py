import random


# Cria a Classe
class Bicicleta:
    # Construtor
    def __init__(self, cor, modelo, ano, valor):
        # instancias do objeto
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Comportamento do objeto
    # Metodos são funções dentro da classe
    def buzinar(self):
        song_list = ["Sai da Frente!!!", "Muuu", "Béééé", "Fon Fon"]
        print(random.choice(song_list))

    def parar(self):
        print("Parando a biclicleta ...")
        print("Bicicleta parada!")

    def andar(self):
        print("Vrummm...")


print("=== TESTE DRIVE ===")
name_client = input("Qual o seu primeiro nome: ")
menu = input(
    """
        === Escolha o Veículo ===
        [1] Bicicleta
        [2] Carro
        [3] Moto
        ->  """
)

while True:
    # Preco sorteio
    preco = [0, 1, 7, 14, 21]

    opcao = int(menu)

    if opcao == 1:
        object_name = name_client + "_bike"
        cor_escolhida = input("Escolha cor: ")
        modelo_escolhido = input("Escolha o modelo: ")
        ano_escolhido = input("Escolha o ano: ")
        preco_sorteado = random.choice(preco)

        object_name = Bicicleta(
            cor_escolhida, modelo_escolhido, ano_escolhido, preco_sorteado
        )

        print(
            f"Mr. / Mra. {name_client} sua bike é {object_name.cor}, o modelo escolhido foi {object_name.modelo}, ano {object_name.ano} eo valor foi de {object_name.valor}!"
        )

        while True:
            menu_test_bike = input(
                """
                === O  quer fazer ===
                [1] Andar
                [2] Buzinar
                [3] Parar
                [q] Sair
                -> """
            )
            opcao = menu_test_bike

            if opcao == "1":
                object_name.andar()
                continue

            elif opcao == "2":
                object_name.buzinar()
                continue

            elif opcao == "3":
                object_name.parar()
                continue

            elif opcao == "q":
                break

            else:
                print("Digite uma opção válida!")
                continue
        break
        
