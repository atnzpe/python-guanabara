"""
Um tabuleiro de xadrez é composto de linhas e colunas.

Há oito linhas e oito colunas. 

Cada coluna é marcada com as letras de A a H. 
Cada linha é marcada com um número de um a oito.

A localização de cada campo é identificada por pares de letras e dígitos. Assim, sabemos que o canto inferior esquerdo do quadro (com a torre branca) é A1, enquanto o canto oposto é H8.

Vamos supor que somos capazes de usar os números selecionados para representar qualquer peça de xadrez. Também podemos assumir que cada linha no tabuleiro de tabuleiro é uma lista.

Veja o código abaixo

"""
'''row  = []

for i in range(8):
    row.append(peao_branco)
    
print(row)'''

my_list = [1, 2]
 
for v in range(2):
    my_list.insert(-1, my_list[v])
 
print(my_list)