from icecream import ic

class DNABase:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, nucleotide) -> None:
        self.base = nucleotide

    @staticmethod
    def _validate_standardise(base):
        allowed = [('a', 'adenine'), ('c', 'cytosine'), ('g', 'guanine'), ('t', 'thymine')]

        for b in allowed:
            if base.lower().strip() in b:
                return b[1]
            
        return False
        
    def get_base(self):
        return self._base
    
    def set_base(self, base):
        valid_base = self._validate_standardise(base)
        if valid_base: 
            self._base = valid_base
        else:
            ValueError(f"{base} - Invalid Base!")
    
    base = property(fget=get_base, fset=set_base)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nucleotide='{self.base}')"

if __name__ == "__main__":
    d1 = DNABase("adenine")
    ic(d1.__dict__)

    d2 = DNABase('T')
    ic(d2)

    d = DNABase("hgjh")


    