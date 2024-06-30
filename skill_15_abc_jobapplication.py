from dataclasses import dataclass
from collections.abc import Sequence
from icecream import ic

@dataclass(frozen=True)
class JobApplicant:
    applicant_id: str
    years_experience: int
    is_recommended: bool
    first_interview_score: float
    second_interview_score: float

class JobApplicantPool(Sequence):
    def __init__(self, *args):
        self._applicants = list(args)

    def add(self, applicant):
        self._applicants.append(applicant)
    
    def __getitem__(self, item):
        if type(item) == slice:
            type(self)(*self._applications[item])
        elif type(item) == int:
            return self._applicants[item]
        
        return NotImplemented
    
    def __len__(self):
        
        pass

    @staticmethod
    def score(applicant: JobApplicant):
        pass

    



if __name__ == "__main__":
    jap = JobApplicantPool()
    ic(jap)