# 1 Crie um programa que diga "se você precisar ir ao mercado". 
# #Você precisa ir ao mercado se "faltar comida" ou "se for sábado". 
# #Mostre na saída do programa o valor lógico, indicando sim ou não.



falta_comida = input(
    '''
    Esta faltando comida?
    [S] - Sim
    [N] - Não
    
    Digite sua Resposta: '''
).upper()

falta_comida = True if falta_comida == "S" else False

hoje_e_sabado = input(
    '''
    Hoje é sábado?
    [S] - Sim
    [N] - Não
    
    Digite sua Resposta: '''
).upper()

hoje_e_sabado = True if hoje_e_sabado == "S" else False

if falta_comida or hoje_e_sabado:
    print ('\nVocê precisa ir ao mercado.')

else:
    print(f'\nFique em casa porque {falta_comida=} e/ou {hoje_e_sabado=}')

#2 Crie um programa que responda "se você pode atravessar a rua" 
# #na faixa de pedestres. Você pode atravessar a rua se o "sinal estiver 
# #vermelho" e "se não houver nenhum carro vindo da direita" E "nem da esquerda". 
# #Altere as variáveis para verificar se o programa esta correto. 
# #Mostre na saída do programa o valor lógico.

