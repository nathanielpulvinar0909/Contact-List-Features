option = ""  # This is assign values to option

# Created a list that contains 50 entries for name entry, first name entry, last name entry, address entry, phone number entry
name_entry = ["Patricia Riley", "Nicholas Quinn", "Johnathan Crawford", "Michael Miller", "Marvin Barnes", "Roy Short",
              "Juan Cochran", "Carol Miller", "Brittany Rhodes", "Daniel Lin", "Robert Pearson", "Bonnie Smith",
              "Lorraine Gutierrez", "Katrina Green", "Desiree Garcia", "Suzanne Garcia", "Diana Bryant",
              "Vanessa Sanford", "Thomas Hughes", "Raymond Hamilton", "Stephen Jenkins", "Amanda Powell", "Thomas Carr",
              "Angie Cook", "Christina Tyler", "Laura Williams", "Jorge Kelly", "Nicholas Newton", "Brian Ross",
              "Rose Beasley", "Walter Anderson", "Cheryl Bell", "Douglas Beck", "Megan Price", "Robert Sanchez",
              "Jennifer Hartman", "Jennifer Brown", "Kenneth Ruiz", "William Maynard", "Andrew Smith", "Brett Jones",
              "Bradley Williams", "Zachary Hudson", "Marie Roberts", "Luis Ramirez", "Colin Arnold", "Debra Walker",
              "Rhonda Stewart", "Bobby Schultz", "Timothy Lopez"]  # Pre-made list for full name
first_name_entry = ["Patricia", "Nicholas", "Jonathan", "Michael", "Marvin", "Roy", "Juan", "Carol", "Brittany",
                    "Daniel", "Robert", "Bonnie", "Lorraine", "Katrina", "Desiree", "Suzanne", "Diana", "Vanessa",
                    "Thomas", "Raymond", "Stephen", "Amanda", "Thomas", "Angie", "Christina", "Laura", "Jorge",
                    "Nicholas", "Brian", "Rose", "Walter", "Cheryl", "Douglas", "Megan", "Robert", "Jennifer",
                    "Jennifer", "Kenneth", "William", "Andrew", "Brett", "Bradley", "Zachary", "Marie", "Luis", "Colin",
                    "Debra", "Rhonda", "Bobby", "Timothy"]  # Pre-made list for first name
last_name_entry = ["Riley", "Quinn", "Crawford", "Miller", "Barnes", "Short", "Cochran", "Miller", "Rhodes", "Lin",
                   "Pearson", "Smith", "Gutierrez", "Green", "Garcia", "Garcia", "Bryant", "Sanford", "Hughes",
                   "Hamilton", "Jenkins", "Powell", "Carr", "Cook", "Tyler", "Williams", "Kelly", "Newton", "Ross",
                   "Beasley", "Anderson", "Bell", "Beck", "Price", "Sanchez", "Hartman", "Brown", "Ruiz", "Maynard",
                   "Smith", "Jones", "Williams", "Hudson", "Roberts", "Ramirez", "Arnold", "Walker", "Stewart",
                   "Schultz", "Lopez"]  # Pre-made list for last name
address_entry = ["Paranaque City", "Taguig City", "Cavite City", "Munoz City", "Quezon City", "Palayan", "Vigan",
                 "Batac", "El Salvador", "Canlaon", "Candon", "Tandag", "La Carlota", "Tangub", "Davao City",
                 "Caloocan", "Zamboanga City", "Cebu City", "Antipolo", "Pasig", "Cagayan de Oro", "Valenzuela",
                 "Dasmariñas", "General Santos", "Bacoor", "San Jose del Monte", "Makati", "Las Piñas", "Bacolod",
                 "Muntinlupa", "Calamba", "Lapu-Lapu City", "Imus", "Angeles City", "Iloilo City", "Marikina",
                 "General Trias", "Pasay", "Mandaluyong", "Santa Rosa", "Biñan", "Tarlac City", "Malabon", "Lipa",
                 "Butuan", "Baguio", "Mandaue", "Iligan", "Cabuyao", "San Fernando"]  # Pre-made list for address
phone_number_entry = ["09456473521", "09226453712", "09238930213", "09257869504", "09326758493", "09056879650",
                      "09064567897", "09155768790", "09165676859", "09175768970", "09255678697", "09264597069",
                      "09355069784", "09364057678", "09373948567", "09964059687", "09975458097", "09074059687",
                      "09084056789", "09090394857", "09103330495", "09223049567", "09233045768", "09323049565",
                      "09332102938", "09455743521", "09235445372", "09238935761", "09257846504", "09326756753",
                      "09055674890", "09063045987", "09156954759", "09163049128", "09175890465", "09253304596",
                      "09263433068", "09353424324", "09364343463", "09373434356", "09963434687", "09974343467",
                      "09074343438", "09083434753", "09093243434", "09103434689", "09227890790", "09238908089",
                      "09328090980", "09338098768"]  # Pre-made list for phone number

while option != "6":  # I used while funtion to automatically repeat the process when the option is done
    introduction = '''
------------------------Address Book-----------------------

What would you like to do?
1. Add Contact
2. Edit Contact
3. Delete Contacts
4. View Contacts
5. Search Address Book
6. Exit
'''
    print(introduction)  # Obviously, this is for the options as per the activity
    option = input("Choose an option: ")  # Promting for the option

    # Clearly, we should use if, elif, and else functions for the options
    if option == "1":  # For adding contacts
        print('''
  >You chose adding a contact
  *****ADDING A CONTACT*****
''')
        # I used input function with the "title()" syntax to capitalize the first letter of their name.  We promt the user for their first name, last name, address, and phone number as well.
        first_name = (input("Input your first name: ").title())
        last_name = (input("Input your last name: ").title())
        address = (input("Input your address: ").title())
        phone_number = (input("Input your phone number: "))
        name_entry.append(f"{first_name} {last_name}")

        # The append() function was used to add the inputed information on the end of the respectives lists
        first_name_entry.append(f"{first_name}")
        last_name_entry.append(f"{last_name}")
        address_entry.append(f"{address}")
        phone_number_entry.append(f"{phone_number}")
        print("")

        # For printing the desired results
        print(f'''

        Successfully added a contact at entry #{address_entry.index(address)} 
        Here are the details:
        Name: {first_name} {last_name}
        Address: {address}
        Phone Number: {phone_number}
        ''')

    elif option == "2":  # For editing contacts
        print('''
  >You chose editing a contact
  *****EDITING A CONTACT*****
''')

        # For assigning the entry number by enumerating it
        for index, name in enumerate(name_entry):
            print(index, name)
        print("")

        edit_option = int(input(
            "What entry number you want to edit? "))  # In this line, we use Python function to prompt the user for the entry number he wants to edit
        print(f'''You want to edit {name_entry[edit_option]}
        Here are the details:
        Name: {name_entry[edit_option]}
        Address: {address_entry[edit_option]}
        Phone Number: {phone_number_entry[edit_option]}
        ''')

        # I personally added this feature to edit a specific detail to make a sense in editing a contact. We need to prompt the user what specific detail he wants to edit.
        edit_details = input(''' What specific detail you want to edit?
        a. Name
        b. Address
        c. Phone Number

        input a/b/c: ''').lower()  # I utilized lower function to avoid unnecessary errors: a / b / c

        if edit_details == "a":  # For editing the name
            print(f"Old Name: {name_entry[edit_option]}")
            new_name = str(input(f"New Name: "))
            name_entry.insert(edit_option, new_name)  # To insert the edited name in a specific index
            print(f'''Sucess!!!
            Updated Information
            Name: {name_entry[edit_option]}
            Address: {address_entry[edit_option]}
            Phone Number: {phone_number_entry[edit_option]}''')
            edit_option = edit_option + 1  # We need to remove the old contact that was already edited
            name_entry.remove(name_entry[edit_option])  # Removing the old contact
        elif edit_details == "b":  # For editing the address
            print(f"Old Address: {address_entry[edit_option]}")
            new_address = str(input(f"New Address: "))
            address_entry.insert(edit_option, new_address)  # To insert the edited address in a specific index
            print(f'''Sucess!!!
            Updated Information:
            Name: {name_entry[edit_option]}
            Address: {address_entry[edit_option]}
            Phone Number: {phone_number_entry[edit_option]}''')
            edit_option = edit_option + 1  # To remove the contact that was already edited
            address_entry.remove(address_entry[edit_option])  # Successfully deleted the old contact
        elif edit_details == "c":  # For editing the phone number
            print(f"Old Phone Number: {phone_number_entry[edit_option]}")
            new_phone_number = str(input(f"New Phone Number: "))
            phone_number_entry.insert(edit_option,
                                      new_phone_number)  # To insert the edited phone number in a specific index
            print(f'''Sucess!!!
            Updated Information
            Name: {name_entry[edit_option]}
            Address: {address_entry[edit_option]}
            Phone Number: {phone_number_entry[edit_option]}''')
            edit_option = edit_option + 1  # In order to remove the old phone number in the list
            phone_number_entry.remove(phone_number_entry[edit_option])  # Removed the phone number in the list
        else:
            print("Sorry. I do not understand that.")  # If the user inputs aside from a/b/c

    elif option == "3":  # For deleting the contact
        print('''
  >You chose deleting a contact
  *****DELETING A CONTACT*****
''')
        # To show the index(entry number) and as well as the name associated in the list
        for index, name in enumerate(name_entry):
            print(index, name)
        print("---end of the list---")
        print("")
        delete_option = int(input(
            "What entry number you want to delete? "))  # Prompts the user for the entry number he wants to be deleted
        print(f"Successfully deleted entry number {delete_option}, which is {(name_entry[delete_option])}.")
        name_entry.remove(f"{(name_entry[delete_option])}")
        address_entry.remove(f"{(address_entry[delete_option])}")
        phone_number_entry.remove(f"{(phone_number_entry[delete_option])}")
        print(".......")

        # Using Python function, we deleted the contact and the succeeding entries moved forward
        print("Updated version of the Address book: ")
        for index, name in enumerate(name_entry):
            print(index, name)  # Proof of updating the contact
        print("")

    elif option == "4":  # For viewing the contacts
        print('''
  >You chose viewing a contact
  *****VIEWING A CONTACT*****
''')
        for index, name in enumerate(name_entry):  # For showing the lists alongside with the entry number
            print(index, name)
        print("---end of list---")

        view_input = int(input("Input the entry number you want to view: "))  # Prompting to view a specific contact
        print(f"You want to view {name_entry[view_input]}")
        print(f'''
        Here are the details about {name_entry[view_input]}.
        Name: {name_entry[view_input]}
        Address: {address_entry[view_input]}
        Phone Number: {phone_number_entry[view_input]}
        ''')

    elif option == "5":  # For seaching a contact
        print('''
  >You chose searching a contact
  *****SEARCHING A CONTACT*****
''')
        # Prompts the user to search the address book by first name, last name, and contact number
        search_address_book = (input('''
    How do you want to search it?
    'a' by first name
    'b' by last name
    'c' by contact number

    Input a/b/c : ''').lower())  # The user was promted to choose between a / b / c

        if search_address_book == "a":  # For finding the first name
            view_first_name = input("What first name are you looking for? ").title()
            if view_first_name in first_name_entry:
                print(
                    f"Yes! We found {view_first_name} in our data")  # Displaying the first name entries that matched the query
            else:
                print(f"Sadly, We do not have {view_first_name} in our data")  # Notifying the user it doesn't exist
        elif search_address_book == "b":  # Looking for last name
            view_last_name = input("What last name are you looking for? ").title()
            if view_last_name in last_name_entry:
                print(
                    f"Yes! We found {view_last_name} in our data")  # Showing the last name entries that matched the query
            else:
                print(f"Sadly, We do not have {view_last_name} in our data")  # It does not match to any data
        elif search_address_book == "c":  # Finding for same contact number
            view_contact_number = input("What contact number are you looking for? ")
            if view_contact_number in phone_number_entry:
                print(f"Yes! We found {view_contact_number} in our data")  # If it matches in one of the data
            else:
                print(f"Sadly, We do not have {view_contact_number} in our data")  # If it does not match to any data
        else:
            print("Sorry. I do not understand that.")  # If the user entered information excluding from a/b/c

    elif option == "6":  # Closes the program
        print('''
        ---Main Menu---
        Thank you for choosing Address Book! We are pleased to serve you. Bye for now''')
    else:
        print("")
        print("Apologies. I do not understand that.")  # If the user entered a number which is not 1 to 6

