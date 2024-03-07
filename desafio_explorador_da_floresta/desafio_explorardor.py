# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input('Digie a quantidade de passo: '))
n = quantidade_passos
#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
if n == 0:
  print("Nenhum passo dado na floresta.")
#Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
if n == 1:
  print(f"Explorador: {n} passo.")
  
if n > 1:
  
  for i in range(n+1):
#Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
    if i > 0 and i == 1:
      print(f"Explorador: {i} passo")
    if i > 1:
      print(f"Explorador: {i} passos")
      
        
        

