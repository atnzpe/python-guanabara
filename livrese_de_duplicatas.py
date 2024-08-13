'''
Livre-se de Duplicatas!
Escreva uma função chamada unique. A função deve aceitar um parâmetro, que é uma lista com qualquer número de elementos dentro. O valor padrão para o parâmetro deve ser uma lista vazia ([]).

A função deve retornar uma nova lista com todos os elementos duplicados removidos. A função deve preservar a ordem original dos elementos.

Exemplo 1: para unique([1, 1, 4, 5, 1]), a saída deve ser [1, 4, 5]
Exemplo 2: para unique(['Mark', 'Mark', 'John', 'Anne']), a saída deve ser ['Mark', 'John', 'Anne']

'''


def unique(lista='[]'):
    new_list = []
    for i in lista:
        if i not in new_list:
            new_list.append(i)
    
    return new_list
    


love = unique([1, 1, 4, 5, 1]) 
peace = unique(['Mark', 'Mark', 'John', 'Anne'])

print(love, ' and ', peace)
