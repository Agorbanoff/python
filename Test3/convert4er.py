import csv
import json

class Convert4er:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_csv(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def write_csv(self, output_file):
        if not self.data:
            return
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)

    def read_json(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

    def write_json(self, output_file):
        with open(output_file, mode='w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def convert(self, from_format="csv", to_format="json", output_file="output.json"):
        if from_format == "csv":
            self.read_csv()
        elif from_format == "json":
            self.read_json()

        if to_format == "csv":
            self.write_csv(output_file)
        elif to_format == "json":
            self.write_json(output_file)
