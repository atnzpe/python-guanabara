pessoa = {
    'nome':'Aline',
    'sobrenome':'Atanazio'
}

dados_pessoa = {
    'idade': 16,
    'Pai': 'Gleyson'
}

#desempacota o dicionario usando os dois asteriscos
dados_pessoa_completa = {**pessoa, **dados_pessoa}

print(dados_pessoa_completa)

for chave,valor in dados_pessoa_completa.items():
    print(chave,valor)