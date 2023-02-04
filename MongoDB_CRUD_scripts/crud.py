from connection import conn
from pprint import pprint

MENU = '''
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Press '1' for 'Create'
Press '2' for 'Read'
Press '3' for 'Update'
Press '4' for 'Delete'
Press '5' for 'Exit'
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''
print(MENU)

collection_obj = conn()


while True:

    inp = input("\nChoose any operation from 1-4: ")

    # Create
    if inp == '1': 
        print("\n---- Inserting Record ----")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile_number = input("Enter Mob. number: ")
        note = input("Enter Note: ")

        record = {
            'name' : name,
            'email' : email,
            'mobile_number' : mobile_number,
            'note' : note
        }

        collection_obj.insert_one(record)
        print("\n---- Record Inserted ----")

    # Read
    elif inp == '2': 
        print("\n---- Fetching Record ----")
        mobile_number = input("\nEnter Mob. number (or click 'Enter' to view all records): ")
        
        cond_dict = {}
        if mobile_number:
            cond_dict['mobile_number'] = mobile_number

        for post in collection_obj.find(cond_dict):
            print("\n")
            pprint(post)
        print("\n---- Record Fetched ----")

    # Update
    elif inp == '3':
        print("\n---- Updating Record ----")
        print("\n**** Hit 'Enter' for the fields that you don't want to give ****")
        mobile_number = input("\nEnter Mob. number: ")
        print("\n**** Enter new information ****\n")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        note = input("Enter Note: ")

        params = {}
        if name:
            params['name'] = name
        if email:
            params['email'] = email
        if name:
            params['note'] = note

        confirmation = input("\nDo you want to change the 'Mobile Number' ? Press 'Y' for Yes else 'N' for No: ")
        if confirmation.lower() == 'y':
             if mobile_number:
                params['mobile_number'] = mobile_number
        
        newvalues = { "$set": params }
        collection_obj.update_one({"mobile_number":mobile_number}, newvalues)
        print("\n---- Record Updated ----")

    # Delete
    elif inp == '4':
        print("\n---- Deleting Record ----")

        print("\n**** Hit 'Enter' for the fields that you don't want to give ****")
        print("\n **** Enter Deleting Criteria ****")
        mobile_number = input("\nEnter Mob. number: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        note = input("Enter Note: ")

        params = {}
        if name:
            params['name'] = name
        if email:
            params['email'] = email
        if name:
            params['note'] = note
        if mobile_number:
            params['mobile_number'] = mobile_number

        collection_obj.delete_many(params)
        
        print("\n---- Record Deleted ----")

    else:
        print("Good Bye!")
        break





