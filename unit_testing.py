import unittest
import json
import subprocess

class TestCSVParser(unittest.TestCase):
    def test_csv_to_json_conversion(self):
        subprocess.run(['python', 'csv_to_json.py', 'test_data.csv', 'output.json'])
        
        with open('test_data.csv', 'r', newline='', encoding='utf-8') as csv_file:
            csv_data = list(csv.DictReader(csv_file))
        
        with open('output.json', 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        self.assertEqual(json_data, csv_data)

    def test_csv_parser_error_handling(self):
        result = subprocess.run(['python', 'csv_to_json.py', 'malformed_data.csv', 'output.json'], stderr=subprocess.PIPE)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Error while parsing CSV', result.stderr.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
