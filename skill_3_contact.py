from icecream import ic

class Contact:
    def __init__(self, firstname, lastname, phone=None, email=None, display_mode = "masked"):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
        

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Contact):
            return False
        
        if ((self.phone is not None and self.phone == __value.phone) and \
                (self.email is not None and self.email == __value.email)):
            return True
        
        if self.firstname == __value.firstname and self.lastname == __value.lastname:
            return True
        
        return False
    
    def __hash__(self) -> int:
        return hash((self.firstname, self.lastname, self.phone, self.email))
    
    def __repr__(self) -> str:
        if self.display_mode == "masked":
            return f"Contact(firstname='{self._obfuscate(self.firstname)}',lastname='{self._obfuscate(self.lastname)}')"
        else:
            return f"Contact(firstname='{self.firstname}',lastname='{self.lastname}', phone='{self.phone}', email='{self.email}', display_mode='{self.display_mode}')"
        
    def __str__(self) -> str:
        return f"{self.lastname[0]} {self.firstname[0]}"
    
    def __format__(self, format_spec):
        if format_spec != "masked":
            return f"Contact(firstname='{self.firstname}', lastname='{self.lastname}', phone='{self.phone}', email='{self.email}')"
        return repr(self)

    @staticmethod
    def _obfuscate(text):
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)


if __name__ == "__main__":

    c1 = Contact("first", "last")
    ic(c1)

    c2 = Contact("first", "last")
    ic(c2)

    ic(c1==c2)

    ic(f"{c1:masked}")

    ic(str(c1))

    ic(format(c1, "MASKED"))
    ic(format(c1, "masked"))
    
    ic(format(c1, "nla"))

    ic(hash(c1))
    ic(hash(c2))