z = [0]
dictionary = {}
conjunto = set()
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return "falsy" if not valor else "truthy"


print(f'TESTE', falsy('TESTE'))
print(f'{z=}', falsy(z))

"""
print(f'{}', falsy())
print(f'{}', falsy('{}'))
print(f'{TESTE}', falsy('{T'))
print(f'{T', falsy('{TE))
print(f'{}', falsy('{}'))
print(f'{}', falsy('{}'))
print(f'{}', falsy('{}'))
print(f'{}', falsy('{}'))
print(f'{}', falsy('{
    """
