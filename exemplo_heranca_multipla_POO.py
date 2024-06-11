# Classe Pai
class Animal:
    # defino um construtor
    def __init__(self, nr_patas):
        self.nr_patas = nr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} igual a {valor}' for chave, valor in self.__dict__.items()])}"


# Classe filha de Animal
class Ave(Animal):
    # defino um construtor
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        # chama construtor PAI
        super().__init__(**kw)


# Classe Filha estende de animal
class Mamifero(Animal):
    # defino um construtor
    def __init__(self, cor_do_pelo, **kw):
        self.cor_do_pelo = cor_do_pelo
        # chama construtor PAI
        super().__init__(**kw)


# Classe filha de mamifero neta de animal
class Cachorro(Mamifero):
    pass


# Classe filha de mamifero neta de animal
class Gato(Mamifero):
    pass


# Classe filha de mamifero neta de animal
class Leao(Mamifero):
    pass


# Classe filha de Animal


# Classe que extende de mamifero e de ave

class Onintorrinco(Mamifero, Ave):
    pass


n_patas_gato = input("Qual o numero de patas do seu gato? ")
cor_do_pelo_gato = input("Qual a cor do pêlo? ")
n_patas_gato = int(n_patas_gato)

n_patas_o = input("Qual o numero de patas do Onintorrinco? ")
cor_do_pelo_o = input("Qual a cor do pêlo? ")
cor_do_bico_o = input("Qual a cor do bico? ")
n_patas_o = int(n_patas_o)

jose_gato = Gato(nr_patas=n_patas_gato, cor_do_pelo=cor_do_pelo_gato)
tony = Onintorrinco(nr_patas=n_patas_o, cor_do_pelo=cor_do_pelo_o, cor_bico=cor_do_bico_o)
print(jose_gato)
print(tony)
