import json
import re
import requests
from bs4 import BeautifulSoup 
import pprint


#this code to open (load) the json file
mytabs = {}
original_path = "C:/Users/t4m16/Mid-term-solution/mytabs.json"
myjsonfile = open(original_path, "r")
jsondata = myjsonfile.read()
mytabs = json.loads(jsondata)
myjsonfile.close()

def importTabs(original_path):
   mytabs = {}
   original_path = "C:/Users/t4m16/OneDrive/Desktop/mytabs2.json"
   myjsonfile = open(original_path, "r")
   jsondata = myjsonfile.read()
   mytabs = json.loads(jsondata)
   myjsonfile.close()
   print(original_path)
   # return original_path


def saveTabs(mytabs):
   try:
      file_path = input("Enter JSON file path: ")
      file_path = file_path+"/mytabs.json"
      with open(file_path, "w") as f:
               json.dump(mytabs, f)
   except:
      print("Invalid path") 
   print("Saved Succesfully")


def sortAllTabs(mytabs):
   border=0
   
   while border < len(mytabs)-1: #O(n), n being the length of the list
      minIndex=border # contain the index of the minimum element
      for i in range(border+1, len(mytabs)): # to find the index of the minimum element, O(n)
         if str(*mytabs[i].keys()).lower()<str(*mytabs[minIndex].keys()).lower(): #O(1), is the line that specifies the order
            minIndex=i
      #swap the two elements
      temp=mytabs[border] #O(1)
      mytabs[border]=mytabs[minIndex]
      mytabs[minIndex]=temp
      
      border=border+1
   pprint.pprint(mytabs)
   

def openNestedTab(mytabs):
   viewTabs(mytabs)
   tab_number = int(input("Enter the number from the list"))
   new_tab = input("Enter the sub tab site")
   tab_name = str(*mytabs[tab_number].keys())
   print(tab_name)
   # for i in range(len(mytabs)):
   test = mytabs[tab_number][tab_name]
   test.append(new_tab)
   print("Sub Tab added")
   
def displayAllTabs(mytabs):
   for i in mytabs:
      print(*i.keys(), end=" :\n")
      print(*i.values())
     



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
      url_web = url_web[2:-2]
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
            displayAllTabs(mytabs)
            mainMenu()
        elif user_input == "5":
            openNestedTab(mytabs)
            mainMenu()
        elif user_input == "6":
            sortAllTabs(mytabs)
            mainMenu()
        elif user_input == "7":
            saveTabs(mytabs)
            mainMenu()
        elif user_input == "8":
            importTabs(mytabs)
            mainMenu()
        else:
            print("Invalid Input, Please enter a number from the list")
            user_input = int(input("Please Choose A Number:"))
            
            
mainMenu()