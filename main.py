import dummy_manager
import manage_subs
import view_module
import storage_module
import summery_module
import subprocess

def main():
    """
    Initializes the application data and displays the main menu loop.

    Returns:
        None
    """
    # dictionary containing a list of subscription services
    # by category, inside the list there is a dictionary for each
    # subscription
    subs = {
        'Streaming': [],
        'Internet And Comms': [],
        'Other Memberships': [],
    }

    # sets ANSI colors in variables for later use
    CYAN = "\033[36m"
    RESET = "\033[0m"

    # clearing terminal
    subprocess.run("cls", shell=True, check=False)  # For Windows

    # simple welcome message
    print(CYAN + "Welcome to the Subscription Manager Application")
    print("Please Select an option from the following menu" + RESET)
    input("Press Enter to continue")

    # menu loop, prints options and asks the user for input
    while True:
        subprocess.run("cls", shell=True, check=False)  # For Windows
        print("\n\n\n")
        print("=" * 50)
        print(CYAN + "1 - manage subscriptions")
        print("2 - view / search / filter")
        print("3 - summary / status overview")
        print("4 - storage (save / load)")
        print("5 - load subscriptions (dummy data)")
        print("0 - exit" + RESET)
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
                manage_subs.sub_menu(subs)

            case 2:
                print()
                view_module.sub_menu(subs)

            case 3:
                print()
                summery_module.sub_menu(subs)

            case 4:
                print()
                storage_module.sub_menu(subs)

            case 5:
                print()
                dummy_manager.sub_menu(subs)

            case 0:
                print("Exiting.....")
                break

            case _:
                input("invalid input, then press Enter to try again")
                continue


if __name__ == "__main__":
    main()




