class Election:
    def __init__(self):
        print("Election Started")

    def vote(self,cands):
        ins=["id","name","from","party"]
        print("\nCandidate Information:")
        print("\n| {:^4} | {:^20} | {:^20} | {:^20} | \n".format(
                ins[0],
                ins[1],
                ins[2],
                ins[3]
            ))
        for c in cands:
            print("| {:^4} | {:^20} | {:^20} | {:^20} | \n".format(
                    c["id"],
                    c["cname"],
                    c["cfrom"],
                    c["party"]
                ))
        vote_to=input("Enter Candidate id").strip()
        candidate=next((i for i in cands if i["id"]==vote_to),None)
        if candidate:
            if not candidate["vote"]:
                candidate["vote"]=1
            else:
                candidate["vote"]+=1
            print(f"Voted to candidate with id {vote_to}")
        else:
            print("Invalid candidate id")

    



