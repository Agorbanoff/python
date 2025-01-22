import json

class ContactBook:
    def __init__(self, filepath):
        self.filepath = filepath
        self.contacts = self.load_file()

    def load_file(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_file(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_record(self, name, phone):
        if name in self.contacts:
            return "This name already exists in the contact book."
        self.contacts[name] = phone
        self.save_file()
        return "Contact added successfully."

    def print_contact_book(self):
        if not self.contacts:
            print("The contact book is empty.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

file_path = "contacts.json"
contact_book = ContactBook(file_path)
response = contact_book.add_record("Mincho", "125313")
print(response)
contact_book.print_contact_book()
