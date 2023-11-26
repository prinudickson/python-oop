from icecream import ic
from functools import total_ordering
from math import sqrt

@total_ordering
class Vector:
    """_summary_
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str: 
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Operation only supported between two instances of vectors")
        return Vector(self.x+other.x, self.y+other.y,self.z+other.z )
    
    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError("Scaling is only possible between a Vector and Scalar")
        return Vector(self.x*other, self.y*other, self.z*other)
    
    def __rmul__(self, other):
        return self*other

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __le__(self, other):
        if not isinstance(other, Vector):
            return TypeError("must be a Vector")
        
        return abs(self) < abs(other)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __getitem__(self, item):
        #if isinstance(type, str) and item.lower() in ['x', 'y', 'z']:
        if isinstance(item, str) and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")
        else:
            NotImplemented


if __name__ == "__main__":
    v1 = Vector(x=1, y=2, z=3)
    ic(v1)
    v2 = Vector(x=2, y=3, z=4)
    ic(v2)
    ic(bool(v2))
    v3 = Vector(x=0, y=0, z=0)
    ic(v3)
    ic(bool(v3))
    ic(v1+v2)
    ic(v1*3.3)
    ic(3*v1)

    ic(v1 < v2)
    ic(abs(v1))
    ic(abs(v2))
    ic(v1['x'])
    ic(v1["X"])
    ic(v1[1])