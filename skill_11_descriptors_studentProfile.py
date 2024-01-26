from icecream import ic

class scoreField:
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(f'scoreField_{self.name}')
    
    def __set__(self, instance, value):
        if not type(value) == int:
            raise TypeError(f"Value should be a Int")

        if self.min < value < self.max:
            instance.__dict__[f'scoreField_{self.name}'] = value

    def __delete__(self, instance):
        del instance.__dict__[f'scoreField_{self.name}']


class textField:
    def __init__(self, length) -> None:
        self.length = length

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(f'textField_{self.name}')
    
    def __set__(self, instance, value):
        if not type(value) == str:
            raise TypeError(f"Value should be a Int")

        if len(value) <= self.length:
            instance.__dict__[f'textField_{self.name}'] = value
        else:
            raise ValueError(f"Now acceptable value")

    def __delete__(self, instance):
        del instance.__dict__[f'textField_{self.name}']

class studentProfile:
    name = textField(100)
    gre_score = scoreField(130, 340)
    sat_score = scoreField(400, 1600)

if __name__ == "__main__":
    s1 = studentProfile()
    s1.name = "Prinu"
    s1.gre_score = 200
    s1.sat_score = 500
    ic(s1.__dict__)




