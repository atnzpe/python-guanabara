def meu_decorador(funcao):
    def envelope():
        print('Pede para o usuario digitar o valor')
        funcao()
        print('Exibe uma mensagem de sucesso')
        
    return envelope

@meu_decorador
def funcao_que_decora():
    print('PEdiu a senha para validar!')
    
#funcao_que_decora = meu_decorador(funcao_que_decora) Modo sem o @meu_decorador
funcao_que_decora()