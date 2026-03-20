OPEN TASKS FOR CONTRIBUTORS
============================

Each task below is small and self-contained.
Pick one, implement it, and open a pull request.

------------------------------------------------------------
FILE: manage_subs.py
------------------------------------------------------------
- [x] Duplicate subscription
    - Let the user pick an existing subscription and copy it under a new name.
    - Use the existing add_subscription() to insert the copy.

- [ ] Cost input validation
    - In make_subscription(), reject negative numbers and non-numeric input for cost.
    - Print an error and ask again (loop until valid).

------------------------------------------------------------
FILE: view_module.py
------------------------------------------------------------
- [ ] Sort by name (alphabetical)
    - Same pattern as the existing sort_by_cost(), but sort by the subscription name field.

------------------------------------------------------------
FILE: summery_module.py
------------------------------------------------------------
- [ ] Most expensive subscription
    - Loop over all categories, find and print the subscription with the highest cost.

- [ ] Cheapest subscription
    - Same as above but find the minimum cost.

------------------------------------------------------------
FILE: storage_module.py
------------------------------------------------------------
- [ ] Export to CSV
    - Add an export_to_csv() function using Python's built-in csv module.
    - Each row: name, category, cost, billing cycle (or whatever fields exist).

- [ ] Last saved timestamp
    - When saving, write the current date/time into the file (or a sidecar .txt).
    - When loading, read and print it so the user knows how fresh the data is.

