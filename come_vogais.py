word = input('Digita um palavra: ')

vowels = 'aeiou'

lista_consoantes = [i for i in word if i not in vowels]
lista_vogais = [i for i in word if i in vowels]

print(f'Consoantes {lista_consoantes}')
print(f'Vogais {lista_vogais}')