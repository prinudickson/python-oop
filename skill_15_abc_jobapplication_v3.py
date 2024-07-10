from dataclasses import dataclass
from collections.abc import Sequence
from icecream import ic
from functools import total_ordering
from bisect import insort

from random import randint, uniform

@total_ordering
@dataclass(frozen=True)
class JobApplicant:
    applicant_id: str
    years_experience: int
    is_recommended: bool
    first_interview_score: float
    second_interview_score: float

    def __post_init__(self):
        score = round(
            self.years_experience * 0.5 +
            self.is_recommended +
            self.first_interview_score * 0.5 +
            self.second_interview_score
            , 2)
        
        super().__setattr__('score', score)
    
    def __le__(self, other):
        return self.score > other.score
    
    def __eq__(self, other):
        return self.score == other.score

class JobApplicantPool(Sequence):
    def __init__(self, *args):
        self._applicants = sorted(list(args)) 

    def add(self, applicant):
        insort(self._applicants, applicant)
    
    def __getitem__(self, item):
        if type(item) == slice:
            return type(self)(*self._applicants[item])
        elif type(item) == int:
            return self._applicants[item]
        
        return NotImplemented
    
    def __len__(self) -> int:
        return len(self._applicants)
    
    def __repr__(self) -> str:
        header = f"Applicant Pool\n(Score | ID)\n{'-'*20}\n"
        return header + "\n".join([
            f"{applicant.score} - {applicant.applicant_id}" for applicant in self._applicants
        ])

    

    
def generate_randon_applicants(n=18):
    return [
        JobApplicant(
            applicant_id=str(randint(10000,90000)),
            years_experience=randint(0,10),
            is_recommended=bool(randint(0,1)),
            first_interview_score=round(uniform(1.0,10.0),2),
            second_interview_score=round(uniform(1.0,10.0),2)
        ) for _ in range(n)
    ]


if __name__ == "__main__":
    jap = JobApplicantPool(*generate_randon_applicants(n=2))
    ic(jap)
    ic(len(jap))
    # ic(jap[2:4])

    # ic(*generate_randon_applicants(n=1))
    jap.add(*generate_randon_applicants(n=1))
    ic(jap)