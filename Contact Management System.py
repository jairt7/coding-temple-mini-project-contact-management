# Coding Temple Mini-Project: Contact Management System
import re

contacts = []

def welcome_message():
    # Prints the main menu
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def what_to_do():
    # Determines what user input from the welcome menu means
    do_what = input("\nWhat would you like to do? ").lower()
    if do_what == "1" or do_what == "add" or do_what == "add a new contact" or do_what == "add new" \
    or do_what == "1. add a new contact":
        return 1
    elif do_what == "2" or do_what == "edit" or do_what == "edit an existing contact" or do_what == "edit existing" \
    or do_what == "2. edit an existing contact":
        return 2
    elif do_what == "3" or do_what == "delete" or do_what == "delete a contact" or do_what == "delete contact" \
    or do_what == "3. delete a contact":
        return 3
    elif do_what == "4" or do_what == "search" or do_what == "search for a contact" or do_what == "search contacts" \
    or do_what == "search for contact" or do_what == "search for contacts" or do_what == "4. search for a contact":
        return 4
    elif do_what == "5" or do_what == "display" or do_what == "display all contacts" or do_what == "display contacts" \
    or do_what == "5. display all contacts":
        return 5
    elif do_what == "6" or do_what == "export" or do_what == "export comtacts to a text file" or do_what == "export contacts" \
    or do_what == "export contacts to text" or do_what == "export contacts to a file" or do_what == "export contacts to file" \
    or do_what == "6. export contacts to a text file":
        return 6
    elif do_what == "7" or do_what == "import" or do_what == "import comtacts from a text file" or do_what == "import contacts" \
    or do_what == "import contacts from text" or do_what == "import contacts from a file" or do_what == "import contacts from file" \
    or do_what == "7. import contacts from a text file":
        return 7
    elif do_what == "8" or do_what == "quit" or do_what == "8. quit":
        return 8
    else:
        return 0
    
def add_contact():
    global contacts
    name = input("Enter the name of the person you'd like to add: ").title()
    phone = input("Enter their phone number: ")
    phone = re.sub("[-() \.]", "", phone)
    address = "None"
    add_address = input("Would you like to add an address? Y or n ").lower()
    if add_address == "y" or add_address == "yes":
        address = input("What's their address? ")
    birthday = "None"
    add_birthday = input("Would you like to add a birthday? Y or n ").lower()
    if add_birthday == "y" or add_birthday == "yes":
        birthday = input("What's their birthday? ")
    notes = "None"
    add_notes = input("Would you like to add any other notes? Y or n ").lower()
    if add_notes == "y" or add_notes == "yes":
        notes = input("What notes would you like to add? ")
    new_contact = {"name": name, "phone": phone, "address": address, "birthday": birthday, "notes": notes}
    try:
        contacts.append(new_contact)
    except Exception as e:
        print(f"An error occurred: {e}")


def edit_contact():
    if contacts == []:
        print("You don't currently have any contacts.")
        return
    which_one = input("Which contact would you like to edit? Please enter their name or phone #: ").title()
    which_one_num = re.sub("[-() \.]", "", which_one)
    if which_one_num.isdigit():
        which_one = which_one_num
    
    for contact in contacts:
        if contact["phone"] == which_one or which_one in contact["name"]:
            print("Is this the contact you'd like to edit?")
            print(contact)
            edit_it = input("Y or n ").lower()
            if edit_it == "y" or edit_it == "yes":
                which_part = input("Which part of the contact would you like to edit? Name, phone number, address,\
 birthday, or notes? ").lower()
                if which_part == "name":
                    new_name = input("What would you like the new name to be? ").title()
                    contact["name"] = new_name
                elif which_part == "phone" or which_part == "phone number" or which_part == "number":
                    new_number = input("What would you like the new number to be? ")
                    new_number = re.sub("[-() \.]", "", new_number)
                    contact["phone"] = new_number
                elif which_part == "address":
                    new_address = input("What would you like the new address to be? ")
                    contact["address"] = new_address
                elif which_part == "birthday":
                    new_birthday = input("What would you like the birthday to be? ")
                    contact["birthday"] = new_birthday
                elif which_part == "note" or which_part == "notes":
                    new_notes = input("What would you like your notes to be? ")
                    contact["notes"] = new_notes
                else:
                    print("Couldn't identify input. Please try again.")
                    
        else:
            continue
    


def delete_contact():
    if contacts == []:
        print("You don't currently have any contacts.")
        return
    which_one = input("Which contact would you like to delete? Please enter their name or phone #: ").title()
    which_one_num = re.sub("[-() \.]", "", which_one)
    if which_one_num.isdigit():
        which_one = which_one_num
    
    for contact in contacts:
        if contact["phone"] == which_one or which_one in contact["name"]:
            print("Is this the contact you'd like to delete?")
            print(contact)
            delete_it = input("Y or n ").lower()
            if delete_it == "y" or delete_it == "yes":
                contacts.remove(contact)
                print("Contact deleted.")
            else:
                continue


def search_contacts():
    if contacts == []:
        print("You don't currently have any contacts.")
        return
    which_one = input("Please enter the name or phone # of the contact you'd like to find: ").title()
    which_one_num = re.sub("[-() \.]", "", which_one)
    if which_one_num.isdigit():
        which_one = which_one_num
    found = False
    for contact in contacts:
        if contact["phone"] == which_one or which_one in contact["name"]:
            print("Match found.")
            print(contact)
            found = True
        else:
            continue
    if not found:
        print("No matches found. Sorry.")


def display_contacts():
    print("\nHere's a list of your contacts.\n")
    contact_number = 1
    for contact in contacts:
        print("Contact #" + str(contact_number) + ": " + contact["name"] + ": \nPhone number: " + str(contact["phone"]) + "\n\
Address: " + contact["address"] + "\nBirthday: " + contact["birthday"] + "\nNotes: " + contact["notes"] + "\n")
        contact_number += 1

def export_contacts():
    with open("stored_contacts.txt", "a") as file:
        for contact in contacts:
            file.write(f"{contact["name"]}-:-{contact["phone"]}-:-{contact["address"]}-:-{contact["birthday"]}-:-\
{contact["notes"]}\n")
    print("Exported contacts as 'stored_contacts.txt'")

def import_contacts():
    with open("stored_contacts.txt", "r") as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\d]+)-:-([\w\s]+)-:-([\w\s/-]+)-:-([\w\s]+)", line)
            contacts.append({'name': data.group(1), 'phone': data.group(2), 'address': data.group(3), "birthday": data.group(4), \
"notes": data.group(5).strip()})
    print("Contacts imported.")

def main_program():
    global keep_going
    what = what_to_do()
    if what == 1:
        add_contact()
    elif what == 2:
        edit_contact()
    elif what == 3:
        delete_contact()
    elif what == 4:
        search_contacts()
    elif what == 5:
        display_contacts()
    elif what == 6:
        export_contacts()
    elif what == 7:
        import_contacts()
    elif what == 8:
        print("\nThanks for using my program. I hope it worked for you.")
        keep_going = False

keep_going = True
while keep_going:
    welcome_message()
    main_program()