def get_matrix(rows, col):  # worst case here is O(n^2)
    matrix = []  ## initialize a matrix
    print(f"Enter elements for ({rows}x{col}) : ")
    for i in range(rows):
        row = []
        print(f"Enter elements of row {i + 1}")  ## (i+1) is because (i) will start at 0, I want it to start at 1
        elements = input().split()
        for j in range(col):
            row.append(int(elements[j]))  ## using int(elements) to confirm that I will add int number in rows
        matrix.append(row)
    return matrix
def addMatrices(matrix1, matrix2): # worst case here is O(n^2)
    result = []
    for i in range(len(matrix1)):
        row = []
        for x in range(len(matrix1[0])):
         row.append(matrix1[i][x] + matrix2[i][x])

        result.append(row)
    return result


def convertMatrix_Dictionary(rows, col):  # worst case here is O(n^2)
    matrix = []
    print(f"Enter the elements for {rows}x{col}")
    for i in range(rows):  ## rows stand for how many rows user wants
        row = []
        for j in range(col):
           elements = input(f"Enter elements :")  ## Elements inside rows
           row.append(elements)
        matrix.append(row)  ## adding rows in matrix
        print(matrix)







def displayMatrix(matrix):  ##  time complexity for this function is O(n)
    for row in matrix:
     print(row)

def dictionaryInput():  ###  overall time complexity for this function is O(n)
    dictionary = {}
    while True:
        key = input("Enter a key or enter 'q' to quit :")
        if key == "q":  # this will stop taking keys and quit the loops
            break
        else:
            value = input("Enter a value :")
        dictionary[key] = value
    inverted_dictionary = {}
    for key, value in dictionary.items():  # key input will be keys in dict and value input will be values
        if value not in inverted_dictionary:
            inverted_dictionary[value] = key
        else:
           inverted_dictionary[value].append(key)
    print("original dictionary :")
    print(dictionary)
    print("Inverted dictionary :")
    print(inverted_dictionary)


def is_rotation_matrix(matrix1, matrix2):  # Overall Time complexity for this function is O(n^2)
    # Check if the dimensions of the matrices are compatible for being rotations
    if len(matrix1) != len(matrix2[0]) or len(matrix1[0]) != len(matrix2):  # just checking so it is O(1)
        return False
    for i in range(len(matrix1)):  # O(n)
        for j in range(len(matrix1[0])):  # O(n)
           if matrix1[i][j] != matrix2[j][i]:  # O(1)

               return False
    return True
# If the function has not returned False at this point, it means that the matrices are rotation matrices, so it returns True.


def input_matrix():  ### Overall Time complexity is O(n^2)
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input(f"Enter the value at position ({i + 1},{j + 1}): "))
            row.append(value)
        matrix.append(row)
    return matrix

def palindrome(s):
    # Base case When the  length of the string  becomes 0 or 1 it will stop and return True
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:  ## if first index and last index is equal
        return palindrome(s[1:-1])  ## call the function again and slice the string
    else:
        return False

def sequentialSearch(s, list):  ## time complexity is O(n)
    for i in range(len(list)):
        if list[i] == s:
          print(f"{s} is found at index {i}")
          return i
    print(f"{s} is not found in the list")
def insertionSort(list):  ## Time complexity is O(n^2)
    for x in range(len(list) - 1):
        for y in range(x + 1, len(list)):
            if list[x] > list[y]:
                temp = list[x]
                list[x] = list[y]
                list[y] = temp
    print(list)



def displayMenu():
    print("1. Add matrices\n"
          + "2. Check Rotation\n"
          + "3. Invert Dictionary\n"
          + "4. Convert Matrix to Dictionary\n"
          + "5. Check Palindrome\n"
          + "6. Search for an Element & Merge Sort\n"
          + "7. Exit")

def main():  #### Overall Time Complexity is O(n^2)
  displayMenu()
  choice = input("Enter your choice :")

  if choice == "1":  ## if user enter 1
       rows = int(input("Enter number of rows :"))
       col = int(input("Enter number of col :"))
       print("Enter elements of the first matrix")
       matrix1 = get_matrix(rows, col)  ## calling function for matrix 1
       print("Enter elements of the second matrix")
       matrix2 = get_matrix(rows, col)  ## calling function for matrix 2
       print("The sum of two matrices")
       result_matrix = addMatrices(matrix1, matrix2)  ## adding matrix1 and matrix 2
       print(result_matrix)
       main()
  elif choice == "2":
        matrix1 = input_matrix()
        matrix2 = input_matrix()
        if is_rotation_matrix(matrix1, matrix2):
            print("The two matrices are rotations of each other.")
        else:
            print("The two matrices are not rotations of each other.")

        main()
  elif choice == "3":
        dictionaryInput()
        main()
  elif choice == "4":
        rows = int(input("Enter rows :"))
        col = int(input("Enter col :"))
        convertMatrix_Dictionary(rows, col)
        main()
  elif choice == "5":
      word = input("Enter a word :")
      if palindrome(word):
          print(f"{word} is palindrome")
      else:
          print(f"{word} is not palindrome")

      main()
  elif choice == "6":
   list = [2, 4, 5, 12, 7, 1, 3]
   print(f"List : {list}")
   s = int(input("Enter an element to find :"))
   sequentialSearch(s, list)
   print("list is sorted :")
   insertionSort(list)
   main()

  elif choice == "7":
      exit()
  else:
      print("invalid input please try again.")
      main()














if __name__ == '__main__':
    main()
























