import json
from urllib2 import Request, urlopen, URLError
#this code to open (load) the json file
mytabs = {}
myjsonfile = open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "r")
jsondata = myjsonfile.read()
mytabs = json.loads(jsondata)

#Save a new tab in the JSON file
def openTab(mytabs):
    print(mytabs)
    #inputs from the user (Title and URL)
    tab_title = input("Enter tab name:")
    tab_url = input("Enter URL")
  
    req = Request(tab_url)
    try:
     response = urlopen(req)
    except URLError, e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print ('Reason: ', e.reason)
        elif hasattr(e, 'code'):
         print('The server couldn\'t fulfill the request.')
         print('Error code: ', e.code)
        else:
            print('URL is good!')
    #Updating the dictionary and saving the changes in the JSON
    mytabs.update({tab_title : tab_url})
    with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:
        json.dump(mytabs, f)
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
        if user_input == 1:
            openTab(mytabs)
            mainMenu()
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