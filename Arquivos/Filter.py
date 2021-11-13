# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um número como parâmetro. Retornará
# Falso de for ímpar e True se for par.
verificaPar(35)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

list(filter(verificaPar, lista))
list(filter(lambda x: x%2==0, lista))

list(filter(lambda num: num > 8, lista))
