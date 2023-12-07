from canditate import Candidate
from voter import Voter


class ElectionManger:
    def __init__(self):
        self.candidate=Candidate()
        self.voter=Voter()
        self.constituency=