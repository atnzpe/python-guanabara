"""
Cenário
Os Beatles foram um dos grupos de música mais populares dos anos 60, e a banda mais vendida na história. Algumas pessoas consideram que eles são o ato mais influente da era do rock. Na verdade, eles foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.

A banda passou por muitas mudanças na formação, culminando em 1962 com a formação de John Lennon, Paul McCartney, George Harrison e Richard Starkey (mais conhecido como Ringo Starr).


Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

#etapa 1: criar uma lista vazia chamada beatles;
#etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
#etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
#etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
#etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.

"""

# etapa 1: criar uma lista vazia chamada beatles;
beatles = []
print("Etapa 1:", beatles)
print()

# etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;

# Criei uma lista com os nomes a serem inseridos
members = ["John Lennon", "Paul McCartney", "George Harrison"]

# Executei o FOR e utiliza o metodo append
for members in members:
    beatles.append(members)

# No exemplo abaixo Usando list comprehension ficaria assim
# beatles = [members for members in members]

print("Etapa 2:", beatles)

# etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
for artist in beatles:
    artist_Stu = "Stu Sutcliffe"
    artist_Pete = "Pete Best"
    while artist_Stu not in beatles and artist_Pete not in beatles:
        r = int(
            input(
                "\nDeseja inserir os Artistas Stu Sutcliffe e Pete Best?\n[1]Sim\n[2]Não\nDigite sua resposta: "
            )
        )
        if r == 1:
            beatles.append(artist_Stu)
            beatles.append(artist_Pete)
            print(f"\nParabens!\n{artist_Pete} e {artist_Stu} inseridos com sucesso!\n")

        else:
            print(
                f"\nVocê optou por não inserir {artist_Stu} e {artist_Pete} na lista de Menbros dos Beatles!"
            )

print("Etapa 3:", beatles)


# etapa 4

print("Etapa 4:", beatles)

# passo 5

print("Etapa 5:", beatles)


# testando o tamanho da lista

("o fabuloso", len(beatles))
