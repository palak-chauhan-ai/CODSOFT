contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return

    print("\n----- CONTACT LIST -----")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['Name']} - {contact['Phone']}")

def search_contact():
    search = input("Enter Name or Phone Number to search: ")

    found = False

    for contact in contacts:
        if search.lower() == contact["Name"].lower() or search == contact["Phone"]:
            print("\nContact Found")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            found = True

    if not found:
        print("Contact not found!")

def update_contact():
    name = input("Enter contact name to update: ")

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contact["Phone"] = input("Enter New Phone Number: ")
            contact["Email"] = input("Enter New Email: ")
            contact["Address"] = input("Enter New Address: ")

            print("Contact updated successfully!")
            return

    print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")