# 2 Crie um programa que responda "se você pode atravessar a rua" 
# na faixa de pedestres. Você pode atravessar a rua se o "sinal estiver 
# #vermelho" e "se não houver nenhum carro vindo da direita" E "nem da esquerda". 
# #Altere as variáveis para verificar se o programa esta correto. 
# #Mostre na saída do programa o valor lógico.

while True:
    
    print(3*'#','Responda as perguntas antes de atravessar.',3*'#')
    
    esta_na_faixa_pedestre = input(
        '''
        Você esta na Faixa de Pedestres?
        [S] - Sim
        [N] - Não
        
        Digite sua Resposta: '''
    ).upper()

    esta_na_faixa_pedestre = True if esta_na_faixa_pedestre == "S" else False
    

    sinal_vermelho = input(
        '''
        Sinal esta vermelho?
        [S] - Sim
        [N] - Não
        
        Digite sua Resposta: '''
    ).upper()

    sinal_vermelho = True if sinal_vermelho == "S" else False

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

    pode_atravessar = esta_na_faixa_pedestre and sinal_vermelho and not carro_vindo_direita and not carro_vindo_esquerda

    if pode_atravessar:
        print (f'\nPode Atravessar a rua {pode_atravessar}.')
        break

    else:
        print('\nFique aguardando e quando possivel responda as perguntas antes de atravessar!')