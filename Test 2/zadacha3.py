import json

class ContactBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = {}

    def load_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            print("File not found. Creating a new empty contact file.")
        except json.JSONDecodeError:
            print("File is corrupted or empty. Please use a valid JSON file.")

    def save_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_record(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        self.contacts[name] = phone
        print("Contact added successfully.")

    def print_contact_book(self):
        if self.contacts:
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("The contact book is empty.")

contact_book = ContactBook('contacts.json')
contact_book.load_file()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Save Contacts")
    print("3. Load Contacts")
    print("4. Display Contacts")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        contact_book.add_record()
    elif choice == '2':
        contact_book.save_file()
    elif choice == '3':
        contact_book.load_file()
    elif choice == '4':
        contact_book.print_contact_book()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose a valid number.")
