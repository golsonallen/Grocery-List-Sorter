Grocery List Sorter
===========================

By Griffin Olson-Allen <griffino@umich.edu>

This program sorts the items on a shopping list based on their order in the grocery store. It orders the items so that the user can
first, go around the perimeter of the store, then the aisles, and finally the frozen section. This is said to be the most efficient way to grocery shop.

The program has a set amount of known items and their associated departments, contained in departments.txt. For each item on the user's list, it will check whether that item is contained within each of the departments. After each item is checked and located in its appropriate department, the sorted version of the user's list is written to a text file.

It works best with more general items (chocolate as opposed to Hershey's) but does take several steps to try and identify
unknown items. If it can't exactly match an item on the user's shopping list with its known items, it will first check for a singular or plural version of the item. Next, it will check if an item in one of the program departments is contained within the word (ex. the user has creamer on their list, and cream is in the program's dairy section) and vice versa. It will break up multiple word items to check each word, with priority given to "frozen" and then the first word in the item (ex. frozen chicken will be in the frozen section while orange chicken will be put in the produce section since orange comes before chicken). 

As a last resort, the program will prompt the user for their best guess of the department of the unknown item. It will then store that item and department in departments.txt for future use, essentially learning the location of that item.