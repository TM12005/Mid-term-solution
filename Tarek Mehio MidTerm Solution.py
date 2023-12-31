import json
import re
import requests
from bs4 import BeautifulSoup 
import pprint


#this code to open (load) the json file
mytabs = {}
original_path = f"./mytabs.json"
myjsonfile = open(original_path, "r") #O(1)
jsondata = myjsonfile.read() #O(1)
mytabs = json.loads(jsondata)#O(n) n the size of the JSON file
myjsonfile.close()#O(1)


#Function to read a JSON file
def importTabs(original_path, mytabs): #O(n) n the size of the JSON file
   #f"C:/Users/t4m16/OneDrive/Desktop/mytabs2.json"
   try:
      original_path = input("Enter the path of the JSON file: ")
      myjsonfile = open(original_path, "r")
      jsondataa = myjsonfile.read()
      mytabs = json.loads(jsondataa)
      pprint.pprint(mytabs)
   except:
      print("invalid input")
   


#Function that takes path from the user and saves the file
def saveTabs(mytabs):#O(n) n being the length of the dictionary
   #check if the path is valid with the try
   try:
      file_path = input("Enter JSON file path: ")#O(1)
      with open(file_path, "w") as f:
               json.dump(mytabs, f)#O(n) n being the length of the dictionary
               print("Saved Succesfully")#O(1)
   except:
      print("Invalid path") #O(1)
   
   
   

#Sorting tabs with SelectionSort 
def sortAllTabs(mytabs):#O(n^2)
   border=0
   while border < len(mytabs)-1: #O(n), n being the of lenth mytabs
      minIndex=border 
      for i in range(border+1, len(mytabs)): # O(n) 
         if str(*mytabs[i].keys()).lower()<str(*mytabs[minIndex].keys()).lower(): #O(1)
            minIndex=i
      #swap the two elements
      temp=mytabs[border] #O(1)
      mytabs[border]=mytabs[minIndex]#O(1)
      mytabs[minIndex]=temp#O(1)
      
      border=border+1#O(1)
   pprint.pprint(mytabs)
   
   
   
#Open a nested Tab in the dictionary
def openNestedTab(mytabs):#O(n^3)
   viewTabs(mytabs)#O(n) n being number of list
   #take number from the list to pick tab family
   tab_number = int(input("Enter the number from the list"))#O(1)
   #Site name to be added
   new_tab = input("Enter the sub tab site")#O(1)
   #fetch the key name of the tab_number
   tab_name = str(*mytabs[tab_number].keys())#O(1)
   # print(tab_name)#O(1)
   #append the new value and save
   test = mytabs[tab_number][tab_name]#O(1)
   test.append(new_tab)#O(n), n being the length of the list
   with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:#O(1)
            json.dump(mytabs, f)#O(n) n being legth of dictionary
   print(test)#O(1)
   print("Sub Tab added")#O(1)
   
   
   
   
#Display the all the tabs
def displayAllTabs(mytabs):#O(n)
   for i in mytabs:#O(n) n being the length of the dictionary
      print(*i.keys(), end=" :\n")
      print(*i.values())
     


#to show the web scrape of the URL
def switchTab(mytabs):
   viewTabs(mytabs)#O(n) n being length of the dictionary mytabs
   user_input = input("Enter the number of the tab: ")
   #if the input was empty this if statement will not execut
   if user_input != "":#O(1)
    #checks if the input can be converted to string
        try:
            num_to_int = int(user_input)#O(1)
        except:
            print("Invalid input, Enter a number")#O(1)
            mainMenu()
   #check if input is None, and print the last element (webscrape)
   if user_input == "":#O(1)
      url_web = str(*mytabs[-1].values())#O(1)
      url_web = url_web[2:-2]#O(1)
      url_https = "https://"+url_web#O(1)
   #If number is out of range
   elif num_to_int > len(mytabs):#O(1)
      print("Invalid Number, number is too big")#O(1)
      mainMenu()
   elif num_to_int < 0:#O(1)
      print("Invalid number, number is too small")#O(1)
      mainMenu()
   else:
      #Remove the bracets from the string to be added to url_https
      url_web = str(*mytabs[num_to_int].values())#O(1)
      url_web = url_web[2:-2]#O(1)
      url_https = "https://"+url_web#O(1)
      
   #print the webscrape of the url_https link using beautifulsoup and requests
   #https://www.geeksforgeeks.org/python-web-scraping-tutorial/
   r = requests.get(url_https)#O(1)
   soup = BeautifulSoup(r.content, 'html.parser') #O(soup) soup the time it takes to fetch the web scrape
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
    result = re.match(pattern, "https://"+tab_url)#O(n) number of pattern length
    if result: #O(1)
        print("Tab added")#O(1)
    #Updating the dictionary and saving the changes in the JSON
        mytabs.append({tab_title : [tab_url]})#O(1)
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:#O(1)
            json.dump(mytabs, f)#O(1)
      #   print(mytabs)
    else:
        print("Invalid URL")#O(1)
        
        
        
        
#Function to view the tabs in the terminal       
def viewTabs(mytabs):#O(n)
   for i in range(len(mytabs)):#O(n) n being the length of mytabs
        print(i,"-", mytabs[i])#O(1)
        
        
        
        
#Close/remove the tab function
def closeTab(mytabs):#O(n)
    
    #print the tabs in the list
    viewTabs(mytabs)#O(n) n being the length of the dictionary
    
    ind_num = input("Enter the number of the tab you want to remove")#O(1)
    #if the input was empty this if statement will not execut
    if ind_num != "":#O(1)
    #checks if the input can be converted to string
        try:
            num_to_int = int(ind_num)#O(1)
        except:
            print("Invalid input, Enter a number")#O(1)
            mainMenu()
    #if the input is None, then close the last tab 
    if ind_num == "":#O(1)
       #remove the last element in the list
        mytabs.pop()#O(1)
        #save the changes
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:#O(1)
            json.dump(mytabs, f)#O(1)
   #check if input is out of range
    elif num_to_int > len(mytabs):#O(1)
        print("invalid number")#O(1)
    elif num_to_int < 0:#O(1)
        print("invalid number")#O(1)
    else:#O(1)
       #pop the num_to_int index element from the dictionary
        mytabs.pop(num_to_int)#O(1)
        print(mytabs)#O(1)
        with open("C:/Users/t4m16/Mid-term-solution/mytabs.json", "w") as f:#O(1)
            json.dump(mytabs, f)#O(1)
            



   

# Main menu that display option lists
def mainMenu():
    #List to display in terminal #O(1)
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    
    user_input = input("Please Choose A Number:")#O(1)
    #Continues While loop that exits only when user enter "9"
    while user_input is not "9":#O(1)
        if user_input == "1":#O(1)
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
            importTabs(original_path, mytabs)
            mainMenu() 
        else:
            print("Invalid Input, Please enter a number from the list")#O(1)
            user_input = int(input("Please Choose A Number:"))#O(1)
    else:
      print("GoodBye")      #O(1)
            
mainMenu()