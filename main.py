import csv

def add_contact(name, phone, email):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

def remove_contact(name):
    contacts = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        contacts = [row for row in reader if row[0] != name]
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def update_contact(name, new_phone, new_email):
    contacts = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                row[1] = new_phone
                row[2] = new_email
            contacts.append(row)
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def display_contacts():
    try:
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
    except FileNotFoundError:
        print("No contacts found. Please add contacts first.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            update_contact(name, new_phone, new_email)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
