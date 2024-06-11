class UsuarioTelefone:
    """
    Representa um usuário de telefone com nome, número e plano.
    """

    PLANOS = ["Plano Essencial Fibra", "Plano Prata Fibra", "Plano Premium Fibra"]

    def __init__(self, nome, numero, plano):
        """
        Inicializa um novo usuário.

        Args:
            nome: O nome do usuário.
            numero: O número de telefone do usuário.
            plano: O plano do usuário.
        """
        self.__nome = nome
        self.__numero = numero
        if plano in self.PLANOS:
            self.__plano = plano
        else:
            raise ValueError("Plano inválido. Os planos disponíveis são: " +
                             ", ".join(self.PLANOS))

    def __str__(self):
        """
        Retorna uma representação em string do usuário.
        """
        return (
            f"Usuário {self.__nome} criado com sucesso."
            
        )

# Entrada:
nome = input()  
numero = input()  
plano = input()  

# Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)

class PlanoTelefone:
    """
    Representa um plano de telefone com nome e saldo.
    """

    def __init__(self, nome, saldo):
        """
        Inicializa um novo plano de telefone.

        Args:
            nome: O nome do plano.
            saldo: O saldo do plano.
        """
        self.__nome = nome  # Atributo nome encapsulado
        self.__saldo = saldo  # Atributo saldo encapsulado

    def verificar_saldo(self):
        """
        Retorna o saldo do plano.
        """
        return self.__saldo

    def mensagem_personalizada(self):
        """
        Retorna uma mensagem personalizada com base no saldo.
        """
        if self.__saldo < 10:
            return f"Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return f"Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return f"Seu saldo está razoável. Aproveite o uso moderado do seu plano."


class UsuarioTelefone:
    """
    Representa um usuário de telefone com nome e plano.
    """

    def __init__(self, nome, plano):
        """
        Inicializa um novo usuário de telefone.

        Args:
            nome: O nome do usuário.
            plano: O plano do usuário (objeto PlanoTelefone).
        """
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        """
        Verifica o saldo do usuário e gera uma mensagem personalizada.
        """
        saldo = self.plano.verificar_saldo()  # Acesando o saldo através do método
        mensagem = self.plano.mensagem_personalizada()  # Obtendo a mensagem
        return saldo, mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)

class UsuarioTelefone:
    """
    Representa um usuário de telefone com nome, número, plano e saldo.
    """

    def __init__(self, nome, numero, plano, saldo_inicial):
        """
        Inicializa um novo usuário de telefone.

        Args:
            nome: O nome do usuário.
            numero: O número de telefone do usuário.
            plano: O plano do usuário (objeto Plano).
            saldo_inicial: O saldo inicial do usuário.
        """
        self.__nome = nome
        self.__numero = numero
        self.plano = plano
        self.plano.saldo = saldo_inicial  # Define o saldo inicial do plano

    def fazer_chamada(self, destinatario, duracao):
        """
        Faz uma chamada telefônica para outro usuário.

        Args:
            destinatario: O número de telefone do destinatário.
            duracao: A duração da chamada em minutos.

        Returns:
            Uma mensagem indicando o sucesso da chamada ou a falta de saldo.
        """
        custo_chamada = self.plano.custo_chamada(duracao)
        if self.plano.saldo >= custo_chamada:
            self.plano.deduzir_saldo(custo_chamada)
            return (
                f"Chamada para {destinatario} realizada com sucesso. "
                f"Saldo: ${self.plano.saldo:.2f}"
            )
        else:
            return "Saldo insuficiente para fazer a chamada."


class Plano:
    """
    Representa o plano de um usuário de telefone.
    """

    def __init__(self):
        """
        Inicializa um novo plano com saldo inicial zero.
        """
        self.saldo = 0.0

    def custo_chamada(self, duracao):
        """
        Calcula o custo de uma chamada.

        Args:
            duracao: A duração da chamada em minutos.

        Returns:
            O custo da chamada.
        """
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        """
        Deduz um valor do saldo do plano.

        Args:
            valor: O valor a ser deduzido.
        """
        self.saldo -= valor


# Entradas do usuário
nome = input()
numero = input()
saldo_inicial = float(input())
destinatario = input()
duracao = int(input())

# Criação dos objetos Plano e UsuarioTelefone
plano_usuario = Plano()  # Cria um objeto Plano
usuario = UsuarioTelefone(nome, numero, plano_usuario, saldo_inicial)  # Cria o usuário

# Realiza a chamada
mensagem = usuario.fazer_chamada(destinatario, duracao)
print(mensagem)