import csv

class Groccery_List_Organizer:

    def __init__(self):
        self.departments = {}
        self.user_dict = {}

    #dictionary to store each department and the items in that department
    def init_departments(self):
        #departments are in order of store location (entry to exit)
        with open("departments.txt", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            #skip header
            next(csvreader)
            for line in csvreader:
                department = line[0]
                item = line[1]
                if department not in self.departments.keys():
                    self.departments[department] = []
                self.departments[department].append(item)

    #open shopping list file, store items in a list
    def open_list(self):
        with open("grocery_list.txt", "r") as shopping_lst:
            items_lst = shopping_lst.read()
            items_lst = items_lst.splitlines()
            #filter out empty strings
            items_lst = list(filter(bool, items_lst))
        return items_lst

    #create a dict to store the items in the users shopping list and their corresponding department
    def init_user_dict(self):
        for department in list(self.departments.keys()):
            self.user_dict[department] = []

    #seach through shoppers list, checking what department each item is in
    #checks each condition and then prompts user if item not found
    def check_list(self, items_lst):
        for item in items_lst:
            for department in list(self.departments.keys()):
                if len(item.split()) == 1:
                    item_found = self.check_conditions(item, department)
                #check frozen first
                elif "frozen" in item.split():
                    item_found = True
                    department = "frozen"
                else:
                    item_found = self.multiword_item(item, department)
                #break once the item is found
                if item_found: 
                    self.user_dict[department].append(item) 
                    break
            #check to see if the item has not been added to the user_dict
            if item not in [item for items_lst in self.user_dict.values() for item in items_lst]:
                self.unknown_item(item)
    
    #checks if any of the words in item belong to any departments
    #Ex. cottage cheese where cheese is included in dairy
    def multiword_item(self, item, department):
        item_lst = item.split()
        for itm in item_lst:
            found = self.check_conditions(itm, department)
            if found:
                return True
        return False
    
    #first checks exact match, then singular vs plural, finally if the item is contained in the word or vice versa
    def check_conditions(self, item, department):
        #item is in one of the departments
        if item in self.departments[department]:
            return True      
        #plural item, singular item in department or singular item, plural item in department
        elif item[:-1] in self.departments[department] or item + 's' in self.departments[department]:
            return True
        #item contained within department item ex. grape(fruit) and (cream)er
        elif len([itm for itm in self.departments[department] if itm in item]) > 0:
            return True
        #vice versa
        elif len([itm for itm in self.departments[department] if item in itm]) > 0:
            return True
        return False

    def unknown_item (self, item):
        print("Sorry, I can't find {} in any department".format(item))
        print("Please enter the best suited deparment for {} out of the following choices: ".format(item))
        print(list(self.departments.keys()))
        while(True):
            department = input("Choice: ")
            #check to make sure its a valid department
            if department in self.departments.keys():
                #add item to users dict and departments file
                self.user_dict[department].append(item)
                self.add_to_departments(department, item)
                break
            else:
                print("Sorry that is not a valid department")

    #add to departments file for future reference
    def add_to_departments(self, department, item):
        with open("departments.txt", "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([department, item])
    
    #sort user list based on ordering of departments in the store
    def generate_ordered_list(self):
        ordered_lst = []
        for department in list(self.departments.keys()):
            ordered_lst += sorted(self.user_dict[department])
        return ordered_lst

    #write ordered list to output file
    def write_ordered_list(self, ordered_lst):
        with open("sorted_grocery_list.txt", "w") as output:
            for item in ordered_lst:
                output.write(item + "\n")

    def main(self):
        self.init_departments()
        items_lst = self.open_list()
        self.init_user_dict()
        self.check_list(items_lst)
        ordered_lst = self.generate_ordered_list()
        self.write_ordered_list(ordered_lst)

if __name__ == "__main__":
    g = Groccery_List_Organizer()
    g.main()