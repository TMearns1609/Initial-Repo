from person import Person
people = []
        
def print_people():
    '''Iterates through the people list and prints our details'''

    for i in people:
        print('\n{0} {1} is {2} years old'.format(i.firstname, i.surname, i.age))

def make_person():
    '''Inputs for a person and returns them'''

    firstname =input("Enter your first name: \n")
    surname = input("Enter your surname: \n")
    dob = input("Enter your date of birth - in the form Mmm DD YYYY: \n")
    p1 = Person(firstname, surname, dob)
    people.append(p1)
