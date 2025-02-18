from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print(vec[0], vec[1])

    vec2 = Vector([3, 1])

    print(vec - vec2)
    print(vec * 3)
    print(4 * vec)
    print(-vec)
    print(+vec)
    zero2 = Vector.zero(2)
    print(zero2)
    print(vec.norm())
    print(vec.normalioze())
    print(vec.normalioze().norm())
    print(vec2.normalioze())
    print(vec2.normalioze().norm())


    try:
        zero2.normalioze()
    except ZeroDivisionError:
        print("can not")

    print(vec.dot(vec2))
