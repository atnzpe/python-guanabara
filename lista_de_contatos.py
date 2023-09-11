contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

entrada = input()

list_name = []

for name, age in contacts:
    list_name.append(name)
    if entrada == name:
        yes = f'{name} is {age}'
    else:
        no = 'Not Found'

if entrada in list_name:
    print(yes)
else:
    print(no)
