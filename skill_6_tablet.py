from icecream import ic

class tablet:

    MODELS = {
        "lite": {
            "base_storage": 32,
            "added_storage": 0,
            "memory": 2
        },
        "pro": {
            "base_storage": 64,
            "added_storage": 0,
            "memory": 3
        },
        "max": {
            "base_storage": 128,
            "added_storage": 0,
            "memory": 4
        },
        
    }

    def __init__(self, model) -> None:

        model = model.lower().strip()

        if model not in list(self.MODELS.keys()):
            raise ValueError("Unrecognised Model - Cannot be added")
        
        specs = self.MODELS[model]
    
        self._model = model
        self._base_storage = specs["base_storage"]
        self._added_storage = specs["added_storage"]
        self._memory = specs["memory"]

    def add_storage(self, x):
        if self._added_storage + x + self._base_storage <= 1024:
            self._added_storage = self._added_storage + x
            # self.calculate_storage()
        else:
            raise ValueError("This is not possible")
        return "added storage added"

    @property
    def storage(self):
        return self._base_storage + self._added_storage

    @storage.setter
    def storage(self, y):
        if 0 < (y - self._base_storage)  and (y - self._base_storage) <= 1024:
            self._added_storage = y - self._base_storage
        else:
            raise ValueError("Not Possible")
        
    @property
    def memory(self):
        return self._memory
    
    @property
    def base_storage(self):
        return self._base_storage

    def __repr__(self) -> str:
        return f"tablet(model='{self._model}', base_storage='{self._base_storage}', added_storage='{self._added_storage}', memory='{self._memory}')"
    

if __name__ == "__main__":
    t = tablet("pro")
    
    ic(t.__dict__)
    t.add_storage(943)
    ic(t.__dict__)
    t.storage = 1000    
    ic(t.__dict__)
    ic(t.storage)
    ic(t.memory)
    ic(t.base_storage)
    ic(t)