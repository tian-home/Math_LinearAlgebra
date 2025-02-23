from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':

    matrix = Matrix([ [1,2], [3,4]])
    print(matrix)
    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.size())
    print(len(matrix))
    print(matrix[0, 1])

    matrix2 = Matrix([[5,6],[7,8]])

    print(matrix+matrix2)
    print(matrix-matrix2)
    print(matrix * 2)
    print(2 * matrix2)
    print(Matrix.zero(4,3))

    T = Matrix([[1.5,0],[0,2]])
    p = Vector([5,3])
    print(T.dot(p))

    P = Matrix([[0,4,5],[0,0,3]])
    print(P.T())

    I = Matrix.identity(2)
    print(I)
    print(matrix.dot(I))
    print(I.dot(matrix))



