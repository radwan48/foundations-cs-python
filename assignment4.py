def displayMenu():
    print("1. Singly Linked List\n"
        + "2. Check if Palindrome\n"
        + "3. Priority Queue\n"
        + "4. Evaluate an Infix Expression\n"
        + "5. Graph\n"
        + "6. Exit")

def displayMenuLl():
    print("a. Add Node\n"
          + "b. Display Nodes\n"
          + "c. Search for & Delete Node\n"
          + "d. Return to main menu")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addNode(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.size += 1







def main():
    linked_list = Linkedlist()
    limit = 0
    choice = ""
    while limit < 4:
        displayMenu()
        choice = input("Enter your choice :")
        if choice == "1":
            limit = 0
            sub_choice = ""
            while sub_choice != "d" and limit < 4:
                displayMenuLl()
                sub_choice = input("Enter your choice :")
                if sub_choice == "a":
                    numeric_value = input("Enter a number to add: ")
                    try:
                        if "." in numeric_value or (numeric_value[0] == '-' and "." in numeric_value[1:]):
                            numeric_value = float(numeric_value)
                        elif numeric_value[0] == '-':
                            numeric_value = int(numeric_value)
                        else:
                            numeric_value = int(numeric_value)
                        linked_list.addNode(numeric_value)
                    except ValueError:
                        print("Please enter a valid numeric value.")
                elif sub_choice == "b":
                    pass
                elif sub_choice == "c":
                    pass
                elif sub_choice == "d":
                    pass
                else:
                    limit += 1
                    print("Invalid choice, please enter the correct choice.")
                    print(f"You have {4 - limit} attempts left")
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            exit()
        else:
            limit += 1
            print("Invalid choice, please enter the correct choice.")
            print(f"You have {4 - limit} attempts left")





if __name__ == '__main__':
    main()




