import json
from datetime import datetime

class Idcounter:
    id = 0
    
    @classmethod
    def get_next_id(cls):
        with open('voterid.log', 'r') as file:
            for f in file:
                cls.id = int(f)
        cls.id += 1
        with open('voterid.log', 'w') as file:
            file.write(str(cls.id))
        return cls.id

class Voter:
    voter_list = []
    
    
    def registration(self):
        while True:
            voter_id = Idcounter.get_next_id()
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
            voter_dict = {'id': voter_id, 'name': name, 'dob': dob_str, 'address': address, 'password': password}
            self.voter_list.append(voter_dict)
            with open('voterlist.txt', 'a') as file:
                file.write(json.dumps(voter_dict) + '\n')
        else:
            print('You are a minor!!')

    def check_voter(self, name, dob, address):
        with open('voterlist.txt', 'r') as file:
            data_list = [json.loads(line) for line in file]
            for data in data_list:
                if (
                    data['name'].lower() == name.lower()
                    and str(data['dob']) == str(dob)  
                    and data['address'].lower() == address.lower()
                ):
                    return True
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
            with open('voterlist.txt', 'r') as file:
                data_list = [json.loads(line) for line in file]
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
                    
            with open('voterlist.txt', 'w') as file:
                for data in data_list:
                    file.write(json.dumps(data) + '\n')

            print('Voter information updated successfully.')
        else:
            print('Voter not found.')        

        
        
    def exists_voter(self, id):
        with open('voterlist.txt', 'r') as file:
            data_list = [json.loads(line) for line in file]
        for data in data_list:
            if data['id'] == id:
                return True
        return False
    
    def delete_voter(self):
        voter_id = int(input('Enter VoterID: '))
        voter_exists = self.exists_voter(voter_id)
        if voter_exists:
            with open('voterlist.txt', 'r') as file:
                data_list = [json.loads(line) for line in file]

            data_list = [data for data in data_list if data['id'] != voter_id]

            with open('voterlist.txt', 'w') as file:
                for data in data_list:
                    file.write(json.dumps(data) + '\n')

            print(f'Voter with ID {voter_id} deleted successfully!')
        else:
            print('Voter not found!')
            
    def search_voter(self):
        voter_id = int(input('Enter VoterID: '))
        voter_exists = self.exists_voter(voter_id)
        if voter_exists:
            with open('voterlist.txt', 'r') as file:
                data_list = [json.loads(line) for line in file]
            for data in data_list:
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
        
# Example usage
v = Voter()
v.search_voter()
