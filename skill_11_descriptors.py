from icecream import ic

class TextField:
    def __init__(self, length) -> None:
        self.length = length

    def __set_name__(self, owner, name):
        #ic(instance)
        ic("within_set_name_")
        ic(owner)
        self.name = name
        
    def __get__(self, instance, owner):
        ic("within_get_")
        ic(instance)
        ic(owner)
        return instance.__dict__.get(f"TextField_{self.name}")
    
    def __set__(self, instance, value):
        ic("within_set_")
        ic(instance)
        #ic(owner)
        if not type(value) == str:
            raise TypeError("Value should be Str")
        
        if len(value) > self.length:
            raise ValueError(f"Value cannot be larger than {self.length} characters")
        
        instance.__dict__[f"TextField_{self.name}"] = value

    def __delete__(self, instance):
        pass

class PersonTable:
    first_name = TextField(100)
    last_name = TextField(150)


if __name__ == "__main__":
    p = PersonTable()
    p.first_name = "Prinu"
    p.last_name = "Dickson"
    ic(p.__dict__)
    ic(p.first_name)
    ic(p.last_name)