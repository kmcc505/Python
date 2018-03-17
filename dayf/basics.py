#Basic object exercises

class Person:
    def __init__(self, name, email, phone, friends=None):
        self.name=name
        self.email=email
        self.phone=phone
        if friends is None:
            friends = []
        self.friends=friends
      
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('{}s email: {}, {}s phone number: {}'.format(self.name, self.email, self.name, self.phone))

   


""" instantiate object of Person with name of 'Sonny' and deets from sheet."""
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

""" instantiate object of Person with name of 'Jordan' and deets from sheet."""
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

"""Have sonny greet jordan with greet method."""
sonny.greet(jordan)

"""Have jordan greet sonny with greet method."""
jordan.greet(sonny)

""" Print email and phone deets for Sonny."""
print(sonny.email, sonny.phone)

"""Now print email and phone for Jordan."""
print(jordan.email, jordan.phone) 

"""Add method to print out contact info for object of Person as noted in sheet."""
sonny.print_contact_info() 

"""Add a friends instance variable to the Person class."""
jordan.friends.append(sonny) 
jordan.friends.append('Anakin')

(print(len(jordan.friends)))
