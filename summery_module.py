import subprocess
def sub_menu (subs):
     """
     Displays the summary menu and routes the user to the selected summary function.

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
        print(CYAN + "1 - monthly total")
        print("2 - yearly total")
        print("3 - full summary")
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
                month_count,month_total = calc_month(subs)
                print (f"{CYAN} Monthly subscriptions: {RESET} {month_count}")
                print (f"{CYAN}Monthly Total (including amortized yearly) is: {RESET}{month_total}")
                input ("Press Enter to continue")
                

            case 2:
                print()
                year_count,year_total = calc_year(subs)
                print (f"{CYAN}Yearly subscriptions: {RESET}{year_count}")
                print (f"{CYAN}Yearly Total is: {RESET}{year_total}")
                input ("Press Enter to continue")
                

            case 3:
                print()
                full_summary(subs)
                input ("Press Enter to continue")
            
            case 0:
                break
                
            
            case _: 
              input("please select from the menu, then press Enter to try again ")
              continue



def full_summary (subs):
    """
    Prints a full summary including monthly total, yearly total,
    and per-category subscription counts.

    Args:
        subs (dict): dictionary containing all the subscriptions

    Returns:
        None
    """
    subprocess.run("cls", shell=True, check=False)
    month_count, month_total = calc_month(subs)
    year_count, year_total = calc_year(subs)
    cat_dict_year,cat_dict_month = count_type_by_cat(subs)
    print("="*50)
    print(f"Monthly Total (including amortized yearly): {month_total} | Yearly Total: {year_total}")
    print(f"Monthly Number of subs: {month_count} | Yearly Number of subs: {year_count}")
    for category in cat_dict_month:
        monthly = cat_dict_month[category]
        yearly = cat_dict_year[category]
        print(f"Category: {category} | Monthly Subs: {monthly} | Yearly Subs: {yearly}")
    print("="*50)














def calc_month (subs):
    """
    Calculates the monthly total based on all subscription costs.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        tuple: A tuple containing:
            - count_month (int): simple count of monthly subscriptions
            - monthtotal (float): total monthly cost including amortized yearly subscriptions
    """
    # sets ANSI colors in variables for later use
    count_month = 0
    monthtotal = 0 # defining month total before use to avoid errors

# nested loops to add up all costs in the subs dict and add to monthtotal
    for items in subs.values():
     for item in items:
       if item['type'] == "Monthly":
        count_month +=1
        monthtotal += item['cost']
       else: 
         monthtotal += (item['cost']/12)

         # prints the result (Monthly totaL)
    return count_month,monthtotal
def calc_year (subs): 
  """
    Calculates the yearly total based on all subscription costs.
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        tuple: A tuple containing:
            - count_year (int): simple count of yearly subscriptions
            - yeartotal (float): total yearly cost including annualized monthly subscriptions
   """
    # sets ANSI colors in variables for later use

  yeartotal = 0 #defining Year total before use to avoid errors
  count_year = 0

  # nested loops to add up all costs in the subs dict and add to year total
  for items in subs.values():
     for item in items:
       if item['type'] == "Yearly":
        count_year +=1
        yeartotal += (item['cost']*12)
       else: 
         yeartotal += item['cost']
         # prints the result (Yearly totaL)
  return count_year,yeartotal


def count_type_by_cat(subs):
 """
    Counts the number of Monthly and Yearly subscriptions per category.

    Args:
        subs (dict): dictionary containing all the subscriptions

    Returns:
        tuple: Two dicts keyed by category name:
            - category_count_year (dict): count of yearly subs per category
            - category_count_month (dict): count of monthly subs per category
 """
 category_count_month = {}
 category_count_year = {}

 # nested loops to count monthly and yearly subs per category
 for category, items in subs.items():
  count_month = 0
  count_year = 0
  for item in items:
    typee= item['type'] 
    if typee == "Monthly":
     count_month += 1
    elif typee == "Yearly":
     count_year += 1
  # store the counts for this category before moving to the next
  category_count_month[category] = count_month
  category_count_year[category] = count_year
 
 return category_count_year, category_count_month
                 

                

             






           