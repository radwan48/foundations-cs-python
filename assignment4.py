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

    def displayNodes(self):
        if self.size == 0:
            print("There is no Nodes to show, please add nodes first to display .")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")


    def searchAndRemove(self, value):
        if self.size == 0:
            print("Cant search and delete the Node since no Nodes yet .")
            return
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if current == self.head:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                self.size -= 1
                print(f"Node remove with value: {value} removed.")
                return
            previous = current
            current = current.next
        print(f"Node with value: {value} not found.")

def inputNumeric(numeric_value):

    try:
        if "." in numeric_value or (numeric_value[0] == '-' and "." in numeric_value[1:]):
             numeric_value = float(numeric_value)
        elif numeric_value[0] == '-':
             numeric_value = int(numeric_value)
        else:
          numeric_value = int(numeric_value)

    except ValueError:
            print("Please enter a valid numeric value.")

def isPalindrome(s):
    if len(s) == 0:
        print("Empty string, please type a string")
        return
    s = s.lower()
    list1 = list(s)
    list2 = []
    original_list = list1.copy()
    while list1:
        list2.append(list1.pop())
    if original_list == list2:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")



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
                    inputNumeric(numeric_value)
                    linked_list.addNode(numeric_value)
                elif sub_choice == "b":
                    linked_list.displayNodes()
                elif sub_choice == "c":
                    input_value = input("Enter Node value to remove :")
                    inputNumeric(input_value)
                    linked_list.searchAndRemove(input_value)
                elif sub_choice == "d":
                    main()
                else:
                    limit += 1
                    print("Invalid choice, please enter the correct choice.")
                    print(f"You have {4 - limit} attempts left")
        elif choice == "2":
            palindrome_string = input("Enter a string to check if it is palindrome or not :")
            isPalindrome(palindrome_string)
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




