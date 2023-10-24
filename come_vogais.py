word = input('Digita um palavra: ')

vowels = 'aeiou'


lista_consoantes = [i for i in word if i not in vowels and i != " "]
lista_vogais = [i for i in word if i in vowels]
espacos = [i for i in word if i == " "]


print(f'Total de Consoantes {len(lista_consoantes)} sua lista: {lista_consoantes}')
print(f'Total de Vogais é {len(lista_vogais)} e sua lista: {lista_vogais}')
print(f'Tota de espacos {len(espacos)}')