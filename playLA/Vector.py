from ._global import EPSILON
import math

class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        return math.sqrt(sum(e**2 for e in self))

    def normalioze(self):
        # return Vector([e/self.norm() for e in self])
        # return 1/self.norm() * Vector(self._values)
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero")
        return Vector(self._values) / self.norm()

    def __add__(self, another):
        assert len(self) == len(another), "Error"
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        assert len(self) == len(another), "Error"
        return Vector([a - b for a, b in zip(self, another)])

    def dot(self, another):
        assert len(self) == len(another), "Error"
        return sum( a*b for a,b in zip(self, another))

    def __mul__(self, k):
        return Vector([k*e for e in self])

    def __rmul__(self, k):
        return Vector([k*e for e in self])

    def __truediv__(self, k):
        return (1/k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
