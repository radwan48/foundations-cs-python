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


def displayMenuStudent():
    print("a. Add a student\n"
          + "b. Interview a student\n"
          + "c. Return to main menu")


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


class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
class Node1:
    def __init__(self, student):
       self.student = student
       self.next = None

class PriorityQueue:
    def __init__(self):
      self.head = None
      self.size = 0

    def enqueue(self, student):
        node = Node1(student)
        if self.size == 0:
            self.head = node
            self.size += 1
        else:
            current = self.head
            previous = None
            while current:
                 if node.student.good_attitude and not current.student.good_attitude:
                     node.next = current
                     if not previous:
                         self.head = node
                     else:
                         previous.next = node
                     self.size += 1
                     return
                 elif current.student.good_attitude and not node.student.good_attitude:
                     node.next = current.next
                     current.next = node
                     self.size += 1
                     return
                 else:
                     if (node.student.final_grade > current.student.final_grade or
                      (node.student.final_grade == current.student.final_grade
                      and node.student.midterm_grade > current.student.midterm_grade)):
                        node.next = current
                        if not previous:
                            self.head = node
                        else:
                            previous.next = node
                        self.size += 1
                        return
                     elif node.student.final_grade < current.student.final_grade or (
                        node.student.final_grade == current.student.final_grade
                        and node.student.midterm_grade < current.student.midterm_grade):

                         node.next = current.next
                         current.next = node
                         self.size += 1
                         return
                     else:
                        if node.student.midterm_grade > current.student.midterm_grade:
                            node.next = current
                            if not previous:
                                self.head = node
                            else:
                                previous.next = node
                                self.size += 1
                            return
                        elif node.student.midterm_grade < current.student.midterm_grade:
                            node.next = current.next
                            current.next = node
                            self.size += 1
                            return
                     previous = current
                     current = current.next
            previous.next = node
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("There are no students to interview with")
        elif self.size == 1:
            print(f"Interview will be with : {self.head.student.name}")
            self.head = None
            self.size -= 1
        else:
            print(f"Interview will be with : {self.head.student.name}")
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1

    def addStudent(self):
        limit = 0
        max_attempts = 4
        input_name = ""
        input_midterm_grade = ""
        input_final_grade = ""
        input_good_attitude = ""

        while limit < max_attempts:
           input_name = input("Enter student name: ")
           if input_name.isalpha():
               break
           print("Please enter a valid name for the student.")
           limit += 1
           print(f"you have {max_attempts - limit} attempts left")


        while limit < max_attempts:
            input_midterm_grade = input(f"Enter midterm grade for {input_name}: ")
            if input_midterm_grade.isdigit() and 0 <= int(input_midterm_grade) <= 100:
                break
            print("Please enter a valid grade between 0 and 100.")
            limit += 1
            print(f"you have {max_attempts - limit} attempts left")


        while limit < max_attempts:
            input_final_grade = input(f"Enter final grade for {input_name}: ")
            if input_final_grade.isdigit() and 0 <= int(input_final_grade) <= 100:
                break
            print("Please enter a valid grade between 0 and 100.")
            limit += 1
            print(f"you have {max_attempts - limit} attempts left")


        while limit < max_attempts:
            input_good_attitude = input("Does this student have good(YES/Y) personality or not(NO/N) :").lower()
            if input_good_attitude in ['yes', 'y']:
                input_good_attitude = True
                break
            elif input_good_attitude in ['no', 'n']:
                input_good_attitude = False
                break
            print("Please enter either yes/y or no/n.")
            limit += 1
            print(f"you have {max_attempts - limit} attempts left")

        new_student = Student(input_name, input_midterm_grade, input_final_grade, input_good_attitude)
        self.enqueue(new_student)


def evaluate_expression(string):

    operators = []
    numbers = []
    pass


class LinkedList:
     def __init__(self):
         self.head = None
         self.size = 0

     def addNode(self, data):
         node = Node(data)
         node.next = self.head
         self.head = next
         self.size += 1

     def displayNodes(self):
         temp = self.head
         while temp:
             print(temp.data, end="-->")
             temp = temp.next
         print("None")


    



def main():
    linked_list = Linkedlist()
    priority_queue = PriorityQueue()
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
                sub_choice = input("Enter your choice :").lower()
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
             limit = 0
             student_choice = ""
             while student_choice != 'c' and limit < 4:
              displayMenuStudent()
              student_choice = input("Enter your choice :").lower()
              if student_choice == "a":
                  priority_queue.addStudent()
              elif student_choice == "b":
                  priority_queue.dequeue()
              elif student_choice == "c":
                  main()
              else:
                  limit += 1
                  print("Invalid choice, please enter the correct choice.")
                  print(f"You have {4 - limit} attempts left")
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




