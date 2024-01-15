from icecream import ic

class point3d:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self) -> str:
        instance_name = "".join([t.__name__ for t in type(self).__mro__[:1]])
        return f"{instance_name}({self.x}, {self.y}, {self.z})"

class coloredPoint(point3d):
    __slots__ = ("color")

    def __init__(self, x, y, z, color) -> None:
        super().__init__(x, y, z)
        self.color = color

class shapePoint(point3d):
    __slots__ = ("shape")

    def __init__(self, x, y, z, shape) -> None:
        super().__init__(x, y, z)
        self.shape = shape

if __name__ == "__main__":
    p = point3d(1,2,3)
    ic(p)
    
    cp = coloredPoint(1,2,3, color="blue")
    ic(cp)
    
    sp = shapePoint(1,2,3, shape="square")
    ic(sp)
    
    ic(sp.__dict__)