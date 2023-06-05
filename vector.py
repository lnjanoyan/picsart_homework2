class Vector:
    def __init__(self, x_coord: int, y_coord: int, z_coord: int = 0):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __pos__(self):
        return self

    def __abs__(self):
        self.x = (self.x ** 2) ** 0.5
        self.y = (self.y ** 2) ** 0.5
        self.z = (self.z ** 2) ** 0.5
        return Vector(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, other):
        if (self.z == 0 and other.z == 0) or (self.z != 0 and other.z != 0):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return "Non equal length"

    def __sub__(self, other):
        if (self.z == 0 and other.z == 0) or (self.z != 0 and other.z != 0):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return "Non equal length"

    def __mul__(self, other):
        if isinstance(other, int):
            self.x = other * self.x
            self.y = other * self.y
            if self.z == 0:
                return Vector(self.x, self.y)
            self.z = other * self.z
            return Vector(self.x, self.y, self.z)
        elif isinstance(other, Vector):
            if (self.z == 0 and other.z == 0) or (self.z != 0 and other.z != 0):
                return self.x * other.x + self.y * other.y + self.z * other.z
            return 'vectors lengths are different'

    def __truediv__(self, other):
        raise NotImplementedError("True division not supported for vectors")

    def __floordiv__(self, other):
        raise NotImplementedError("Floor division not supported for vectors")

    def __mod__(self, other):
        raise NotImplementedError("Modulus operation not supported for vectors")

    def __divmod__(self, other):
        raise NotImplementedError("divmod() not supported for vectors")

    def __pow__(self, power, modulo=None):
        raise NotImplementedError("Exponentiation not supported for vectors")

    def __iadd__(self, other):
        if (self.z == 0 and other.z == 0) or (self.z != 0 and other.z != 0):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        return "Non equal lengths"

    def __isub__(self, other):
        if (self.z == 0 and other.z == 0) or (self.z != 0 and other.z != 0):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        return "Non equal lengths"

    def __imul__(self, scalar):
        if isinstance(scalar, int):
            self.x *= scalar
            self.y *= scalar
            self.z *= scalar
            return self
        return 'Non scalar value'

    def __itruediv__(self, other):
        raise NotImplementedError("True division not supported for vectors")

    def __ifloordiv__(self, other):
        raise NotImplementedError("Floor division not supported for vectors")

    def __imod__(self, other):
        raise NotImplementedError("Modulus operation not supported for vectors")

    def __ipow__(self, other):
        raise NotImplementedError("Exponentiation not supported for vectors")

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"Vector({self.x}.{self.y},{self.z})"

    def __format__(self, format_spec):
        return f"({self.x},{self.y},{self.z})"

    def __len__(self):
        return '1 dimensional vector'

    def __getitem__(self, coord):
        if coord == 'x':
            return self.x
        elif coord == 'y':
            return self.y
        elif coord == 'z':
            return self.z
        else:
            print('No such coordinate, only x,y,z.')

    def __setitem__(self, coord, value):
        if coord == 'x':
            self.x = value
        elif coord == 'y':
            self.y = value
        elif coord == 'z':
            self.z = value
        else:
            print('No such coordinate, only x,y,z.')

    def __delitem__(self, key):
        raise TypeError("Vectors do not support item deletion")

    def __contains__(self, item):
        if item == self.x or item == self.y or item == self.z:
            return True
        return False


vec1 = Vector(1, 2, 2)
vec2 = Vector(-1, 2, 4)
print(vec1 + vec2, vec1 * 2, 5 in vec2)
