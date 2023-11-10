import urllib.request
from urllib.error import URLError, HTTPError



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
     if url.startswith(('http://', 'https://')):  # https://www.w3schools.com/python/ref_string_startswith.asp                                                        
        list_tabs.append(url)                           # For .startwith method
        opened_tabs[title] = url
     else:
      print("Please type a valid url")
      openTab()
    else:
        print("Please enter an a valid title for url")
        openTab()


def closeTab():
    if len(list_tabs) == 0:
        print("No tabs open to close. Please open a tab before attempting to close.")
        return
    index = input("Enter the index for the tab to close :")
    if index.strip():  ## to check if the input has empty string
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(list_tabs):
              list_tabs.pop(index)
              print(f"Closed tab at index {index}.")
            else:
                 print("Invalid index, please enter a valid index")
        else:
            print("Please enter a valid integer index")
    else:
        list_tabs.pop(-1)
        print("close last tab")


def readUrl(weburl):
    try:
      data = weburl.read()
      print(str(data))
    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except URLError as e:
         print(f"URL Error: {e.reason}")
    except Exception as e:
       print(f"An unexpected error occurred: {e}")




def switchTab(list_tabs):
    if len(list_tabs) == 0:
        print("No tabs open to display content. Please open a tab before attempting to display.")
        return
    index_tab = input("Enter the index for the tab to display its content :")
    if index_tab.strip():
        if index_tab.isdigit():
            index_tab = int(index_tab)
            if 0 <= index_tab < len(list_tabs):
             try:
                weburl = urllib.request.urlopen(list_tabs[index_tab])
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
        weburl = urllib.request.urlopen(list_tabs[-1])
        readUrl(weburl)
     except HTTPError as e:
         print(f"HTTP Error: {e.code}")
     except URLError as e:
         print(f"URL Error: {e.reason}")
     except Exception as e:
         print(f"An unexpected error occurred: {e}")




opened_tabs = {}
list_tabs = []

def main():
    displayMenu()
    choice = input("Enter your choice :")
    while choice != "9":
        if choice == "1":
            openTab()
            print(opened_tabs)
            print(list_tabs)
            main()
        elif choice == "2":
            closeTab()
            print(opened_tabs)
            print(list_tabs)
            main()
        elif choice == "3":
            switchTab(list_tabs)
            main()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        else:
            print("invalid input, please try again")
            main()




if __name__ == '__main__':
    main()