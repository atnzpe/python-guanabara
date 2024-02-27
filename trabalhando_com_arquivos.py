file = open("./text.txt")
cont = file.read()
# print(cont)
file.close()


file = open("./text.txt")

lista = []

for line in file.readlines():
    lista.append(line)
    # print(line)

# print(lista)
file_new = open("./newtext.txt", "w")

for text in lista:
    file_new.write('new_'+text)

file_new.close()

file_new = open("./newtext.txt")
cont = file_new.read()
print(cont)
file_new.close()

# a = int(input())

# file = open("/book.txt")
# print(file.read(a))
