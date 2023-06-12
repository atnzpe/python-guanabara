#Leia o preço e mostre um novo preço com o acrescimo de 5%

price = float(input("Digite o preço do item: "))
new_price =  price-(price * 0.05)

print(f"Preço Antigo: R$ {price}\nPreço Atual: R$ {new_price}")