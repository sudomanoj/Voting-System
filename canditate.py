from helper import load_from_file, save_to_file


class Candidate:
    sn=0
    filename="data/candidates.txt"
    def __init__(self):
        self.candidates=[]
        self.candidates.extend(load_from_file(self.filename))
    
    def update_id(self):
        data=self.candidates
        id_values = [item["id"] for item in data]
        self.sn = max(id_values) + 1 if id_values else 1

        
    def check_duplicate(self,can):
        if any(candidate["cname"] == can["cname"] and candidate["cparty"] == can["cparty"] and
                        candidate["cfrom"] == can["cfrom"] for candidate in self.candidates):
                    return 1
        return 0
            



    def add_candidate(self):
        try:
            can={"vote_count":0}            
            name=str(input("Enter your name: ")).strip()
            party=str(input("Enter your party name: ")).strip()
            cfrom=str(input("Enter from where you are taking candency: ")).strip()
            if name and party and cfrom:
                can.update({"cname":name,"cparty":party,"cfrom":cfrom})
                if self.check_duplicate(can):
                    print("User with same details already exists")
                else:
                    self.update_id()
                    can["id"]=self.sn
                    self.candidates.append(can)
                    self.sn+=1
                    print("Candidate added")
            else:
                print("You must fill all the required fields")

            

        except Exception as e:
            print("add_candidate",e)

    def update_candidate(self):
        try:
                id=int(input("Enter your candidate id: eg 12,14.."))
                candidate=next((i for i in self.candidates if i["id"]==id),None)
                if candidate:      
                    name=str(input("Enter your name: ")).strip()
                    party=str(input("Enter your party name: ")).strip()
                    cfrom=str(input("Enter from where you are taking candency: ")).strip()

                   
                    if not self.check_duplicate({"cname":name,"cparty":party,"cfrom":cfrom}):
                        if name:
                            candidate["cname"]=name
                        if party:
                            candidate["cparty"]=party
                        if cfrom:
                            candidate["cfrom"]=cfrom
                        print("Candidate upadted successfully " if any([name,party,cfrom]) else "No change in candidate")
                    else:
                        print("Candidate with same details already exists")
                   
                else:
                    print("Invalid candidate Id")

            

        except Exception as e:
            print("update_candidate",e)



    def delete_candidate(self):
        try:
            id=int(input("Enter your candidate id: eg 12,14.."))
            candidate=next((i for i in self.candidates if i["id"]==id),None)
            if candidate and not candidate["vote_count"]:      
                self.candidates.remove(candidate)
                print("Candidate removed successfully")
            else:
                print("Cannot delete the Candidate")
        

        except Exception as e:
            print("update_candidate",e)


    def view_candidate(self):
        try:
            if self.candidates:
                print("\nCandidate Information:")
                for candidate in self.candidates:
                    print(f"\nId: {candidate['id']}")
                    print(f"\nName: {candidate['cname']}")
                    print(f"from: {candidate['cfrom']}")
                    print(f"Party: {candidate['cparty']} ")
                    print("=" * 30)  
            else:
                print("No candidates to show")

            

        except Exception as e:
            print("view_candidate",e)


