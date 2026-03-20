import json
import subprocess
def sub_menu (subs):
     """
     Displays the storage module menu and routes the user to
     load or save to a file

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
        print(CYAN + "1 - save to file")
        print("2 - load from file(OVERWRITE)")
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
                savetofile(subs)

            case 2:
                print()
                loadfromfile(subs)
            
            case 0:
                break
                
            
            case _: 
              input("please select from the menu, then press Enter to try again ")
              continue



def savetofile (subs):
    """
    This function saves the current subs dict to a json file
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """

    # take the filename from the user and strips spaces  to avoid mistakes
    filename = input("enter file name to save ").strip()

    # searches for if the file already exist and overwrites it if does or just makes a new one 
    # if it doesn't with the name the user gave
    if not filename.endswith(".json"): filename += ".json"
    with open(filename, "w") as f:
        json.dump(subs, f, indent=2)
    input (f"FILE {filename.strip().lower()} SAVED SUCCESSFULLY, PRESS ENTER TO CONTINUE")




def loadfromfile (subs):
    """
    This function loads a json file to the subs dict
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """
    # take the filename from the user and strips spaces to avoid mistakes
    filename = input("enter file name to load ").strip()

    # searches for if the file already exist and loads it
    if not filename.endswith(".json"): filename += ".json"
    try:
        with open(filename, "r") as f:
            load = json.load(f)
    except FileNotFoundError:
        input("File Not Found, press Enter to return to the menu")
        return
    except json.JSONDecodeError:
        input("File is not a valid json, press Enter to return to the menu")
        return
    
    subs.clear()
    subs.update(load)
    input (f"FILE {filename.strip().lower()} LOADED SUCCESSFULLY, PRESS ENTER TO CONTINUE")