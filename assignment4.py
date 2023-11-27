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

def displayMenuGraph():
    print("a. Add vertex\n"
          + "b. Add edge\n"
          + "c. Remove vertex\n"
          + "d. Remove edge\n"
          + "e. Display vertices with a degree of X or more.\n"
          + "f. Return to main menu")






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addNode(self, data):  # worst case is O(1)
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

    def displayNodes(self):   # Worst case O(n)
        if self.size == 0:  # if linked list is empty
            print("There is no Nodes to show, please add nodes first to display .")  #O(1)
            return
        temp = self.head
        while temp:  # traversing into linked list # O(n)
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")


    def searchAndRemove(self, value):  #Worst case is O(n)
        if self.size == 0:  # if its empty
            print("Cant search and delete the Node since no Nodes yet .")
            return
        current = self.head
        previous = None
        while current:
            if current.data == value:  # if  value found
                if current == self.head:  # if the value was the first head node
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

def inputNumeric(numeric_value):  # worst case is O(1)

    try:  # we try if number contains decimal point, or it is a negative number or both
        if "." in numeric_value or (numeric_value[0] == '-' and "." in numeric_value[1:]):
             numeric_value = float(numeric_value)  #casting it to float
        elif numeric_value[0] == '-':
             numeric_value = int(numeric_value)  # casting it to integer
        else:
          numeric_value = int(numeric_value)    # casting it to integer
    except ValueError:  # handle ValueError
            print("Please enter a valid numeric value.")

def isPalindrome(s):  #Worst case is O(n)
    if len(s) == 0:  #if input was empty by user
        print("Empty string, please type a string")
        return
    s = s.lower()  #changing all the letter to lower case to make sure we can compare between characters
    list1 = list(s)  #change string to a list
    list2 = []
    original_list = list1.copy()  # made a copy of list of the string
    while list1:                    # while list is not empty
        list2.append(list1.pop())   #  we append the last element
    if original_list == list2:    # then compare it with the original list
        print(f"{s} is palindrome")  # if list2 is the same as the input, so it is palindrome
    else:
        print(f"{s} is not palindrome")  # if list2 is not the same as the input, so it is palindrome


class Student:  # worst case is O(1)
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade  #cheracteristics for the student
        self.final_grade = final_grade
        self.good_attitude = good_attitude
class Node1:  # worst case is O(1)
    def __init__(self, student):
       self.student = student
       self.next = None

class PriorityQueue:  # worst case is O(1)
    def __init__(self):
      self.head = None
      self.size = 0

    def enqueue(self, student):  # worst case is O(n)
        node = Node1(student)
        if self.size == 0:  # if the queue was empty
            self.head = node  # new student will be at head node
            self.size += 1   # adding size by one
        else:
            current = self.head  # we will use current as self.head for traversing in the queue
            previous = None  # we will use previous as the previous node for the current
            while current:  # while current is not None
                 if node.student.good_attitude and not current.student.good_attitude:  # we need to check if new node have good attitude and the current node have bad attitude
                     node.next = current
                     if not previous:  # if there is no previous priority
                         self.head = node  # we added to the head
                     else:   # if there is previous priority
                         previous.next = node  # we add it next to previous
                     self.size += 1
                     return
                 elif current.student.good_attitude and not node.student.good_attitude:  # we need to check if new node have bad attitude and the current node have good attitude
                     node.next = current.next  #Adding new node after current node
                     current.next = node
                     self.size += 1
                     return
                 else:
                     if (node.student.final_grade > current.student.final_grade or  #we are checking if final grade of the new node is greater has priority fist and
                      (node.student.final_grade == current.student.final_grade       # if final grade was equal we check the midterm grade of the new node and if its higher it has the priority
                      and node.student.midterm_grade > current.student.midterm_grade)):
                        node.next = current  # if the condition was true we link the new node to current
                        if not previous:  # if there is no previous priority
                            self.head = node  # we add it to the head
                        else:  # if there is previous priority
                            previous.next = node  # we add it next to previous
                        self.size += 1
                        return
                     elif node.student.final_grade < current.student.final_grade or (    #we are checking if final grade of the current node is greater has priority fist and
                        node.student.final_grade == current.student.final_grade           # if final grade was equal we check the midterm grade of the current node and if its higher it has the priority
                        and node.student.midterm_grade < current.student.midterm_grade):
                         node.next = current.next  # we link the new node after current
                         current.next = node  #then we add new node next to current
                         self.size += 1
                         return
                     previous = current  # we set previous to current
                     current = current.next  # we set current to new current which is next to it
            previous.next = node  # if current is none we set new node next to previous
            self.size += 1

    def dequeue(self):  # worst case is O(1)
        if self.size == 0:  # we check if queue is empty
            print("There are no students to interview with")
        elif self.size == 1:  #if queue have single element(student)
            print(f"Interview will be with : {self.head.student.name}")
            self.head = None
            self.size -= 1
        else:  #if queue have more than single element(student)
            print(f"Interview will be with : {self.head.student.name}")
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1

    def addStudent(self):  # not sure if worst case is O(n) or O(log n)
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


def evaluateExpression(string):  #O(string)
    operators = []  #list stack for operators "+-*/"
    numbers = []    # list stack for numbers "+-*/"
    def applyOperator():
        operator = operators.pop()
        right_number = numbers.pop()
        left_number = numbers.pop()
        if operator == "+":
            numbers.append(left_number + right_number)
        elif operator == "-":
            numbers.append(left_number - right_number)
        elif operator == "*":
            numbers.append(left_number * right_number)
        elif operator == "/":
            numbers.append(left_number // right_number)

    for char in string:
        if str(char).isdigit():
            numbers.append(int(char))
        elif char in "+-*/":
            while operators and operators[-1] in "+-*/" and char in "+-*/":
                applyOperator()
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
          while operators[-1] != '(':
             applyOperator()
          operators.pop()

    while operators:
        applyOperator()
    return numbers[0]

def infixExpression():  # O(s)
    try:
      user_input = input("Enter an infix expression: ")
      result = evaluateExpression(user_input)
      print("Result:", result)
    except ValueError:
        print("Value error, please check your expression")
    except IndexError:
        print("Index error, please check your expression")



class LinkedList:
     def __init__(self):
         self.head = None
         self.size = 0

     def addNode(self, data):  #O(1) worst case
         node = Node(data)
         node.next = self.head
         self.head = node
         self.size += 1

     def removeNode(self, data):  # worst case is O(n)
         if self.size == 0:
             return
         elif self.size == 1:
             self.head = None
             self.size -= 1
         else:
             current = self.head
             previous = None
             while current and current.data != data:
                 previous = current
                 current = current.next
             if current:
                 if previous:
                     previous.next = current.next
                 else:
                     self.head = current.next
                 self.size -= 1

     def getElements(self):
         elements = []  # we use this function to get the data form the linked list of the vertices
         current = self.head
         while current:
             elements.append(current.data)
             current = current.next
         return elements


     def displayNodes(self):
         temp = self.head
         while temp:
             print(temp.data, end="-->")
             temp = temp.next
         print("None")

class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self):  # O(1)
        vertex = input("Enter a vertex : ")
        if vertex.isdigit():
          vertex = int(vertex)
          if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()
          else:
           print(f"vertex {vertex} already exists")


    def addEdge(self):  # worst case is O(n)
        if not self.adj_list:
            print("Graph is empty, add vertices first")
            return
        vertex1 = input("enter the edge you want to add of the first vertex: ")
        if not vertex1.isdigit():
            print("Please enter valid vertex")
            return
        vertex2 = input("enter the edge you want to add of the second vertex: ")
        if not vertex2.isdigit():
            print("Please enter valid vertex")
            return
        vertex1 = int(vertex1)
        vertex2 = int(vertex2)
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].addNode(vertex2)
            self.adj_list[vertex2].addNode(vertex1)
            print(f"Edge added between vertex: {vertex1} and vertex: {vertex2}")
        elif vertex1 in self.adj_list and vertex2 not in self.adj_list:
            print("Vertex", vertex2, "does not exist to add the edge!\n")
        elif vertex1 not in self.adj_list and vertex2 not in self.adj_list:
            print("Vertex", vertex1, "and Vertex", vertex2, " not exist to add the edge!\n")
        else:
            print("Vertex", vertex1, "does not exist to add the edge!\n")

    def displayVertices(self):  # worst case is O(v)
        if not self.adj_list:
            print("Graph is empty, there is nothing to be displayed.")
            return
        input_vertex = input("Enter vertex you which to display and display all vertices that are larger than vertex :")
        if input_vertex.isdigit():
            input_vertex = int(input_vertex)
            if input_vertex not in self.adj_list:
                print(f"Vertex: {input_vertex} is not found in graph")
                return
            for vertex in self.adj_list:
                if vertex >= input_vertex:
                    print("vertex:", str(vertex) + ",", end=" ")
            print()
        else:
            print("Please enter the number of the vertex")

    def removeVertex(self):  ##worst case is O(1)
        if not self.adj_list:
            print("Graph is empty, there is nothing to remove.")
        vertex = input("Enter a vertex that you wish to remove :")
        if not vertex.isdigit():
            print("Please enter valid vertex.")
        vertex = int(vertex)
        if vertex in self.adj_list:
          del self.adj_list[vertex]
          print(f"Vertex: {vertex} has been removed")
        else:
            print("Vertex is not found to remove.")

    def removeEdge(self):  # worst case O(1)
        if not self.adj_list:
            print("Graph is empty, there is nothing to remove.")
            return
        vertex1 = input("Enter the first vertex :")
        if not vertex1.isdigit():
            print("Please enter a valid vertex number")
            return
        vertex1 = int(vertex1)
        vertex2 = input("Enter the second vertex :")
        if not vertex2.isdigit():
            print("Please enter a valid vertex number")
        vertex2 = int(vertex2)
        edge_found = False
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 in self.adj_list[vertex1].getElements() and vertex1 in self.adj_list[vertex2].getElements():
                 self.adj_list[vertex1].removeNode(vertex2)
                 self.adj_list[vertex2].removeNode(vertex1)
                 print(f"Edge removed between vertex: {vertex1} and vertex: {vertex2}")
            else:
                print(f"There is no edge between vertex: {vertex1} and vertex: {vertex2}")
        elif vertex1 in self.adj_list and vertex2 not in self.adj_list:
            print(f"Cant remove edge, since vertex {vertex2} not found")
        elif vertex2 in self.adj_list and vertex1 not in self.adj_list:
            print(f"Cant remove edge, since vertex {vertex1} not found")
        else:
            print(f"There is no edge between vertex :{vertex1} and vertex :{vertex2}")






def main():
    linked_list = Linkedlist()
    priority_queue = PriorityQueue()
    graph = Graph()
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
            infixExpression()
        elif choice == "5":
            limit = 0
            graph_choice = ""
            while graph_choice != 'f' and limit < 4:
                displayMenuGraph()
                graph_choice = input("Enter your choice :").lower()
                if graph_choice == "a":
                    graph.addVertex()
                elif graph_choice == "b":
                    graph.addEdge()
                elif graph_choice == "c":
                    graph.removeVertex()
                elif graph_choice == "d":
                    graph.removeEdge()
                elif graph_choice == "e":
                    graph.displayVertices()
                elif graph_choice == "f":
                    main()
                else:
                    limit += 1
                    print("Invalid choice, please enter the correct choice.")
                    print(f"You have {4 - limit} attempts left")
        elif choice == "6":
            exit()
        else:
            limit += 1
            print("Invalid choice, please enter the correct choice.")
            print(f"You have {4 - limit} attempts left")




def name():  # worst case is O(1)
 name_input = input("Enter your name :")
 if not name_input.isalpha():
     print("Please enter your real name")
     name()
 else:
     print(f"Hello {name_input}")
     main()

name()



