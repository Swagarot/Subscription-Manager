def cat_to_list (subs):
    """
    return a list of category names from the current subs directory 
    
    Args:
        subs (dict): dictionary containing all the subscriptions  
    
    Returns:
        cat_list (list): containing all the categories
    """

    # makes an empty list, goes over all categories in the subs dict and appends them to the list
    cat_list = []
    for category in subs.keys():
        cat_list.append(category)
    return cat_list