from helper import save_to_file


class Election:
    filename="data/Election_result.txt"
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
        try:
            if cands:
                for c in cands:
                    print("| {:^4} | {:^20} | {:^20} | {:^20} | \n".format(
                            c["id"],
                            c["cname"],
                            c["cfrom"],
                            c["cparty"]
                        ))
                vote_to=int(input("Enter Candidate id"))
                candidate=next((i for i in cands if i["id"]==vote_to),None)
                if candidate:                    
                    candidate["vote_count"]+=1
                    print(f"Voted to candidate with id {vote_to}")
                else:
                    print("Invalid candidate id")
            else:
                print("No candidates to show")
        except Exception as e:
                print(e)

    def result(self,cands):
        try:
            if cands:
                sorted_cands = sorted(cands, key=lambda c: c['vote_count'],reverse=True) 
                winner=sorted_cands[0]
                winner_name=winner["cname"]
                winner_from=winner["cfrom"]
                winner_party=winner["cparty"]
                print(f"{winner_name} from party {winner_party} who has taken candidancy from {winner_from} wins the election")
                ins=["id","name","from","party"]
                print("\nCandidate Information:")
                print("\n| {:^4} | {:^20} | {:^20} | {:^20} | \n".format(
                        ins[0],
                        ins[1],
                        ins[2],
                        ins[3]
                    ))
                for c in sorted_cands:
                    print("| {:^4} | {:^20} | {:^20} | {:^20} | \n".format(
                            c["id"],
                            c["cname"],
                            c["cfrom"],
                            c["cparty"]
                        ))
                save_to_file(self.filename,sorted_cands)

        except Exception as e:
            print(e)


