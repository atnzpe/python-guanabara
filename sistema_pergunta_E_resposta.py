# Exercício - Sistema de Perguntas e Respostas

import random

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5+5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','3','20'],
        'Resposta': '5',
    }
]


def sorteia_pergunta(lista_perguntas):
    pergunta_atual = random.choice(lista_perguntas)
    print(pergunta_atual['Pergunta'])
    print ('Escolha um Opção:')
    for chave in pergunta_atual['Opções']:
        print(f'> {chave}')

    while True:
        resposta = input('Digite sua Escolha: ')

        if resposta in pergunta_atual['Resposta']:
            print(f'Certa Resposta!')
            break
        else:
            print('Voce errou!')
            break

    #return print(pergunta_atual['Pergunta'])



sorteia_pergunta(perguntas)



#for chave in pergunta_atual:
    #print (pergunta_atual[chave])



#print(perguntas[Pergunta])

