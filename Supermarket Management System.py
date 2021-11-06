# An inventory list consisiting of items in the supermarket
# Each item is a dictionary consisting of item name, item level, and item price
#key: item_name, item_level, item_price, value: corresponding value for each attribute
inventory = []

#Homepage of the app including the welcome and 6 activities that user can operate, including:
# view items, add items, purchase items, search items, edit items, and exit
# Only supermarket staffs are able to add items
#Each time user complete an activity, the app should automatically navigate back to the homepage
while True:
    print("Welcome to the Supermarket!")
    print("Select one:")
    print("1. View Items")
    print("2. Add Items")
    print("3. Purchase Items")
    print("4. Search Items")
    print("5. Edit Items")
    print("6. Exit")

    #Ask user to select an operation to perform
    #The number user enter must be from 1 to 6. Otherwise, it is an invalid selection
    selection = int(input())

    #View items:
    #1. Show the total number of items in the supermarket (i.e, the number of dictionaries in inventory list).
    #2. Show information for each item, including its name and its inventory level (i.e., the keys and values of each dictionary)
    #Note that 2. is only executed if there is at least 1 item in supermarket's inventory
    if selection == 1:
        print("**********View Items**********")
        print("The number of items available in the supermarket is: %d " %len(inventory))
        if len(inventory) != 0:
            print("Below are all available items in the supermarket.")
            for item in inventory:
                for key, value in item.items():
                    print("%s : %s " %(key, value))
        else:
            print("No items available in inventory.")
        print("Return to homepage")

    #Add items:
    #Inclusively for supermarket staff
    #1. User will keep adding items until there is no item left that he want to add
    #2. For each item, the system will require the user to enter name, level, price (i.e., corresponding to each dictionary's keys)
    #*Note that for item level, user must enter an integer and for price, user must enter a float with 2 decimal places
    elif selection == 2:
        print("**********Add Items**********")
        continue_adding = True
        while continue_adding:
            item = {}
            print("Please enter the information below:")
            item["item_name"] = input("Item name : ")

            while True:
                try:
                    item["item_level"] = int(input("Item level : "))
                    break
                except ValueError:
                    print("Item level must be an integer")
            while True:
                try:
                    item["item_price"] = float(input("Item price ($) : "))
                    break
                except ValueError:
                    print("Item price must be a decimal.")
            print("Item has been successfully added")
            inventory.append(item)

            keep_adding = int(input("Do you want to add more items?\n1.Yes\n2.No\n"))
            if keep_adding == 2:
                continue_adding = False
                print("Return to homepage")

    #Purchase items
    #Check to see if there is any item in the supermarket inventory
    #Ask the user the name of the item he wants to buy and the quantity he wants to buy
    #User can purchase multiple items at a time
    #Make sure to that items purchased are in the inventory and the quantities purchased don't exceed those in the inventory
    elif selection == 3:
        print("**********Purchase Items**********")

        if len(inventory) > 0:
            continue_purchasing = True
            while continue_purchasing:
                for item in inventory:
                    for key, value in item.items():
                        print("%s : %s " %(key, value))

                purchased_item = input("Enter the name of the item you want to purchase: ")
                purchased_level= int(input("Enter the quantity you want to purchase: "))

                for item in inventory:
                    if purchased_item == item["item_name"]:
                        if item["item_level"] != 0 :
                            if purchased_level <= item["item_level"]:
                                print("Pay %d at checkout counter." %(item["item_price"]* purchased_level))
                                item["item_level"] -= purchased_level
                            else:
                                print("There are only %d items left." %item["item_level"])
                        else:
                            print("Out of stock!")

                keep_purchasing = int(input("Do you want to purchase more items?\n1. Yes\n2. No\n"))
                if keep_purchasing == 2:
                    continue_purchasing = False
                    print("Return to homepage")
        else:
            print("No items available!")
            print("Return to homepage")

    #Search items
    #User must enter the name of the item (case insensitive)
    #Returns the details of item if it exists
    elif selection == 4 :
        print("**********Search Items**********")
        search_item = input("Enter the items name to search in inventory : ")
        for item in inventory:
            if item["item_name"].lower() == search_item.lower():
                print("The item named ' + find_item + ' is displayed below with its details.")
                print(item)
            else:
                print("Item Not Found")
        print("Return to Homepage")

    #Edit items
    #Ask user to enter the name of the item he wants to edit (case insensitive)
    #If item exists, show him the current details of that item first
    elif selection == 5 :
        print("**********Edit Items**********")
        edit_item = input("Enter the name of the item that you want to edit : ")
        for item in inventory:
            if edit_item.lower() == item["item_name"].lower():
                print("Here are the current details of " + edit_item)
                print(item)
                item["item_name"] = input("Item name : ")
                while True:
                    try:
                        item["item_level"] = int(input("Item level : "))
                        break
                    except ValueError:
                        print("Item level must be an integer.")
                while True:
                    try:
                        item["item_price"] = float(input("Price $ : "))
                        break
                    except ValueError:
                        print("Item price must be a decimal.")
                print("Item has been successfully updated")
                print(item)
            else:
                print("Item Not Found")
        print("Return to Homepage")

    #Exit (i.e., homepage not shown)
    elif Selection == 6 :
        print("Exited!")
        break

    #If user select a number that is not from 1 to 6, return invalid message
    else:
         print("Invalid!")
