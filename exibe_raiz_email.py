
#Crie um programa com um loop for e uma declaração de break.
#O programa deve iterar os caracteres em um endereço de e-mail, 
#sair do loop quando atingir o símbolo '@' e imprimir a peça antes de @ em uma linha.



email = input('Digte seu email. nome@provedor: ')

raiz_email = ""

for i in email:
    if i == '@':
        break
    raiz_email += i
print(f'A raiz do seu email é "{raiz_email}"')