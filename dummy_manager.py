import subprocess
import json

dummy_data = {
        'Streaming': [
            {"name": "Netflix", "cost": 17.99, "type": "Monthly"},
            {"name": "Spotify", "cost": 10.99, "type": "Monthly"},
            {"name": "Disney Plus", "cost": 139.90, "type": "Yearly"},
            {"name": "YouTube Premium", "cost": 13.99, "type": "Monthly"},
        ],
        'Internet And Comms': [
            {"name": "Fiber Internet", "cost": 49.90, "type": "Monthly"},
            {"name": "Cloud Backup", "cost": 5.99, "type": "Monthly"},
            {"name": "Domain Renewal", "cost": 62.00, "type": "Yearly"},
        ],
        'Other Memberships': [
            {"name": "Gym Membership", "cost": 39.90, "type": "Monthly"},
            {"name": "Amazon Prime", "cost": 79.90, "type": "Yearly"},
            {"name": "Canva Pro", "cost": 12.99, "type": "Monthly"},
        ],
    }
def sub_menu (subs):
     """
     Displays the dummy data menu and lets the user choose to replace or append dummy data.

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
        print(CYAN + "1 - replace data with dummy data")
        print("2 - append dummy data to existing data")
        print("3 - load dummy data from json (OVERWRITE)")
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
                load_dumb_data(subs)
                

            case 2:
                print()
                load_dummy_data_append(subs)
            
            case 3:
                print()
                loadfromfile(subs)
            case 0:
                break
            
            case _: 
              input("please select from the menu, then press Enter to try again ")
              continue




def load_dumb_data(subs): 
    """
    This function loads dummy data into the subs dict in the main file
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        None
    """

    # creates a dummy data dict with the same stracture as subs

    # clears the current subs dict and writes dummy data to it
    subs.clear()
    subs.update(dummy_data)
    input("DUMMY DATA LOADED SUCCESSFULLY, press Enter to continue")

def load_dummy_data_append(subs):
    """
    Appends dummy data to the existing subs dict without clearing it.

    Args:
        subs (dict): dictionary containing all the subscriptions

    Returns:
        None
    """
    for category, items in dummy_data.items():
        subs[category].extend(items)

    input("DUMMY DATA LOADED SUCCESSFULLY (APPENDED), press Enter to continue")

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
       input("File Not Found, press any key to return to menu")
       return
    except json.JSONDecodeError:
        input("File is not a valid json, press any key to return to menu")
        return
    
    subs.clear()
    subs.update(load)
    input (f"FILE {filename.strip().lower()} LOADED SUCCESSFULLY, ENTER ANY KEY TO CONTINUE")