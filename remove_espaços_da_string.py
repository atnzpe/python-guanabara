string = input('Digite sua String com espaços: ')
new_string = ""
n_string_strip = string.strip(" ")
maria = ""



for i in string:
    if i != " ":
        new_string += i

print('Strig Original')    
print(string)
print(len(string))

print('String com espaços removidos pelo for')  
print(new_string)
print(len(new_string))

print('String Sem espaços, no incio e no final, pelo  metodo Strip')  
print(n_string_strip)
print(len(n_string_strip))


        

