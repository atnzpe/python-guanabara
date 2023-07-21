"""
Introdução ao try/except

try (tipo if) -> Tentar excutar o código
except (tipo else)-> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    numero_float = float (numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_str * 2:.0f}')
except:
    print('Impresso no bloco except')
    print('Isso não é um número')