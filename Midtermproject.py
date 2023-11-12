import urllib.request
from urllib.error import URLError, HTTPError
import json
 ## CANT IMPORT : From bs4 import BeautifulSoup
tabs = []


def displayMenu():
    print("1. Open Tab\n"
        + "2. Close Tab\n"
        + "3. Switch Tab\n"
        + "4. Display All Tabs\n"
        + "5. Open Nested Tab\n"
        + "6. Clear All Tabs\n"
        + "7. Save Tabs\n"
        + "8. Import Tabs\n"
        + "9. Exit")


def openTab():

    title = input("Enter a title :")
    if title and title.isalnum():
     url = input("Enter the url :")
     if url.startswith(('http://', 'https://', 'www')):  # https://www.w3schools.com/python/ref_string_startswith.asp
         opened_tabs = {'title' : title, 'url' : url}            # For .startwith method
         tabs.append(opened_tabs)
     else:
      print("Please type a valid url")
      openTab()
    else:
        print("Please enter an a valid title for url")
        openTab()


def closeTab():
    if len(tabs) == 0:
        print("No tabs open to close. Please open a tab before attempting to close.")
        return
    index = input("Enter the index for the tab to close :")
    if index.strip():  ## to check if the input has empty string
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tabs):
              tabs.pop(index)
              print(f"Closed tab at index {index}.")
            else:
                 print("Invalid index, please enter a valid index")
        else:
            print("Please enter a valid integer index")
    else:
        tabs.pop(-1)
        print("Closed last tab")




def readUrl(weburl):    ##https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)
    try:  ## https://www.w3schools.com/python/python_try_except.asp
      data = weburl.read()  # try to do this block of code
      print(data)
    except HTTPError as e:                # except these HTTP errors and url errors
        print(f"HTTP Error: {e.code}")
    except URLError as e:
         print(f"URL Error: {e.reason}")
    except Exception as e:                # except any unexpected error other than http and url errors
       print(f"An unexpected error occurred: {e}")




def switchTab(tabs):
    if len(tabs) == 0:
        print("No tabs open to display content. Please open a tab before attempting to display.")
        return
    index_tab = input("Enter the index for the tab to display its content :")
    if index_tab.strip():
        if index_tab.isdigit():
            index_tab = int(index_tab)
            if 0 <= index_tab < len(tabs):
             try:
                weburl = urllib.request.urlopen(tabs[index_tab]['url'])
                readUrl(weburl)
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
        weburl = urllib.request.urlopen(tabs[-1]['url'])
        readUrl(weburl)
     except HTTPError as e:
         print(f"HTTP Error: {e.code}")
     except URLError as e:
         print(f"URL Error: {e.reason}")
     except Exception as e:
         print(f"An unexpected error occurred: {e}")


def openNestedTabs():
    if len(tabs) == 0:
        print("Cant open Nested tab, since tabs are empty")
        return
    nested_index = input("Please specify the index of parent tab where you want to add the nested tab")
    if nested_index.strip():
        if not nested_index.isdigit():
            print("index must be number")
            return
        nested_index = int(nested_index)
        if not (0 <= nested_index < len(tabs)):
            print("Invalid index, Index not found")
            return
        title = input("Title :")
        if title and title.isalnum():
            new_url = input("Enter url :")
            if new_url.startswith(('http://', 'https://')):

                nested_tabs = tabs[nested_index][title] = new_url
            else:
                 print("Please type a enter url")

        else:
             print("Please enter an a valid title for url")
    else:
      print("Invalid index , please enter a valid index")



def clearAllTabs():
    tabs.clear()
    print("Cleared all opened tabs")


def displayTitles(tabs):
    if len(tabs) != 0:
     for tab in tabs:
         print(tab.get('title'))
    else:
        print("There is no tab yet to display titles")


def saveTabs(tabs):  ## https://opensource.com/article/19/7/save-and-load-data-python-json
   if len(tabs) == 0:
       print("No tabs to save")
       return
   file_path = input("Enter the file path to save the tabs: ")
   with open(file_path, 'w') as f:
    json.dump(tabs, f)
    print(f"Saved tabs into {file_path}")


def importTab():
    file_path = input("Enter a file path to load : ")
    with open(file_path) as f:
        load = json.load(f)
        print(load)


def main():
    displayMenu()
    choice = input("Enter your choice :")
    while choice != "9":
        if choice == "1":
            openTab()
            print(tabs)
            main()
        elif choice == "2":
            closeTab()
            print(tabs)
            main()
        elif choice == "3":
            switchTab(tabs)
            main()
        elif choice == "4":
            displayTitles(tabs)
            print(nested_tabs)
            main()
        elif choice == "5":
            openNestedTabs()
            main()
        elif choice == "6":
            clearAllTabs()
            print(tabs)
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






if __name__ == '__main__':
    main()