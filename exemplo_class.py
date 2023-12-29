class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
n = input()
idd = input()
fido = Player(n, idd)
#print(fido.name)
fido.intro()