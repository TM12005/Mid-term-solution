import json
import re
import requests
from bs4 import BeautifulSoup 
#this code to open (load) the json file
mytabs = {}
myjsonfile = open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "r")
jsondata = myjsonfile.read()
mytabs = json.loads(jsondata)

def openNestedTab(mytabs):
   viewTabs(mytabs)
   tab_number = int(input("Enter the number from the list"))
   tab_name = str(*mytabs[tab_number].keys())
   print(tab_name)
   # for i in range(len(mytabs)):
   test = str(mytabs[tab_number][tab_name])
   print(test)
   



def switchTab(mytabs):
   viewTabs(mytabs)
   user_input = input("Enter the number of the tab: ")
   #if the input was empty this if statement will not execut
   if user_input != "":
    #checks if the input can be converted to string
        try:
            num_to_int = int(user_input)
        except:
            print("Invalid input, Enter a number")
            mainMenu()
   if user_input == "":
      url_web = str(*mytabs[-1].values())
      url_https = "https://"+url_web
   elif num_to_int > len(mytabs):
      print("Invalid Number, number is too big")
      mainMenu()
   elif num_to_int < 0:
      print("Invalid number, number is too small")
      mainMenu()
   else:
      url_web = str(*mytabs[num_to_int].values())
      url_web = url_web[2:-2]
      print(url_web)
      
      url_https = "https://"+url_web
      # print(url_web)
      # print("https://".map(str, url_web))
   
   # print(url_https)
   
   
   #https://www.geeksforgeeks.org/python-web-scraping-tutorial/
   r = requests.get(url_https)
   soup = BeautifulSoup(r.content, 'html.parser') 
   print(soup.prettify()) 
   
   
   
   
#Save a new tab in the JSON file
def openTab(mytabs):
   #  print(mytabs)
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
        mytabs.append({tab_title : [tab_url]})
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:
            json.dump(mytabs, f)
      #   print(mytabs)
    else:
        print("Invalid URL")
        
        
        
        
def viewTabs(mytabs):
   for i in range(len(mytabs)):
        print(i,"-", mytabs[i])
        
        
        
        
#Close/remove the tab function
def closeTab(mytabs):
    
    #print the tabs in the list
    viewTabs(mytabs)
    
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
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:
            json.dump(mytabs, f)
    elif num_to_int > len(mytabs):
        print("invalid number")
    elif num_to_int < 0:
        print("invalid number")
    else:
        mytabs.pop(num_to_int)
        print(mytabs)
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:
            json.dump(mytabs, f)
            



   

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
    while user_input != "9":
        if user_input == "1":
            openTab(mytabs)
            mainMenu()
        elif user_input == "2":
            closeTab(mytabs)
            mainMenu()
        elif user_input == "3":
            switchTab(mytabs)
            mainMenu()
        elif user_input == "4":
            displayAllTabs()
        elif user_input == "5":
            openNestedTab(mytabs)
            mainMenu()
        elif user_input == "6":
            sortAllTabs()
        elif user_input == "7":
            saveTabs()
        elif user_input == "8":
            importTabs()
        else:
            print("Invalid Input, Please enter a number from the list")
            user_input = int(input("Please Choose A Number:"))
            
            
mainMenu()