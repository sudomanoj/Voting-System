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
            0 --> result\n
            1 --> schedule\n
            2 --> register candidate\n
            3 --> update candidate\n
            4 --> delete candidate\n
            5 --> register voter\n
            6 --> update voter\n
            7 --> search voter\n
            8 --> delete voter\n
            9 --> vote\n
            10 --> view candidates\n
            11 --> view voters\n
            a --> Promote to admin\n
            l --> login with new user\n
            h --> help\n
            e --> exit\n

            ''')
    
    def login_user(self):
        try:
            id=int(input("Enter your id: "))
            password=str(input("Enter your password: ")).strip()
            user=next((v for v in self.voter.voter_list if v["id"]==id),None)
            if user and user["password"]==password:
                self.user=user
                print("You are authenticated, Go on\n")
            else:
                print("You are not authenticated, Invalid Credentials")
        except Exception as e:
            print(e)
        




    
    def run_election(self):
        try:
            self.print_help()
            while True:
                command=str(input("Enter your choice:")).strip()
                match command:

                    case "1":
                        if self.user and self.user["role"]=="admin":
                            data=load_from_file(self.constituency.filename)
                            if not data:
                                self.constituency.election() 
                            else:
                                print("You already have scheduled an election")
                        else:
                            print("Please login to proceed, Also you must be admin")
                            self.login_user()                   

                    case "2":
                        if self.user:
                            if self.user["role"]=="admin":
                                self.candidate.add_candidate()
                            else:
                                print("you must be admin to proceed")
                        else:
                            print("Please login to proceed, Also you must be admin")

                            self.login_user()    
                    

                    case "3":
                        if self.user:
                            if self.user["role"]=="admin":
                                self.candidate.update_candidate()
                            else:
                                print("you must be admin to proceed")

                        else:
                            print("Please login to proceed")
                            self.login_user()   

                    case "4":
                        if self.user:
                            if self.user["role"]=="admin":
                                self.candidate.delete_candidate()
                            else:
                                print("you must be admin to proceed")
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
                        if self.user:
                            if self.user["role"]=="admin":
                                self.voter.delete_voter()
                            else:
                                print("you must be admin to proceed")
                                
                        else:
                            print("Please login to proceed, Also you must be admin")
                            self.login_user()  

                    case "a":
                        try:
                            i=int(input("Enter your id: "))
                            user=next((u for u in self.voter.voter_list if u["id"]==i),None)
                            if user:
                                user["role"]="admin"
                                print("User Promoted to admin")
                            else:
                                print(f"No user with id {i} exists")
                        except Exception as e:
                            print(e)


                    case "9":
                        try:
                            if self.user:
                                if self.user["role"]=="voter":
                                    data=load_from_file(self.constituency.filename)
                                    if not data:
                                        print("No election scheduled")
                                        continue
                                    
                                    if datetime.strptime(data["date_of_election"], "%Y-%m-%d").date()==date.today():
                                        if not self.user["voted"]:
                                            self.election.vote(self.candidate.candidates)
                                            self.user["voted"]+=1
                                        else:
                                            print("You have already voted")
                                    else:
                                        print("Election is not today,You cannot vote now")
                                else:
                                    print("you must be voter to proceed")
                                

                            else:
                                print("Please login to proceed, Only voter can vote")
                                self.login_user()  
                        except Exception as e:
                            print(e)
                    
                    case "0":
                        if self.user:
                            if self.user["role"]=="admin":
                                self.election.result(self.candidate.candidates)
                            else:
                                print("you must be admin to proceed")

                        else:
                            print("Please login to proceed")
                            self.login_user()  

                    case "10":
                        self.candidate.view_candidate()

                    case "11":
                        print(self.voter.voter_list)
                        for v in self.voter.voter_list:
                            print(
                                f'''
***************                                
id={v["id"]}
Name={v["name"]}
Address={v["name"]}
Voted={v["voted"]}
Password={v["password"]}
****************                                '''
                            )

                    

                    case "l":
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
                        
        except KeyboardInterrupt as e:
            print("\nExitting...")
            print(f"Saving candidates data to {self.candidate.filename}")
            save_to_file(self.candidate.filename,self.candidate.candidates)
            print(f"Saving Voters data to {self.voter.filename}")
            save_to_file(self.voter.filename,self.voter.voter_list)
            print(e)
        except Exception as e:
            print(e)


ElectionManger().run_election()