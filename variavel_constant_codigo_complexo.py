"""
Constante = "Variáveis" imutáveis
Muitas condições no mesmo if (ruim)
    Muitos blocos aninhados deixando o código complexo(ruim)

"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local do carro na estrada

RADAR_1 = 60 # VELOCIDADE MÁXIMA RADAR 1
LACAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 #a distancia onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou maior que velocidade radar 1')
