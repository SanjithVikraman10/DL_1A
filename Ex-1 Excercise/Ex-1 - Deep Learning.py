import tensorflow as tf

scalar = tf.constant(7)
scalar.ndim

vector = tf.constant([10, 10])
vector.ndim

matrix = tf.constant([[1, 2], [3, 4]])
print(matrix)
print('The number of dimensions of a matrix is: ' + str(matrix.ndim))

matrix = tf.constant([[1, 2], [3, 4]])
matrix1 = tf.constant([[2, 4], [6, 8]])

print(matrix + matrix1)
print(matrix1 - matrix)
print(matrix1 * matrix)
print(matrix1 / matrix)

matrix = tf.constant([[1, 2], [3, 4]])
print(matrix)
