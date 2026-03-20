# Subscription Manager 
A terminal-based app to track and manage your subscriptions.
You can add, edit, delete, and search subscriptions across categories like Streaming, Internet, and Other.
It also shows cost summaries (monthly/yearly), lets you filter and sort your list, and supports saving and loading your data from a file.

## Modules

**manage_subs.py** - handles adding, editing, and deleting subscriptions. when adding, you fill in the name, cost, billing type (monthly/yearly), and category.

**view_module.py** - handles all the ways to look at your subscriptions. you can display everything, search by name, filter by category or billing type, and sort by cost.

**summery_module.py** - gives you a cost overview. shows a full summary, calculates your total monthly and yearly spend, and counts how many subs you have per category.

**storage_module.py** - saves your subscriptions to a local file and loads them back. uses JSON format so the data is easy to read.

**dummy_manager.py** - loads a set of sample subscriptions so you can test the app without entering data manually.

**get_categories.py** - small helper that converts the categories dictionary into a simple list, used by other modules.


OPEN TASKS FOR CONTRIBUTORS
============================

here are some 3 easy tasks you can do

------------------------------------------------------------
FILE: manage_subs.py
------------------------------------------------------------
[ ] Duplicate subscription
    - Let the user pick an existing subscription and copy it under a new name.
    - Use the existing add_subscription() to insert the copy.

[ ] Cost input validation
    - In make_subscription(), reject negative numbers and non-numeric input for cost.
    - Print an error and ask again (loop until valid).

------------------------------------------------------------
FILE: view_module.py
------------------------------------------------------------
[ ] Sort by name (alphabetical)
    - Same pattern as the existing sort_by_cost(), but sort by the subscription name field.

