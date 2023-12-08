import json
from datetime import datetime

from helper import load_from_file

   
        

class Voter:
    id = 0
    filename="data/voterlist.txt"

    def get_next_id(self):
        data=self.voter_list
        id_values = [item["id"] for item in data]
        self.id = max(id_values) + 1 if id_values else 1

    def __init__(self):
        self.voter_list = []
        self.voter_list.extend(load_from_file(self.filename))
    
    def registration(self):
        while True:
            name = input('Enter Name: ')
            dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")
                continue 
            
            address = input('Enter address: ')
            password = input('Enter password: ')
            voter_exists = self.check_voter(name, dob, address)
            
            if voter_exists:
                print('Voter already exists in the system! Enter new voter!')
            else:
                break

        age = self.calculate_age(dob)
        
        if age >= 18:
            self.get_next_id()
    
            voter_dict = {'id': self.id, "role":"voter","voted":0,'name': name, 'dob': dob_str, 'address': address, 'password': password}
            self.voter_list.append(voter_dict)
            print('Voter added')
        else:
            print('You are a minor!!')

    def check_voter(self, name, dob, address):
        if self.voter_list:
            if any(voter['name'] ==name and voter['dob'] == dob and voter['address'] == address for voter in self.voter_list):
                return True
        else:
            return False

    
    def calculate_age(self, dob):
        try:
            current_date = datetime.now().date()
            age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
            return age
        except Exception as e:
            print(e)

    def update_voter(self):
        voter_id = int(input('Enter ID: '))
        voter_exists = self.exists_voter(voter_id)
        if voter_exists:
            data_list = self.voter_list
            for i, data in enumerate(data_list):
                if data['id'] == voter_id:
                    name = input('Enter new Name: ')
                    dob_str = input('Enter new dob (yyy-mm-dd): ')
                    address = input('Enter new address: ')
                    password = input('Enter new password: ')
                    if len(name) > 0:
                        data_list[i]['name'] = name
                    data_list[i]['dob'] = dob_str
                    if len(address) > 0:
                        data_list[i]['address'] = address
                    if len(password) > 0:
                        data_list[i]['password'] = password

            print('Voter information updated successfully.')
        else:
            print('Voter not found.')        

        
        
    def exists_voter(self, id):
        if self.voter_list:
                if id in [voter["id"] for voter in self.voter_list]:
                    return True
                else:
                    return False
        return False
    
    def delete_voter(self):
        voter_id = int(input('Enter VoterID: '))
        voter_exists = self.exists_voter(voter_id)
        if voter_exists:
            voter = [data for data in self.voter_list if data['id'] == voter_id]
            self.voter_list.remove(voter[0])
            print(f'Voter with ID {voter_id} deleted successfully!')
        else:
            print('Voter not found!')
            
    def search_voter(self):
        voter_id = int(input('Enter VoterID: '))
        voter_exists = self.exists_voter(voter_id)
        if voter_exists:
            for data in self.voter_list:
                if data['id'] == voter_id:
                    print(f"""
ID : {data['id']}
Name : {data['name']}
DOB : {data['dob']}
Address : {data['address']}
Password : {data['password']}
                        """)

        else:
            print(f'Voter with ID {voter_id} not found!!')
        
