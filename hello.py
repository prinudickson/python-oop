class MercedesBenz:
    model = "z"
    weight = 2300
    height = 150
    doors = 4
    wheels = 4


print(MercedesBenz.__dict__)

a = MercedesBenz()

print(a.__dict__)

MercedesBenz.color = "Blue"

print(MercedesBenz.__dict__)

print(a.color)

print(dir(a))


