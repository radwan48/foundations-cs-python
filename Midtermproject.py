import urllib.request
from urllib.error import URLError, HTTPError
import json

  # Cant import urlib3
  # CANT IMPORT : From bs4 import BeautifulSoup
tabs = []


def displayMenu(): # displaying menu for the user
    print("1. Open Tab\n"
        + "2. Close Tab\n"
        + "3. Switch Tab\n"
        + "4. Display All Tabs\n"
        + "5. Open Nested Tab\n"
        + "6. Clear All Tabs\n"
        + "7. Save Tabs\n"
        + "8. Import Tabs\n"
        + "9. Exit")


def openTab():  # worst case is O(n)

    title = input("Enter a title :")
    if title and title.isalnum():  #if title is not empty and doesn't have symbols
     url = input("Enter the url :")
     if url.startswith(('http://', 'https://', 'www.')):  # https://www.w3schools.com/python/ref_string_startswith.asp
         opened_tabs = {'title' : title, 'url' : url}            # For .startwith method
         tabs.append(opened_tabs)                # add dictionary opened_tabs to tabs list
     else:
      print("Please type a valid url")
      openTab()              # if it is invalid url we call the openTab func again
    else:
        print("Please enter an a valid title for url")
        openTab()


def isEmptytabs(message=""):  # worst case O(1)  # message will be a string to be orinted
    if len(tabs) == 0:    # if tabs is empty
        print(message)    # I will use this message in function with different strings
        return False
    return True


def closeTab():  # worst case time complexity is O(n)
    if not isEmptytabs("No tabs open to close. Please open a tab before attempting to close."):
        return  # return to exit the code and return nothing
    index = input("Enter the index for the tab to close :")
    if index.strip():  ## to check if the input has empty string so here if it is not empty
        if index.isdigit():  ## check if index is a number
            index = int(index)
            if 0 <= index < len(tabs):  #  if index between the length of tabs
              tabs.pop(index)
              print(f"Closed tab at index {index}.")
            else:
                 print("Invalid index, please enter a valid index")
        else:
            print("Please enter a valid integer index")
    else:
        tabs.pop(-1)
        print("Closed last tab")




def readUrl(weburl):    ##https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser) # worst case is O(n)
    try:  ## https://www.w3schools.com/python/python_try_except.asp
      data = weburl.read()  # try to do this block of code
      print(data)
    except HTTPError as e:                # except these HTTP errors and url errors
        print(f"HTTP Error: {e.code}")
    except URLError as e:
         print(f"URL Error: {e.reason}")
    except Exception as e:                # except any unexpected error other than http and url errors
       print(f"An unexpected error occurred: {e}")




def switchTab(tabs): ## worst case is O(n)
    if not isEmptytabs("No tabs open to display content. Please open a tab before attempting to display."):
        return
    index_tab = input("Enter the index for the tab to display its content :")
    if index_tab.strip():
        if index_tab.isdigit():
            index_tab = int(index_tab)
            if 0 <= index_tab < len(tabs):
             try:
                weburl = urllib.request.urlopen(tabs[index_tab]['url'])  # I used this method to open the specific url
                readUrl(weburl)                                          # which it's in list tab at index_tab at 'url'
             except HTTPError as e:
                 print(f"HTTP Error: {e.code}")
             except URLError as e:
                 print(f"URL Error: {e.reason}")
             except Exception as e:
                 print(f"An unexpected error occurred: {e}")

            else:
                print("invalid index , please enter a valid index")
        else:
            print("invalid index, please enter a valid integer index")
    else:
     try:
        weburl = urllib.request.urlopen(tabs[-1]['url'])  # this will display last tab html content
        readUrl(weburl)
     except HTTPError as e:  # handling HTTP error and url erros
         print(f"HTTP Error: {e.code}")
     except URLError as e:
         print(f"URL Error: {e.reason}")  # except any unexpected error other than http and url errors
     except Exception as e:
         print(f"An unexpected error occurred: {e}")


def openNestedTabs():  # worst case is O(n)
    if not isEmptytabs("Cant open Nested tab, since tabs are empty"):
        return
    nested_index = input("Please specify the index of parent tab where you want to add the nested tab :")
    if nested_index.strip():  # if it is not empty
        if not nested_index.isdigit():  # if user type other than digits it will return nothing and will print a message
            print("index must be number")
            return
        nested_index = int(nested_index)  # casting from  a sting input to integer to be the index
        if not (0 <= nested_index < len(tabs)):  # if index is not in tabs it will return nothing
            print("Invalid index, Index not found")
            return
        title = input("Title :")
        if not title or not title.isalnum():
            print("Please enter an a valid title for url")
            return
        new_url = input("Enter url :")
        if new_url.startswith(('http://', 'https://', 'www.')):  # url should start with https:// or http:// or www.
             tabs[nested_index][title] = new_url           # add dictionary to opened tab
        else:
            print("Please type a valid url")   # url doesn't start with the requirements, so it will print this message
    else:
      print("Invalid index , please enter a valid index")



def clearAllTabs():  # worst case is O(n)
    tabs.clear()  #Clear  all tabs
    print("Cleared all opened tabs")


def displayTitles(tabs):  # worst case is O(n)
    if not isEmptytabs("There is no tab yet to display titles"):
        return
    for tab in tabs:
         print(tab.get('title'))   # print titles in tabs


def saveTabs(tabs):   # worst case is O(n)           ## https://opensource.com/article/19/7/save-and-load-data-python-json
   if not isEmptytabs("No tabs to save"):
       return
   file_path = input("Enter the file path to save the tabs: ")
   try:
     with open(file_path, 'w') as f:
      json.dump(tabs, f)
      print(f"Saved tabs into {file_path}")
   except Exception as f:  ## cant find on the internet handling error blocks
       print(f"An unexpected error occurred: {f}")


def importTab():  # worst case is O(n)
    file_path = input("Enter a file path to load : ")  #input a strint for file path
    try:                                    # try
     with open(file_path) as f:        # | #this block of code
       load = json.load(f)             # |  load the file
       print(load)                     # | print the content
    except ValueError as f:                                  # handling Value error using except
        print(f"Value error: {f}")
    except Exception as f:
        print(f"An unexpected error occurred: {f}")



print("Hello User")
def main():  # worst case is O(n)

    displayMenu()
    choice = input("Enter your choice :")
    while choice != "9":
        if choice == "1":
            openTab()
            main()
        elif choice == "2":
            closeTab()
            main()
        elif choice == "3":
            switchTab(tabs)
            main()
        elif choice == "4":
            displayTitles(tabs)
            main()
        elif choice == "5":
            openNestedTabs()
            main()
        elif choice == "6":
            clearAllTabs()
            main()

        elif choice == "7":
            saveTabs(tabs)
            main()
        elif choice == "8":
            importTab()
            main()
        else:
            print("invalid input, please try again")
            main()
    else:
        exit()




main()