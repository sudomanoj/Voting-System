import json
from datetime import datetime

class Constituency:
    filename='data/constituency.txt'
    def __init__(self):
        print('###### Election #####')

    def election(self):
        try:
            area = input('Enter Constituency Area: ')
            date_of_election = input('Enter date (YYYY-MM-DD): ')
            area_exists = self.check_area(area)

            try:
                doe = datetime.strptime(date_of_election, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")
                return 
            if not area_exists: 
                if not area.strip(): 
                    print('Please provide a valid area!')
                else:
                    constituency_dict = {'constituency': area, 'date_of_election': str(doe)}
                    with open(self.filename, 'a') as file:
                        file.write(json.dumps(constituency_dict) + '\n')
                    print('Election details saved successfully.')
            else:
                print(f'Given area {area} already exists!')
        except Exception as e:
            print(e)




            
    def check_area(self, area):
        try:
            with open(self.filename, 'r') as file:
                data_list = [json.loads(line) for line in file]
                for data in data_list:
                    if data['constituency'].lower() == area.lower():
                        return True
            return False
        except Exception as e:
            print(e)
            return False
