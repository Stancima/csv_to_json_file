import csv
import json
import sys

# creating the csv_to_json function and reading the csv file.

def csv_to_json(csv_path, json_path):
    try:
        with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            
# writing into the json file.

            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(rows, json_file, ensure_ascii=False, indent=2)
                
# error handling for csv parsing issues.

    except csv.Error as e:
        print(f'Error while parsing CSV: {e}')
        sys.exit(1)

if __name__ == '__main__':
    
 # Code in this block will only be executed when this script is run directly

    if len(sys.argv) != 3:
        print('Usage: python csv_to_json.py <csv_path> <json_path>')
        sys.exit(1)
        
# setting the arguments.

    csv_path = sys.argv[1]
    json_path = sys.argv[2]

    csv_to_json(csv_path, json_path)
