import numpy as np

if __name__ == '__main__':

    A = np.array([[1,2], [3,4]])
    print(A)

    print(A.shape)
    print(A.T)

    print(A[1,1])

    print(A[0])
    print(A[:,1])

    B = np.array([[5, 6], [7, 8]])
    print(A+ B)
    print(A- B)
    print(10* A)

    print(A*B)

    print(A.dot(B))
    print(B.dot(A))

    p =np.array([10,100])

    print(A+p)
    print(A+1)

    print(A.dot(p))

    I = np.identity(2)
    print(I)
    print(A.dot(I))
    print(I.dot(A))

    invA = np.linalg.inv(A)
    print(invA)
    print(A.dot(invA))

    C = np.array([[1,2,3], [4,5,6]])
    np.linalg.inv(C)