# 3 Crie um programa que responda "se você pode atravessar a rua"'
# em qualquer local da rua. Você pode atravessar a rua se o "sinal estiver
# #vermelho" OU "se não houver nenhum carro vindo da direita" E "nem da esquerda".
# #Altere as variáveis para verificar se o programa esta correto.
# #Mostre na saída do programa o valor lógico.



while True:

    print(
        """
+============================================+
|                                            |
| Responda as perguntas antes de atravessar. |
|                                            |      
+============================================+
"""
    )

    sinal_vermelho = input(
        '''
        Sinal esta vermelho?
        [S] - Sim
        [N] - Não
        [Q] - Sair ou Voltar
        
        Digite sua Resposta: '''
    ).upper()

    if sinal_vermelho == "S":
        sinal_vermelho = True 
    elif sinal_vermelho == "Q":
        break
    else:
        sinal_vermelho = False

    carro_vindo_direita = input(
        '''
        Carro Vindo na direita?
        [S] - Sim
        [N] - Não
        
        Digite sua Resposta: '''
    ).upper()

    carro_vindo_direita = True if carro_vindo_direita == "S" else False

    carro_vindo_esquerda = input(
        '''
        Carro Vindo na esquerda?
        [S] - Sim
        [N] - Não
        
        Digite sua Resposta: '''
    ).upper()

    carro_vindo_esquerda = True if carro_vindo_esquerda == "S" else False

    pode_atravessar = sinal_vermelho or not carro_vindo_direita and not carro_vindo_esquerda

    if pode_atravessar:
        print('\nPode Atravessar a rua.')
        break

    else:
        print('\nFique aguardando e quando possivel responda as perguntas antes de atravessar!')
