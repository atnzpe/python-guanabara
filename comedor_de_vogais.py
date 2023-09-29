user_word = input('Digite uma palagra: ').upper()
vogais = 'AEIOU'
vogais_comidas = []

for letter in user_word:
    if letter in vogais:
        vogais_comidas.append(letter)
        continue
    print(letter)

print(vogais_comidas)
print(f'Total de Vogais comidas foram {len(vogais_comidas)}')