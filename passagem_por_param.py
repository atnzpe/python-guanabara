def mensagem_curta(nome):
    print('Executa a Funçõa Mensagem')
    return f'Retorna oi {nome}'

def mensagem_longa(nome):
    print ('Executa a mensagem longa')
    return f'Retorna Olá tudo bem com você {nome}'

def executar(funcao, nome):
    print('Executando a funcao Executar')
    return funcao(nome)

nome = input('Qual o seu nome? ')

print(executar(mensagem_curta, nome))
print(executar(mensagem_longa, nome))


