#phone book app cmd line program 

import pickle

phonebook = {}

""" This is a phonebook dictionary with user names as keys and phone numbers as values."""

def hello():
    print('Welcome to your phonebook app! ')
    print('Please select a number: ')
    print('1. Look up an entry ')
    print('2. Set an entry ')
    print('3. Delete an entry ')
    print('4. List all entries ')
    print('5. Save to database')
    print('6. Restore from previous database ')
    print('7. End program ')

    choice = int(input('Enter a number: '))

    if choice == 1:
        find()
    elif choice == 2:
        entry()
    elif choice == 3:
        remove()
    elif choice == 4:
        listall()
    elif choice == 5:
        savefile()
    elif choice == 6:
        restorefile()
    elif choice == 7:
        endprogram()
    else:
        hello()



"""The hello function prints instructions for the user to follow 
on the screen."""

    
def find():
    name = input('Name of contact? ')
    print(phonebook[name])
    hello()

""" Asks user for name of contact and returns the phone number for that user
from the dictionary phonebook."""

def entry():
    entryname = input('Name of contact: ')
    entrynumber = input('Enter phone number: ')
    phonebook[entryname] = entrynumber
    hello()
    

"""Adds entry name and entry number to dictionary phone book through user based inputs."""

def remove():
    
    x = input('Contact name to delete: ')
    del phonebook[x]
    hello()
    

""" Asks user for input, assigns input to variable, then deletes that
dictionary entry via method."""

def listall():
    for key, value in phonebook.items():
        print (key,':',value)
    hello()
    
"""This function lists all contents of the phone book dictionary."""

def savefile():
    myfile = open('phone.pickle', 'wb')
    pickle.dump(phonebook, myfile)
    myfile.close
    hello()

def restorefile():
    myfile=open('phone.pickle', 'rb')
    phonebook = pickle.load(myfile)
    hello()

""" Saves the database to pickle file. Need to work on this more."""

def endprogram():
    print('Goodbye!')

"""prints goodbye to console."""

hello()
