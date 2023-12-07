import json
def save_to_file(filename,data):
    try:
        with open(filename, 'w') as file:
            
            json.dump(data, file, indent=2)
        print(f"\nData saved to {filename} as JSON.")
    except Exception as e:
        print(f"Error saving  data: {e}")

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"\nData loaded from {filename}.")
        if data:
            return data
        else:
            return []
    except Exception as e:
        print(f"Error loading  data: {e}")
        return []