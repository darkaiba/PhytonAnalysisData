# Criando uma classe chamada Livro
class Livro():

    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self):

        # Atributos de cada objeto criado a partir desta classe.
        # O self indica que estes são atributos dos objetos
        self.titulo = 'O Monge e o Executivo'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe")

    # Métodos são funções, que recebem como parâmetro atributos do objeto criado
    def imprime(self):
        print("Foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))

# Criando uma instância da classe Livro
Livro1 = Livro()

# Tipo do Objeto Livro1
type(Livro1)

# Atributo do objeto Livro1
print(Livro1.titulo)

# Método do objeto Livro1
Livro1.imprime()

# Criando a classe Livro com parâmetros no método construtor
class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe")

    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo, isbn))

# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("A Menina que Roubava Livros", 77886611)

print(Livro2.titulo)
# Método do objeto Livro2
Livro2.imprime("A Menina que Roubava Livros", 77886611)

# Criando a classe cachorro
class Cachorro():
    def __init__(self, raça):
        self.raça = raça
        print("Construtor chamado para criar um objeto desta classe")

# Criando um objeto a partir da classe cachorro
Rex = Cachorro(raça='Labrador')

# Criando um objeto a partir da classe cachorro
Golias = Cachorro(raça='Huskie')

# Atributo da classe cachorro, utilizado pelo objeto criado
print(Rex.raça)

# Atributo da classe cachorro, utilizado pelo objeto criado
print(Golias.raça)
