from playLA.Matrix import Matrix

if __name__ == '__main__':

    matrix = Matrix([ [1,2], [3,4]])
    print(matrix)
    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.size())
    print(len(matrix))
    print(matrix[0, 1])