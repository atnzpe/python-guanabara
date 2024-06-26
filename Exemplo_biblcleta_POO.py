import random


# Classe Pai
class Veiculo:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    # Comportamento do objeto
    # Metodos são funções dentro da classe
    def buzinar(self):
        song_list = ["Sai da Frente!!!", "Muuu", "Béééé", "Fon Fon"]
        print(random.choice(song_list))

    def parar(self):
        print("Parando veículo ...")
        print("Bicicleta parada!")

    def andar(self):
        print("Vrummm...")


# Cria a Classe filha
class Moto(Veiculo):
    pass


class Carro(Veiculo):
    def __init__(self, cor, modelo, ano, tanque_cheio):
        super().__init__(cor, modelo, ano)
        self.tanque_cheio = tanque_cheio

    def abastecido(self):
        print(f"{'Sim' if self.tanque_cheio else 'Não'}' estou abastecido")

    pass


class Caminhao(Veiculo):
    pass


class Bicicleta(Veiculo):
    def trocar_marchar(self):
        print("Trocou A Marcha!")


print("=== TESTE DRIVE ===")
name_client = input("Qual o seu primeiro nome: ")


def menu():
    escolha = input(
        """
        === Escolha o Veículo ===
        [0] Bicicleta
        [1] Moto
        [2] Carro
        [3] Caminhão
        [4] Para SAIR
        ->  """
    )
    return escolha


while True:
    # Preco sorteio
    # preco = [0, 1, 7, 14, 21]
    opcao = menu()
    if opcao == "0":
        object_name = name_client + "_bike"
        cor_escolhida = input("Escolha cor: ")
        modelo_escolhido = input("Escolha o modelo: ")
        ano_escolhido = input("Escolha o ano: ")

        object_name = Bicicleta(cor_escolhida, modelo_escolhido, ano_escolhido)

        print(
            f"Mr. / Mra. {name_client} sua bike é {object_name.cor}, o modelo escolhido foi {object_name.modelo}, ano {object_name.ano} !"
        )

        while True:
            menu_test_bike = input(
                """
                === O  que Deseja ===
                [1] Andar
                [2] Buzinar
                [3] Parar
                [4] Verificar Tanque
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

            elif opcao == "4":
                object_name.abastecido()

            elif opcao == "q":
                break

            else:
                print("Digite uma opção válida!")
                continue

    elif opcao == "1":
        pass
        continue
    elif opcao == "2":
        object_name = name_client + "_carro"
        cor_escolhida = input("Escolha cor: ")
        modelo_escolhido = input("Escolha o modelo: ")
        ano_escolhido = input("Escolha o ano: ")
        # preco_sorteado = random.choice(preco)
        while True:
            _escolha = input("""
            === Tanque Cheio? ===
            [1] Sim
            [0] Não
            """)
            opcao = _escolha
            if opcao == "1":
                tanque_cheio = True
                break
            elif opcao == "2":
                tanque_cheio = False
                break
            else:
                print("Escolha um opção válida!")
                continue
            # preco_sorteado = random.choice(preco)

        object_name = Carro(
            cor_escolhida, modelo_escolhido, ano_escolhido, tanque_cheio
        )

        print(
            f"Mr. / Mra. {name_client} sua bike é {object_name.cor}, o modelo escolhido foi {object_name.modelo}, ano {object_name.ano} !"
        )
        
        continue
    elif opcao == "3":
        pass
        continue
    elif opcao == "4":
        pass
        break
    else:
        print("Digite uma opção válida!")
        continue
