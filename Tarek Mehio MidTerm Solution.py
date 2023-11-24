import json
import re
#this code to open (load) the json file
mytabs = {}
myjsonfile = open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "r")
jsondata = myjsonfile.read()
mytabs = json.loads(jsondata)


#Save a new tab in the JSON file
def openTab(mytabs):
    print(mytabs)
    #inputs from the user (Title and URL)
    tab_title = input("Enter tab name: ")
    tab_url = input("Enter URL: ")
    #check if url is valid
    #https://snyk.io/blog/secure-python-url-validation/
    pattern = "^https:\/\/[0-9A-z.]+.[0-9A-z.]+.[a-z]+$"
    result = re.match(pattern, "https://"+tab_url)
    if result: 
        print("Tab added")
    #Updating the dictionary and saving the changes in the JSON
        mytabs.append({tab_title : tab_url})
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:
            json.dump(mytabs, f)
        print(mytabs)
    else:
        print("Invalid URL")

def closeTab(mytabs):
    
    #print the tabs in the list
    for i in range(len(mytabs)):
        print(i,"-", mytabs[i])
    
    ind_num = input("Enter the number of the tab you want to remove")
    #if the input was empty this if statement will not execut
    if ind_num != "":
    #checks if the input can be converted to string
        try:
            num_to_int = int(ind_num)
        except:
            print("Invalid input, Enter a number")
            mainMenu()
    
        
    if ind_num == "":
        mytabs.pop()
    elif num_to_int > len(mytabs):
        print("invalid number")
    elif num_to_int < 0:
        print("invalid number")
    else:
        mytabs.pop(num_to_int)
        print(mytabs)


# Main menu that display option lists
def mainMenu():
    #List to display in terminal
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    
    user_input = input("Please Choose A Number:")
    #Continues While loop that exits only when user enter "9"
    while user_input != 9:
        if user_input == "1":
            openTab(mytabs)
            mainMenu()
        elif user_input == "2":
            closeTab(mytabs)
            mainMenu()
        elif user_input == "3":
            switchTab()
        elif user_input == "4":
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