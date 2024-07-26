'''
PT-BR

Dicionário interativo
Escreva um programa que implemente um dicionário interativo simples. Comece solicitando ao usuário o seguinte:

Digite uma palavra em inglês ou EXIT: << coloque um espaço no final desta mensagem

Quando o usuário digitar EXIT em letras maiúsculas, encerre o programa com o seguinte:

Tchau!

Caso contrário, tente encontrar o equivalente em alemão no dicionário fornecido no exercício.

a. se a palavra estiver no dicionário, imprima: Tradução: {} << substitua {} pela palavra do dicionário
b. se a palavra não estiver no dicionário, imprima: Sem correspondência!

Você deve continuar solicitando novas palavras ao usuário com o mesmo prompt ('Digite uma palavra em inglês ou EXIT: ') até que o usuário forneça EXIT.

Aqui está um exemplo de como o programa poderia funcionar com a entrada do usuário mostrada em negrito:

Digite uma palavra em inglês ou EXIT: dog
Não há correspondência!
Digite uma palavra em inglês ou EXIT: face
Tradução: Gesicht
Digite uma palavra em inglês ou EXIT: EXIT
Tchau!

English

Interactive Dictionary
Write a program that implements a simple interactive dictionary. Start by prompting the user with the following:

Enter a word in English or EXIT: << put a space at the end of this message

When the user enters EXIT in capital letters, terminate the program with the following:

Bye!

Otherwise, try to find the German equivalent in the dictionary provided in the exercise.

a. if the word is in the dictionary, print: Translation: {} << replace {} with the word from the dictionary
b. if the word is not in the dictionary, print: No match!

You should keep asking the user for new words with the same prompt ('Enter a word in English or EXIT: ') until the user provides EXIT.

Here's an example of how the program could work with user input shown in the bold:

Enter a word in English or EXIT: dog
No match!
Enter a word in English or EXIT: face
Translation: Gesicht
Enter a word in English or EXIT: EXIT
Bye!

'''

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word = input("Enter a word in English or EXIT: ")
    
    if word != "EXIT":
        if word in sample_dict:
            print("Translation:",sample_dict[word])
        
        else:
            print('No match!')
            
    else:
        print("Bye!")
        break
        
            
        