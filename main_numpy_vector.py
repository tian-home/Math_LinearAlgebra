import numpy as np

if __name__ == '__main__':
    print(np.__version__)

    lst = [1, 2, 3]
    vec = np.array([1,2,3])
    print(np.zeros(5))
    print(np.full(5,666))
    print(vec)
    print(vec.size, len(vec))
    print(vec[1])
    print(vec[-1])
    print(vec[0:2])
    print(type(vec[0:2]))

    vec2 = np.array([4, 5, 6])

    print(vec + vec2)
    print(vec - vec2)
    print(vec * vec2)
    print(vec.dot(vec2))

    #取模
    print(np.linalg.norm(vec))
    #归一化
    print(vec / np.linalg.norm(vec))
    print (np.linalg.norm(vec / np.linalg.norm(vec)))
