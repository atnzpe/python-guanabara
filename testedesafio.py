def prompt_avaliado(prompt):
    palavra_chave =["amor","carinho","paz"]
    
    for palavra_chave in palavra_chave:
        if palavra_chave in prompt:
            return f"Deu certo"
        else:
            return f"Deu errado"
            
prompt_user = input("Digite aqui sua entrada: ")

result = prompt_avaliado(prompt_user)

print(result) 