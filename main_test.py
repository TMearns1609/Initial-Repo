from person import Person
import logic

choices =['1', '2', '3']
    
def Menu():
    '''Menu choices'''
    
    print("\n1 = Make a person \n2 = Print the list \n3 = Exit\n")

def Selection():
    '''The selection logic'''

    Menu()
    choice = input ("What do you wish to do?")
    while choice != choices[0] or choice != choices[1] or choice != choices[2]:
        choice = input ("What do you wish to do?")
        if choice == choices[0]:
            logic.make_person()
            Menu()
        if choice == choices[1]:
            logic.print_people()
            Menu()
        if choice == choices[2]:
            input("Press any key to exit")
            break


if __name__=='__main__':
    Selection()
    
