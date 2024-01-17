numbers = []
control = len(numbers)
while control < 5:
    n = int(input("Digite um numero: "))
    numbers.append(n)
    control = len(numbers)
    #if control <= 5:
        #break

        
print(numbers)
numbers[0] = 111
new_element = numbers[0]
print(numbers)
numbers[1] = numbers[4]
print(numbers)
del numbers[3]
print(numbers[-4])
numbers.remove
print(numbers)
numbers.append(new_element)
print(numbers)
numbers.insert(-2,new_element)
print(numbers)

#new_list = []
new = [new_list for new_list in range(5)]
print(new)



    
    