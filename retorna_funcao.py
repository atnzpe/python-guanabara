def calculadora(operacao):
    def soma(a, b):
        return f'Soma {a} + {b} = {(a+b)}'
    
    def sub(a, b):
        return f'Subtração {a} - {b} = {(a-b)}'
    
    def mult(a, b):
        return f'Multiplicaçõa {a} * {b} = {(a*b)}'
    
    def div(a, b):
        return f'Divisão de {a} / {b} = {(a/b)}'
    
    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return mult
        case '/':
            return div
        
def menu():
    menu = ''' Escolha uma opção:
    [+] Soma 
    [-] Subtração
    [*] Multiplicação
    [/] Divisão
    ->  '''
    return input(menu)

operacao = menu()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

result = calculadora(operacao)(n1,n2)

print(result)
