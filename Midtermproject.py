
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
        dict[title] = url
     else:
      print("Please type a valid url")
      openTab()
    else:
        print("Please enter an a valid title for url")
        openTab()


def closeTab():
    index = input("Enter the index for the tab to close :")
    if len(list_tabs) == 0:
        print("No tabs open to close. Please open a tab before attempting to close.")
    elif index in list_tabs:
     list_tabs.pop(int(index))
     print(f"Closed tab at index {index}.")
    else:
        list_tabs.pop()

dict = {}
list_tabs = []

def main():
    displayMenu()
    choice = input("Enter your choice :")
    while choice != "9":
        if choice == "1":
            openTab()
            print(dict)
            print(list_tabs)
            main()
        elif choice == "2":
            closeTab()
            main()
        elif choice == "3":
            pass
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