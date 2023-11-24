
# Main menu that display option lists
def mainMenu():
    
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    
    user_input = int(input("Please Choose A Number:"))
    
    while user_input != 9:
        if user_input == 1:
            openTab()
        elif user_input == 2:
            closeTab()
        elif user_input == 3:
            switchTab()
        elif user_input == 4:
            displayAllTabs()
        elif user_input == 5:
            openNestedTab()
        elif user_input == 6:
            sortAllTabs()
        elif user_input == 7:
            saveTabs()
        elif user_input == 8:
            importTabs()
        else:
            print("Invalid Input, Please enter a number from the list")
            user_input = int(input("Please Choose A Number:"))
            
            
mainMenu()