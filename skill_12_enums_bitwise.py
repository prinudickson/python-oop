from icecream import ic
from enum import auto, Flag
from datetime import datetime

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

class BaseUser:
    USER_ROLES = {
        "admin": Permission.READ | Permission.WRITE | Permission.EXECUTE,
        "user": Permission.READ,
        "manager": Permission.READ | Permission.WRITE,
        "support": Permission.EXECUTE
    }

    def _infer_permission(self):
        permissions = Permission.READ
        role = self.user_role

        if role in self.USER_ROLES:
            permissions = self.USER_ROLES.get(role)
        elif type(role) == int:
            try:
                Permission(role)
            except ValueError:
                pass
            else:
                permissions = role

        return Permission(permissions)
    
    def _validate_permission(self, permission):
        if permission not in self.permissions:
            raise PermissionError(f"User does not have {permission.name} permission")

    def read(self, file="script.py"):
        self._validate_permission(Permission.READ)
        
        with open(file) as f:
            return f.read
        
    def write(self, file="script.py", content=""):
        self._validate_permission(Permission.WRITE)

        with open(file, "w") as f:
            f.write(content)
            print(f"Wrote content_ {content}")

    def execute(self, file="script.py"):
        self._validate_permission(Permission.EXECUTE)

        exec(open(file).read())
        print(f"Executed the file {file}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name = '{self.name}', user_role = '{self.user_role}')"

class User(BaseUser):
    def __init__(self, name, user_role) -> None:
        #super().__init__()
        self.name = name
        self.user_role = user_role

        self.permissions = self._infer_permission()


        

if __name__ == "__main__":
    

    m = User(name = "Mmmmmanager", user_role="manager")
    m.write(file="xyz.py", content="print(datetime.now())")

    u = User(name = "Uuuusssser", user_role="user")
    ic(u.__dict__)
    s = u.read(file="xyz.py")
    ic(u.read(file="xyz.py"))
    ic(str(s))

    a = User(name = "Aaaadmin", user_role="admin")
    a.execute(file="xyz.py")
    ic(a.__dict__)


    u2 = User(name = "Uuuusssser2", user_role=3)
    ic(u2.__dict__)
    s = u2.read(file="xyz.py")
    ic(u2.read(file="xyz.py"))
    ic(str(s))

    p1 = Permission
    ic(p1.__dict__)
    ic(p1(1))
    ic(p1.READ)
    ic(p1(Permission.READ | Permission.WRITE | Permission.EXECUTE))
