from playLA.Vector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def row_vector(self, index):
        return Vector(self._values[index])

    def col_vector(self, index):
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    def size(self):
        r, c = self.shape()
        return r * c

    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        return self.shape()[1]


    def shape(self):
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__