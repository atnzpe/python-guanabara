frase_ou_palavra = input ("Digita qualquer coisa: ")

#print(new_string.count())

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase_ou_palavra):
    letra_atual = frase_ou_palavra[i]
    
    if letra_atual == '':
        i += 1
        continue
    
    qtd_atual = frase_ou_palavra.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual

    #print(letra_atual,qtd_vezes_cacter_apareceu)
    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_que_apareceu_mais_vezes}" que apreceu'
      f'"{qtd_apareceu_mais_vezes}X"')    