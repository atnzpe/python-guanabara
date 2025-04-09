# IMporta a biblioteca numpy

import numpy as np


class LinearRegression:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # variavel privada é um método privado
        self.__correlation_coefficient = self.__correlacao()  # correlaçao
        self.__inclination = self.__inclinacao()  # inclinacão
        self.__intercept = self.__interceptacao()  # interceptação

    # Métodos

    def __correlacao(self):
        covariacao = np.cov(self.x, self.y, bias=True)[0][1]
        variancia_x = np.var(self.x)
        variancia_y = np.var(self.y)

        return covariacao / np.sqrt(variancia_x * variancia_y)

    def __inclinacao(self):
        std_x = np.std(self.x)
        std_y = np.std(self.y)

        return self.__correlation_coefficient * (std_y / std_x)

    def __interceptacao(self):
        media_x = np.mean(self.x)
        media_y = np.mean(self.y)

        return media_y - media_x * self.__inclination

    def previsao(self,valor):
        
        return self.__intercept + (self.__inclination * valor)
    
    
    #Exemplo de Calculo para teste
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,8,10])
    
lr = LinearRegression(x,y)

preview = lr.previsao(6)

print("A previsao é: ", preview)
