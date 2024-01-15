from icecream import ic

class point3d:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attr_final = ""

        if class_name != "point3d":
            additional_attr = self.__class__.__dict__["__slots__"]
            if isinstance(additional_attr, tuple) == 1:
                attr = additional_attr[0]
                attr_val = getattr(self, attr)
            elif isinstance(additional_attr, str):
                attr = additional_attr
                attr_val = getattr(self, attr)
            else:
                raise AttributeError("Cannot handle this!")
            
            attr_final = f", {attr}='{attr_val}'"
            
        return f"{class_name}({self.x}, {self.y}, {self.z}{attr_final})"

class coloredPoint(point3d):
    #making this slots definition to reflect as tuple
    #This will be tested in __repr__
    __slots__ = ("color", )

    def __init__(self, *args, color="black", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color

class shapePoint(point3d):
    #making this slots definition reflect as str
    #This will be tested in __repr__
    __slots__ = ("shape")

    def __init__(self, *args, shape="sphere", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.shape = shape

if __name__ == "__main__":
    p = point3d(1,2,3)
    ic(p)
    
    cp = coloredPoint(1,2,3, color="blue")
    ic(cp)
    
    sp = shapePoint(1,2,3, shape="square")
    ic(sp)
    
    #ic(sp.__dict__)