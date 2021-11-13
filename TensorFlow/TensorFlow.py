import tensorflow as tf

# Cria um tensor
# Esse tensor é adicionado como um nó ao grafo.
hello = tf.constant('Hello, TensorFlow!')
print(hello)

# Constantes
const_a = tf.constant(5)
const_b = tf.constant(9)
print(const_a)
# Soma
total = const_a + const_b

print(total)
# Criando os nodes no grafo computacional
node1 = tf.constant(5, dtype = tf.int32)
node2 = tf.constant(9, dtype = tf.int32)
node3 = tf.add(node1, node2)

# Executa o grafo
print("\nA soma do node1 com o node2 é:", node3)

# Tensores randômicos
rand_a = tf.random.normal([3], 2.0)
rand_b = tf.random.uniform([3], 1.0, 4.0)
print(rand_a, rand_b)
# Subtração
diff = tf.subtract(rand_a, rand_b)
print('\nSubtração entre os 2 tensores é: ', diff)

# Tensores
node1 = tf.constant(21, dtype = tf.int32)
node2 = tf.constant(7, dtype = tf.int32)

# Divisão
div = tf.math.truediv(node1, node2)
print('\nDivisão Entre os Tensores: \n', div)

# Criando tensores
tensor_a = tf.constant([[4., 2.]])
tensor_b = tf.constant([[3.],[7.]])

print(tensor_a, tensor_b)
# Multiplicação
# tf.math.multiply(X, Y) executa multiplicação element-wise
# https://www.tensorflow.org/api_docs/python/tf/math/multiply
prod = tf.math.multiply(tensor_a, tensor_b)
print('\nProduto Element-wise Entre os Tensores: \n', prod)

# Outro exemplo de Multiplicação de Matrizes
mat_a = tf.constant([[2, 3], [9, 2], [4, 5]])
mat_b = tf.constant([[6, 4, 5], [3, 7, 2]])
print(mat_a, mat_b)

# Multiplicação
# tf.linalg.matmul(X, Y) executa multiplicação entre matrizes
# https://www.tensorflow.org/api_docs/python/tf/linalg/matmul
mat_prod = tf.linalg.matmul(mat_a, mat_b)
print('\nProduto Element-wise Entre os Tensores (Matrizes): \n', mat_prod)
# Criado o mesmo tensor com tf.Variable() e tf.constant()
changeable_tensor = tf.Variable([10, 7])
unchangeable_tensor = tf.constant([10, 7])
print(changeable_tensor, unchangeable_tensor)
# Isso vai gerar erro - requer o método assign()
changeable_tensor[0] = 7
print(changeable_tensor)

# Isso vai funcionar
changeable_tensor[0].assign(7)
print(changeable_tensor)

# Isso vai gerar erro (não podemos alterar tensores criados com tf.constant())
unchangeable_tensor[0].assign(7)
#print(unchangleable_tensor)

# Tensor preenchido com 1
tf.ones(shape=(3, 2))
# Tensor preenchido com 0
tf.zeros(shape=(3, 2))

# Cria um tensor rank 4 (4 dimensões)
rank_4_tensor = tf.zeros([2, 3, 4, 5])
print(rank_4_tensor)

# Imprime atributos do tensor
print("Tipo de dado de cada elemento:", rank_4_tensor.dtype)
print("Número de dimensões (rank):", rank_4_tensor.ndim)
print("Shape do tensor:", rank_4_tensor.shape)
print("Elementos no eixo 0 do tensor:", rank_4_tensor.shape[0])
print("Elementos no último eixo do tensor:", rank_4_tensor.shape[-1])
print("Número total de elementos (2*3*4*5):", tf.size(rank_4_tensor).numpy())

# Obtém os 2 primeiros itens de cada dimensão
print(rank_4_tensor[:2, :2, :2, :2])

# Obtém a dimensão de cada índice, exceto o final
print(rank_4_tensor[:1, :1, :1, :])

# Cria um tensor e rank 2 (2 dimensões)
rank_2_tensor = tf.constant([[10, 7],
                             [3, 4]])

# Obtém o último item de cada linha
print(rank_2_tensor[:, -1])
