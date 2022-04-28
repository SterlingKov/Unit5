dictionary = {
    'lol':'laugh out loud',
    'wbu':'what about you',
    'ofc':'of course',
    'ft':'FaceTime'
}

while True:
    inpt = input("which abbreviation would you like to look up? - ")
    if inpt in dictionary:
        print(dictionary[inpt])
    elif inpt == 'Commands':
        print("List of commands: Change, Print Dictionary, Delete")
    elif inpt == 'Change':
        inpt2 = input("Which abbreviation would you like to change? - ")
        if inpt2 in dictionary:
            defnt2 = input(f"What would you like to change '{inpt2}' to? - ")
            dictionary[inpt2] = defnt2
    elif inpt == 'Print Dictionary':
        print(dictionary)
    elif inpt == 'Delete':
        inpt3 = input("Which abbreviation would you like to delete? - ")
        if inpt3 in dictionary:
            dictionary.pop(inpt3)
        else:
            print(f"'{inpt3}' is not in the dicionary")
    else:
        resp = input('Sorry, that word is not in the dictionary. Would you like to add it? - ')
        if resp == 'yes':
            defnt = input("What is the definition for the abbreviation? - ")
            dictionary[inpt] = defnt
        else:
            pass