import get_categories
import view_module
import subprocess
def sub_menu (subs):
     """
     Displays the manage subscriptions menu and routes the user to
     add, edit, or delete subscription functions.

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
        print(CYAN + "1 -  add subscription")
        print("2 - edit current subscriptions")
        print("3 - delete subscription")
        print("4 - duplicate subscription")
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
                sub,cat = make_subscription(subs)
                add_subscription(subs, sub, cat)
                input("Subscriptions added successfully \nPress Enter to go back to the menu")

            case 2:
                print()
                edit_subscription(subs)
               
            case 3:
                print()
                delete_subscription(subs)
            
            case 4:
                print()
                duplicate_subscription(subs)

            case 0:
                break
                
            
            case _: 
              input("please select from the menu, then press Enter to try again ")
              continue

def duplicate_subscription (subs):
    """
    Prompts the user for subscription details and creates a subscription dictionary.

    Args:
        subs (dict): dictionary containing all the subscriptions
     
    Returns:
        None
    """
    # a loop for choosing category, with input validation 
    cat_list = get_categories.cat_to_list (subs)
    cat_num = 0
    view_module.display_subs(subs)
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
     # ask user for which subscription they want to duplicate, 
     # then use the make_subscription function to create a new subscription with the same details but a different name
    while True:
        try:
            sub_num = int(input("please enter the number of the subscription you want to duplicate ")) -1 # -1 to match user input to actual list index
        except ValueError:
            input("please enter only a number, then press Enter to try again")
            continue
        if sub_num < 0 or sub_num >= len(subs[cat]):
            input("invalid subscription number, then press Enter to try again")
            continue
        else:
            sub = subs[cat][sub_num].copy()
            break
     # ask user for new subscription name
    name = input("What is the name of the new subscription? ")
    sub['name'] = name
    add_subscription(subs, sub, cat)
    input("Subscriptions added successfully \nPress Enter to go back to the menu")

def make_subscription (subs): 
    """
    Prompts the user for subscription details and creates a subscription dictionary.

    Args:
        subs (dict): dictionary containing all the subscriptions
    
    Returns:
        tuple: A tuple containing:
            - sub (dict): Dictionary with keys 'name', 'cost', 'type'
            - cat (str): Category name ('Streaming', 'Internet And Comms', or 'Other Memberships')
    """
    cat_list = get_categories.cat_to_list(subs)
    # asks the user for subscription details and sets them to variables
    name = input ("please enter sub name  ")
    while True:
        try:
            cost = float(input("please enter cost "))
            if cost <= 0:
                input("Please enter a positive value. Press Enter to try again")
                continue
            else: 
                break
        except ValueError:
            input("please enter only a number, then press Enter to try again")
            continue

    print("please enter type ")
    while True:
     try:
      choice = int(input("1 - Monthly \n 2 - Yearly"))
     except ValueError:
       print("please enter a number only")
       continue
     match choice:
      case 1:
       typeofsub = "Monthly"
       break
      case 2:  
       typeofsub = "Yearly"
       break
      case _:
          input("please choose either 1 or 2, then press Enter to try again")
          continue


    # asks the to choose a category with a number input instead
    # of typing the whole category to avoid errors
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
    sub = {
        'name' : name, 
        'cost' : cost, 
        'type' : typeofsub,
    }
    return sub,cat # returns the sub directory with the inputs, and category

def add_subscription (subs,sub,cat): 
    """
    Appends a subscription to the selected category in the main subs dict.

    Args:
        subs (dict): dictionary containing all the subscriptions
        sub (dict): subscription dictionary to add
        cat (str): category name the subscription should be added to
    
    Returns:
       None
    """
    # adds the given sub directory to subs in the correct category
    subs[cat].append(sub)
    print("adding subscriptions....")

def edit_subscription (subs): 
    """
    Prompts the user for subscription and lets them edit the details of the subscription.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        dict: The updated subscriptions dictionary.
    """

    # a loop for choosing category, with input validation 
    cat_list = get_categories.cat_to_list (subs)
    cat_num = 0
    view_module.display_subs(subs)
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
    
    # a loop for choosing which subscription to edit from the displayed list based on the subscription number
    while True:
        try:
            sub_num = int(input("please enter the number of the subscription you want to edit ")) -1 # -1 to match user input to actual list index
        except ValueError:
            input("please enter only a number, then press Enter to try again")
            continue
        if sub_num < 0 or sub_num >= len(subs[cat]):
            input("invalid subscription number, then press Enter to try again")
            continue
        else:
            break
    # a loop for a small menu to choose which detail in the current selected subscription to edit
    while True:
        print("Please choose which detail you want to edit")
        try:
            choice = int(input("1 - name \n2 - cost \n3 - type "))
        except ValueError:
            input("please enter only a number, then press Enter to try again")
            continue
        
        match choice:
            case 1:
                subs[cat][sub_num]['name'] = input ("please enter new sub name  ")
                break
            case 2:
                try:
                 subs[cat][sub_num]['cost'] = float(input("please enter new cost "))
                except ValueError:
                    input("please enter only a number, then press Enter to try again")
                    continue
                break
            case 3:
                print("please enter type ")
                while True:
                    try:
                        choice2 = int(input("1 - Monthly \n 2 - Yearly"))
                    except ValueError:
                        print("please enter a number only")
                        continue
                    match choice2:
                        case 1:
                            subs[cat][sub_num]['type'] = "Monthly"
                            break
                        case 2:
                            subs[cat][sub_num]['type'] = "Yearly"
                            break
                        case _:
                            input("invalid choice, then press Enter to try again")
                            continue
                break
            case _:
                input("invalid choice, then press Enter to try again")
                continue
    
    # returns a message to the user that their edit has been made successfully 
    input (f" Subscription #{sub_num+1} in category {cat} edited successfully \n Press Enter to continue ")
    
    return subs

def delete_subscription (subs): 
    """
    Prompts the user for subscription that they want to delete
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        dict: The updated subscriptions dictionary.
    """
    # a loop with letting the user choose which category the subscription they want to choose is in
    cat_list = get_categories.cat_to_list (subs)
    cat_num = 0
    view_module.display_subs(subs)
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
    
    # a loop asking the user for the number of subscription they want to delete in the category
    
    while True:
        try:
            sub_num = int(input("please enter the number of the subscription you want to delete: ")) -1 
        except ValueError:
            input ("please enter only a number, then press Enter to try again")
            continue
        if sub_num < 0 or sub_num >= len(subs[cat]):
            input("invalid subscription number, then press Enter to try again")
            continue
        else:
            break
    
    #user confirmation for deleting the subscription . loops until the user input is 'yes / no'
    while True:
      print(f"\nSubscription to be deleted: \n#{sub_num+1}| Name: {subs[cat][sub_num]['name']} | Cost: {subs[cat][sub_num]['cost']} | Type: {subs[cat][sub_num]['type']}")
      user_conf = input(f"\nPlease type 'YES / NO' to confirm: ").lower()
      if user_conf == "yes":
        # removing the subscription
        del subs[cat][sub_num]
        input (f" Subscription #{sub_num+1} in category {cat} deleted successfully \n Press Enter to continue ")
        break
      elif user_conf == "no":
        input("Subscription is not deleted. Press Enter to continue")
        break
      else:
        print("Invalid value. Please type only 'YES / NO'")
    return subs