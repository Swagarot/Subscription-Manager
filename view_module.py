import subprocess
import get_categories
def sub_menu (subs):
     """
     Displays the view menu and routes the user to the selected view/search function.

     Args:
         subs (dict): dictionary containing all the subscriptions

     Returns:
         None
     """
     CYAN = "\033[36m"
     RESET = "\033[0m"
     while True:
        subprocess.run("cls", shell=True, check=False)  # For Windows
        print("\n\n\n")
        print("=" * 50)
        print(CYAN + "1 - display all subscriptions")
        print("2 - filter by category")
        print("3 - filter by type")
        print("4 - sort by cost")
        print("5 - search by name")
        print("0 - back" + RESET)
        print("=" * 50)
        print("\n")

        # tries to catch exception if the user inputs a wrong
        # type and also if the user interrupted with keyboard (ctrl+c)
        try:
            choice = int(input("Enter Selection "))
        except ValueError:
            input("Please enter a valid number, then press Enter to try again")
            continue
        except KeyboardInterrupt:
            print("\nExiting due to user interrupt...")
            break

        # match case for user menu selection
        match choice:
            case 1:
                print()
                display_subs(subs)
                input("Press Enter to go back to the menu")

            case 2:
                print()
                display_subs_by_cat(subs)
                input("Press Enter to go back to the menu")
               
            case 3:
                print()
                display_subs_by_type(subs)
                input("Press Enter to go back to the menu")

            case 4:
                print()
                sort_by_cost(subs)
                input("Press Enter to go back to the menu")

            case 5:
                print()
                search_subs(subs)
                input("Press Enter to go back to the menu")
            
            case 0:
                break
                
            
            case _: 
              input("please select from the menu, then press Enter to try again ")
              continue



def display_subs (subs):
    """
    This function takes the sub directory and prints it.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """
    # clearing terminal
    subprocess.run("cls", shell=True, check=False)  # For Windows
    
    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    # border_width set based on a template
    sample_line = f"#   | Name: {'':15} | Cost: {'':7} | Type: {'':12}|"
    border_width = len(sample_line)
    


    # prints each header of a category in the subs directory
    # then prints each sub in a formated way inside a table
    for category, items in subs.items():
     print (f"{CYAN} ==={category.upper()}=== {RESET}")
     print("-"*border_width)
     num = 0
     for item in items:
       num += 1 
       name = item['name']
       typee= item['type']
       cost = item['cost']
       line = f"#{str(num):<2} | Name: {str(name)[:15]:<15} | Cost: {str(cost)[:7]:<7} | Type: {str(typee)[:12]:<12}|"
       print(line)
       print("-"*border_width)


def search_subs (subs): 
    """
    Prompts the user for subscription that they want to look up, and then prints the results
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """ 
    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    # asking user for the name of the subscription
    search = input ("Enter the name or partial name of the subscription ")
    subprocess.run("cls", shell=True, check=False)
    print (CYAN+"Found these subscriptions: "+RESET)
   
    #simple counter to track results and print no resutls found if there are 0
    results = 0
    # nested loop to search within all the sub dict items for the requested subscription
    for category, items in subs.items():
        for item in items:
            name = item['name']
            typee= item['type']
            cost = item['cost']
            if search.lower().strip() in item['name'].lower():
                results += 1 
                line = f"| Name: {str(name)[:15]:<15} | Cost: {str(cost)[:7]:<7} | Type: {str(typee)[:12]:<12}|"
                print(f"{line} {CYAN} In {category} {RESET}")
    if results == 0:
        print("No Results Found")
     
def display_subs_by_cat (subs):
    """
    This function takes the sub directory and prints it.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """
    # clearing terminal
    subprocess.run("cls", shell=True, check=False)  # For Windows
    
    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    # border_width set based on a template
    sample_line = f"#   | Name: {'':15} | Cost: {'':7} | Type: {'':12}|"
    border_width = len(sample_line)
    
    cat_list = get_categories.cat_to_list (subs)
    cat_num = 0
    print("Choose a Category based on number")
    for category in cat_list:
        cat_num += 1 
        print(f"#{cat_num} {category}")
    while True:
        try:
            choice = int(input("Enter Number: ")) - 1 
            if choice < 0 or choice >= len(cat_list):
                input("number is out of range, then press Enter to try again")
                continue
            break
        except ValueError:
            input("please enter only a number, then press Enter to try again")
            continue
    cat = cat_list[choice]

    # prints each header of a category in the subs directory
    # then prints each sub in a formated way inside a table
    for category, items in subs.items():
         if category == cat:
            print (f"{CYAN} ==={category.upper()}=== {RESET}")
            print("-"*border_width)
            num = 0
            for item in items:
             num += 1 
             name = item['name']
             typee= item['type']
             cost = item['cost']
             line = f"#{str(num):<2} | Name: {str(name)[:15]:<15} | Cost: {str(cost)[:7]:<7} | Type: {str(typee)[:12]:<12}|"
             print(line)
             print("-"*border_width)
            break

def display_subs_by_type (subs):
    """
    This function takes the sub directory and prints it by the type selected.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """
    # clearing terminal
    subprocess.run("cls", shell=True, check=False)  # For Windows
    
    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    # border_width set based on a template
    sample_line = f"#   | Name: {'':15} | Cost: {'':7} | Type: {'':12}|"
    border_width = len(sample_line)

    print("please enter type ")
    while True:
        try:
            choice2 = int(input("1 - Monthly \n 2 - Yearly"))
            if choice2 == 1:
                selected_type = "Monthly"
                break
            if choice2 == 2:
                selected_type = "Yearly"
                break
            input("invalid choice, then press Enter to try again")
        except ValueError:
            print("please enter a number only")
            continue
    num = 0
    # prints matching subscriptions by selected type
    print (f"{CYAN} Showing all results from type: {selected_type} {RESET}")
    for  items in subs.values():
       for item in items:
        typee= item['type']
        if typee == selected_type:
         print("-"*border_width)
         num += 1
         name = item['name']
         cost = item['cost']
         line = f"#{str(num):<2} | Name: {str(name)[:15]:<15} | Cost: {str(cost)[:7]:<7} | Type: {str(typee)[:12]:<12}|"
         print(line)
         print("-"*border_width)
    if num ==0: 
       input (f"No Results Found in {selected_type}")
       
def sort_by_cost (subs):
    """
    This function takes the sub directory and prints it sorted by cost.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """
    # clearing terminal
    subprocess.run("cls", shell=True, check=False)  # For Windows
    
    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    # border_width set based on a template
    sample_line = f"#  | Name: {'':15} | Cost: {'':7} | Type: {'':12}|"
    border_width = len(sample_line)
    


    # prints each header of a category in the subs directory
    # then prints each sub in a formated way inside a table
    # flatten all subscriptions from all categories into one list
    flat = []
    for items in subs.values():
     for item in items:
        flat.append(item)
    # sort the flat list by cost, highest first
    flat = sorted(flat, key=lambda item: item['cost'], reverse=True)

    sample_line = f"#   | Name: {'':15} | Cost: {'':7} | Type: {'':12}|"
    border_width = len(sample_line)
    print (f"{CYAN} ===ALL SUBSCRIPTIONS SORTED BY COST (HIGHEST FIRST)=== {RESET}")
    print()
    print("-"*border_width)
    for i in range (0,len(flat)):
        name = flat[i]['name']
        typee= flat[i]['type']
        cost = flat[i]['cost']
        line = f"#{str(i+1):<2} | Name: {str(name)[:15]:<15} | Cost: {str(cost)[:7]:<7} | Type: {str(typee)[:12]:<12}|"
        print(line)
        print("-"*border_width)