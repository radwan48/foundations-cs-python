import urllib.request

from urllib import request


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
            if 0 <= int(index) < len(list_tabs):
              list_tabs.pop(index)
              print(f"Closed tab at index {index}.")
            else:
                 print("Invalid index, please enter a valid index")
        else:
            print("Please enter a valid integer index")
    else:
        list_tabs.pop(-1)
        print("close last tab")

def switchTab():
    index_tab = input("Enter the index for the tab to display its content :")
    if len(list_tabs) == 0:
        print("No tabs open to display content. Please open a tab before attempting to display.")
    elif index_tab in list_tabs:
        for index_tab in range(len(list_tabs)):
          print(str(list_tabs[index_tab]))
      # display_url = request.urlopen(content)

    else:
        print(str((list_tabs[len(list_tabs)-1])))





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
            switchTab()
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