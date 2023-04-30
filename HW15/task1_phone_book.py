import re

phone_book = {}

# Adding a contact
def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")

    # Checking the phone number format using regular expressions
    while not re.match(r'^(\+?3?8?)?0\d{9}$', phone_number):
        print("Incorrect phone number format. Please enter the number in the format +380XXXXXXXXX, 380XXXXXXXXX or 0XXXXXXXXX.")
        phone_number = input("Enter a phone number: ")

    phone_book[name] = phone_number
    print("Contact added.")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Display a list of all contacts
def list_contacts():
    if not phone_book:
        print("The phone book is empty.")
    else:
        print("Contacts:")
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")

# Searching for a contact by name and displaying its detailed information
def show_contact():
    name = input("Enter the name of the contact you want to view: ")
    if name in phone_book:
        print(f"Name: {name}")
        print(f"Phone number: {phone_book[name]}")
    else:
        print("Contact not found.")

# Number of entries
def show_stats():
    print(f"In the phone book {len(phone_book)} entry(s).")

# Commands
while True:
    print("To add a contact, type 'add'.")
    print("To delete a contact, type 'delete'.")
    print("To display a list of contacts, type 'list'.")
    print("To view a contact, type 'view'.")
    print("To exit the program, type 'exit'.")
    print("To view the number of contacts in the book, enter 'number'.")

    command = input("Enter the command: ").lower()

    if command == "add":
        add_contact()
    elif command == "amount":
        show_stats()
    elif command == "delete":
        delete_contact()
    elif command == "list":
        list_contacts()
    elif command == "view":
        show_contact()
    elif command == "exit":
        break
    else:
        print("Wrong command. Enter a command from the list.")