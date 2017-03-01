"""
    Use SortedDisc library
"""
from sortedcontainers import SortedDict

def print_menu():
    """
        print the menu
    """
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user

    # guard against non integer number
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except:
        print("Please enter a value between 1~5")
        continue

    print("the input is {}\n".format(menu_choice))
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        x = None
        y = None
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))

        # exception: No user in the dict.
        if x == None:
            print("There is no user.")
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")

        #in case the user reenter an existing name
        while name in usernames:
            print("Please enter a new user name")
            name = input("Name: ")
            
        username = input("User Name: ")
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            # remove an entry task 1
            del usernames[name]
        # in case the user doesn't exist
        else:
            print("{} doesn't exist.")
            

    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            y = usernames[name]
            print("The user name is {}\n".format(usernames[name]))
        #in case the user name in not in the dict
        else:
            print ("Username {} not found.\n".format(name))
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
