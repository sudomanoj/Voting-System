from canditate import Candidate
from constituency import Constituency
from voter import Voter


class ElectionManger:
    def __init__(self):
        self.candidate=Candidate()
        self.voter=Voter()
        self.constituency=Constituency()


    def print_help(self):
        print('''
            1 --> schedule
            2 --> register candidate
            3 --> update candidate
            4 --> delete candidate
            5 --> register voter
            6 --> update voter
            7 --> search voter
            8 --> delete voter
            9 --> vote
            0 --> result
            h --> help
            e --> exit

            ''')
    
    def run_election(self):
        self.print_help()
        while True:
            command=str(input("Enter your choice:")).strip()
            match command:

                case "1":
                    self.constituency.election()                    

                case "2":
                    self.candidate.add_candidate()
                    
                case "3":
                    self.candidate.update_candidate()

                case "4":
                    self.candidate.delete_candidate()

                case "5":
                    self.voter.registration()

                case "6":
                    self.voter.update_voter()

                case "7":
                    self.voter.search_voter()

                case "8":
                    self.voter.delete_voter()

                case "h":
                    self.print_help()
                    
                case "e":
                    print("Exitting")
                    break

                case _:
                    print("Invalid command")
                    self.print_help()


ElectionManger().run_election()