import os

secret_word = input('Digite a palavra secrete: ')
word_check = ''
size_secrete_word = len(secret_word)

for i in range(size_secrete_word):
    print('Limpando a Tela')
    os.system("cls")

while True:
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in secret_word:
        word_check += letra_digitada

    formed_word = ''
    for letra_secreta in secret_word:
        if letra_secreta in word_check:
            formed_word += letra_secreta
            
        else:
            formed_word += '*'
           
    print(formed_word)
