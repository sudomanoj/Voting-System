from datetime import date, datetime
from canditate import Candidate
from constituency import Constituency
from election import Election
from helper import load_from_file, save_to_file
from voter import Voter


class ElectionManger:
    def __init__(self):
        self.candidate=Candidate()
        self.voter=Voter()
        self.constituency=Constituency()
        self.election=Election()
        self.user={}


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
    
    def login_user(self):
        id=input("Enter your name: ").strip()
        password=str(input("Enter your password")).strip()
        user=next((v for v in self.voter.voter_list if v["id"]==id),None)
        if user and user["password"]==password:
            self.user=user
            print("You are authenticated, Go on\n")
        else:
            print("You are not authenticated, Invalid Credentials")
        




    
    def run_election(self):
        self.print_help()
        while True:
            command=str(input("Enter your choice:")).strip()
            match command:

                case "1":
                    if self.user and self.user["role"]=="admin":
                        self.constituency.election() 
                    else:
                        print("Please login to proceed, Also you must be admin")
                        self.login_user()                   

                case "2":
                    if self.user and self.user["role"]=="admin":
                        self.candidate.add_candidate()
                    else:
                        print("Please login to proceed, Also you must be admin")

                        self.login_user()    
                    
                case "3":
                    if self.user and self.user["role"]=="admin":
                        self.candidate.update_candidate()
                    else:
                        print("Please login to proceed, Also you must be admin")

                        self.login_user()   

                case "4":
                    if self.user and self.user["role"]=="admin":
                        self.candidate.delete_candidate()
                    else:
                        print("Please login to proceed, Also you must be admin")

                        self.login_user()   

                case "5":
                    self.voter.registration()

                case "6":
                    self.voter.update_voter()

                case "7":
                    self.voter.search_voter()

                case "8":
                    if self.user  and self.user["role"]=="admin":
                        self.voter.delete_voter()
                    else:
                        print("Please login to proceed, Also you must be admin")
                        self.login_user()  


                case "9":
                    if self.user and self.user["role"]=="voter":
                        data=load_from_file("constituency.txt")
                        if data["date_of_election"]==date.today():
                            if not self.user["vote"]:
                                self.election.vote(self.candidate.candidates)
                            else:
                                print("You have already voted")
                        else:
                            print("Election is not today,You cannot vote now")

                    else:
                        print("Please login to proceed")
                        self.login_user()  
                
                case "0":
                    if self.user and self.user["role"]=="admin":
                        self.election.result(self.candidate.candidates)

                    else:
                        print("Please login to proceed")
                        self.login_user()  

                case "h":
                    self.print_help()
                    
                case "e":
                    print("Exitting...")
                    print(f"Saving candidates data to {self.candidate.filename}")
                    save_to_file(self.candidate.filename,self.candidate.candidates)
                    print(f"Saving Voters data to {self.voter.filename}")
                    save_to_file(self.voter.filename,self.voter.voter_list)
                    break

                case _:
                    print("Invalid command")
                    self.print_help()


ElectionManger().run_election()