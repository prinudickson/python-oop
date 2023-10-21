from icecream import ic

class MercedesBenz:
    model = "z"
    weight = 2300
    height = 150
    doors = 4
    wheels = 4

    def __init__(self, color="black"):
        self.color = color
        
    def drive(self):
        ic(f"A Mercedez is driving. It is {self}\n")

ic(MercedesBenz.__dict__)

a = MercedesBenz()

ic(a.__dict__)

MercedesBenz.color = "Blue"

ic(MercedesBenz.__dict__)

ic(a.color)

ic(dir(a))


m1 = MercedesBenz()
m2 = MercedesBenz()

ic(m1.__dict__)
ic(m2.__dict__)


objs = [m1, m2]

attribs = ["color", "doors"]
vals = ["Red",4]

for obj in objs:
    for attr, val in zip(attribs, vals):
        setattr(obj, attr, val) 

ic(m1.__dict__)
ic(m2.__dict__)

