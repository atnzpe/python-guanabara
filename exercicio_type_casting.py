# The first activity is asking you to create a program that contains a variable of type string with a
# number indicating how much money you have in the bank. Then, you should subtract one thousand from
# this value and display the result in the program's output.

#Atividades 1 
#Crie um programa que possui uma variável do "tipo string" 
#contendo um número que indique quanto você tem no banco. 
#Em seguida desconte mil deste valor e mostre na saída do programa. 


print(
    """
+====================================================================+
|                                                                    |
| Atividades 1                                                       |
| Crie um programa que possui uma variável do "tipo string"          |
| contendo um número que indique quanto você tem no banco.           |
| Em seguida desconte mil deste valor e mostre na saída do programa. |
|                                                                    |
+====================================================================+
"""
)

saldo = "10000"
saldo_incial = saldo
desconto =  1000
saldo_final = int(saldo) - desconto 

print(f'O saldo incial era de R$ {saldo} teve um {desconto=} e o {saldo_final}', type(saldo))


#2 Crie um programa que indique se seu saldo bancário esta zerado (valor lógico).
# Declare uma variável para guardar seu saldo bancário.

saldo_bancario_zerado = bool(1)
estou_sem_credito = bool(0)

if saldo_bancario_zerado or estou_sem_credito:
    print("Estou liso!")
    print(f"{saldo_bancario_zerado=}",type(saldo_bancario_zerado), type(estou_sem_credito))
    
else:
    print('liso é tu besta!')
    print(f"{saldo_bancario_zerado=}",type(saldo_bancario_zerado))


# 
# 3 Crie um programa que contenha sua altura, 
# mas deve somente mostrar a parte inteira de sua altura na saída do programa,
# pois queremos uma estimativa.

altura = 1.78
altura_inteiro = int(altura)

print(f"{altura=} e {altura_inteiro=}")