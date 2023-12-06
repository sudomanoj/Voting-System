from helper import load_from_file, save_to_file


class Candidate:
    sn=0
    filename="candidates.json"
    def __init__(self):
        self.candidates=[]
        self.candidates.extend(load_from_file(self.filename))
    
    @classmethod
    def get_id(cls):
        data=load_from_file(cls.filename)
        max=1
        for d in data:
            if d["id"]>max:
                max=data["id"]
        return max
            



    def add_candidate(self,user):
        try:
            if user["role"]=="admin":
                can={}            
                name=str(input("Enter your name: ")).strip()
                party=str(input("Enter your party name: ")).strip()
                cfrom=str(input("Enter from where you are taking candency: ")).strip()
                if name and party and cfrom:
                    can.update({"cname":name,"cparty":party,"cfrom":cfrom})
                    if any(candidate["cname"] == can["cname"] and candidate["cparty"] == can["cparty"] and
                           candidate["cfrom"] == can["cfrom"] for candidate in self.candidates):
                        print("Candidate already exists")
                    else:
                        can["id"]=Candidate.get_id()+1
                        self.candidates.append(can)
                        self.sn+=1
                        print("Candidate added")
                else:
                    print("You must fill all the required fields")
            else:
                print("You must be admin for this operation")
            

        except Exception as e:
            print("add_candidate",e)

    def update_candidate(self,user):
        try:
            if user["role"]=="admin":
                id=int(input("Enter your candidate id: eg 12,14.."))
                candidate=next((i for i in self.candidates if i["id"]==id),None)
                if candidate:      
                    name=str(input("Enter your name: ")).strip()
                    party=str(input("Enter your party name: ")).strip()
                    cfrom=str(input("Enter from where you are taking candency: ")).strip()
                    if name:
                        candidate["cname"]=name
                    if party:
                        candidate["cparty"]=party
                    if cfrom:
                        candidate["cfrom"]=party
                    if name or party or cfrom:
                        print("Candidate upadted successfully")
                    else:
                        print("No change in candidate")

                    
                else:
                    print("Invalid candidate Id")

            else:
                print("You must be admin for this operation")
            

        except Exception as e:
            print("update_candidate",e)



    def delete_candidate(self,user):
        try:
            if user["role"]=="admin":
                id=int(input("Enter your candidate id: eg 12,14.."))
                candidate=next((i for i in self.candidates if i["id"]==id),None)
                if candidate:      
                    self.candidates.remove(candidate)
                    print("Candidate removed successfully")
                else:
                    print("Invalid candidate Id")

            else:
                print("You must be admin for this operation")
            

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


c=Candidate()
user={"role":"admin"}
while True:
    command=str(input("Enter your choice"))
    match command:

        case "a":
            c.add_candidate(user)

        case "u":
            c.update_candidate(user)

        case "d":
            c.delete_candidate(user)

        case "v":
            c.view_candidate()
        case "e":
            print("Exitting")
            save_to_file(c.filename,c.candidates)
            break
        case _:
            print("Invalid command")