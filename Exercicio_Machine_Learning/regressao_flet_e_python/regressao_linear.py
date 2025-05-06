# Importa a biblioteca NumPy, essencial para operações com arrays e matrizes.  O 'as np' cria um alias para facilitar o uso.
import numpy as np

class LinearRegression:
    """
    Esta classe implementa uma regressão linear simples para prever o valor de uma variável dependente (y) com base em uma variável independente (x).
    """
    def __init__(self, x, y):
        """
        Construtor da classe. Inicializa a classe com os dados de entrada.

        Args:
            x (numpy.ndarray): Array NumPy contendo os valores da variável independente.
            y (numpy.ndarray): Array NumPy contendo os valores da variável dependente.
        """
        # Atributos da classe que armazenam os dados de entrada.
        self.x = x
        self.y = y

        # Calcula e armazena os parâmetros da regressão linear no momento da criação do objeto.  Usando __ para indicar que são atributos privados, acessíveis apenas internamente à classe.
        self.__correlation_coefficient = self.__correlacao()  # Coeficiente de correlação
        self.__inclination = self.__inclinacao()  # Inclinação (coeficiente angular) da reta
        self.__intercept = self.__interceptacao()  # Intercepto (coeficiente linear) da reta


    def __correlacao(self):
        """
        Calcula o coeficiente de correlação entre as variáveis x e y.

        Returns:
            float: O coeficiente de correlação entre x e y.
        """
        # Calcula a covariância entre x e y usando a função cov do NumPy. bias=True indica que a covariância populacional deve ser calculada.
        covariacao = np.cov(self.x, self.y, bias=True)[0][1] 
        # Calcula a variância de x usando a função var do NumPy.
        variancia_x = np.var(self.x)
        # Calcula a variância de y usando a função var do NumPy.
        variancia_y = np.var(self.y)

        # Calcula o coeficiente de correlação usando a fórmula: covariância / (desvio_padrão(x) * desvio_padrão(y))
        return covariacao / np.sqrt(variancia_x * variancia_y)


    def __inclinacao(self):
        """
        Calcula a inclinação (coeficiente angular) da reta de regressão.

        Returns:
            float: A inclinação da reta de regressão.
        """
        # Calcula o desvio padrão de x usando a função std do NumPy.
        std_x = np.std(self.x)
        # Calcula o desvio padrão de y usando a função std do NumPy.
        std_y = np.std(self.y)

        # Calcula a inclinação usando a fórmula: coeficiente_de_correlação * (desvio_padrão(y) / desvio_padrão(x))
        return self.__correlation_coefficient * (std_y / std_x)


    def __interceptacao(self):
        """
        Calcula o intercepto (coeficiente linear) da reta de regressão.

        Returns:
            float: O intercepto da reta de regressão.
        """
        # Calcula a média de x usando a função mean do NumPy.
        media_x = np.mean(self.x)
        # Calcula a média de y usando a função mean do NumPy.
        media_y = np.mean(self.y)

        # Calcula o intercepto usando a fórmula: média(y) - inclinação * média(x)
        return media_y - media_x * self.__inclination


    def previsao(self, valor):
        """
        Faz uma previsão para um novo valor de x usando a equação da reta de regressão.

        Args:
            valor (float): O novo valor de x para o qual se deseja fazer a previsão.

        Returns:
            float: A previsão para o valor de y correspondente ao valor de x fornecido.
        """
        # Usa a equação da reta: y = intercepto + inclinação * x
        return self.__intercept + (self.__inclination * valor)


# Exemplo de uso da classe LinearRegression
x = np.array([1, 2, 3, 4, 5]) # Array NumPy com os valores da variável independente.
y = np.array([2, 4, 5, 8, 10]) # Array NumPy com os valores da variável dependente.

lr = LinearRegression(x, y) # Cria uma instância da classe LinearRegression.

preview = lr.previsao(6) # Faz uma previsão para x = 6.

print("A previsao é: ", preview) # Imprime a previsão.