# Criando a classe Animal - Super-classe
class Animal():

    def __init__(self):
        print("Animal criado")

    def Identif(self):
        print("Animal")

    def comer(self):
        print("Comendo")

# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")

    def Identif(self):
        print("Cachorro")

    def latir(self):
        print("Au Au!")

# Criando um objeto (Instanciando a classe)
rex = Cachorro()

# Executando o método da classe Cachorro (sub-classe)
rex.Identif()

# Executando o método da classe Animal (super-classe)
rex.comer()

# Executando o método da classe Cachorro (sub-classe)
rex.latir()
