def get_matrix(rows, col):
    matrix = []
    print(f"Enter elements for ({rows}x{col}) : ")
    for i in range(rows):
        row = []
        print(f"Enter elements of row {i + 1}")
        elements = input().split()
        for j in range(col):
            row.append(int(elements[j]))
        matrix.append(row)
    return matrix
def addMatrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for x in range(len(matrix1[0])):
         row.append(matrix1[i][x] + matrix2[i][x])

        result.append(row)
    return result


def convertMatrix_Dictionary(rows,col):
    matrix = []
    print(f"Enter the elements for {rows}x{col}")
    for i in range(rows):
        row = []
        for j in range(col):
           elements = input(f"Enter elements :")
           row.append(elements)
        matrix.append(row)
        print(matrix)







def displayMatrix(matrix):
    for row in matrix:
     print(row)

def dictionaryInput():
    dictionary = {}
    while True:
        key = input("Enter a key or enter 'q' to quit :")
        if key == "q":
            break
        else:
            value = input("Enter a value :")
        dictionary[key] = value
    inverted_dictionary = {}
    for key, value in dictionary.items():
        if value not in inverted_dictionary:
            inverted_dictionary[value] = key
        else:
           inverted_dictionary[value].append(key)
    print("original dictionary :")
    print(dictionary)
    print("Inverted dictionary :")
    print(inverted_dictionary)


def is_rotation_matrix(matrix1, matrix2):
    # Check if the dimensions of the matrices are compatible for rotation
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    # Check if the columns of matrix1 are rows in matrix2
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[j][i]:
                return False

    return True


def input_matrix():
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
    # Base case
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False


def displayMenu():
    print("1. Add matrices\n"
          + "2. Check Rotation\n"
          + "3. Invert Dictionary\n"
          + "4. Convert Matrix to Dictionary\n"
          + "5. Check Palindrome\n"
          + "6. Search for an Element & Merge Sort\n"
          + "7. Exit")

def main():
  displayMenu()
  choice = input("Enter your choice :")

  if choice == "1":
       rows = int(input("Enter number of rows :"))
       col = int(input("Enter number of col :"))
       print("Enter elements of the first matrix")
       matrix1 = get_matrix(rows, col)
       print("Enter elements of the second matrix")
       matrix2 = get_matrix(rows, col)
       print("The sum of two matrices")
       result_matrix = addMatrices(matrix1, matrix2)
       print(result_matrix)
       main()
  elif choice == "2":
        matrix1 = input_matrix()
        matrix2 = input_matrix()
        if is_rotation_matrix(matrix1, matrix2):
            print("Matrix 1 is a rotation of Matrix 2 .")
        else:
            print("Matrix 1 is not a rotation of Matrix 2.")

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
  elif choice == "7":
      exit()
  else:
      print("invalid input please try again.")
      main()




def sequenttialSearch(S,list):
    for i in range(len(list)):
        if list[i] == S:
            print(f"{S} is found at index {i}")
        return -1
def insertionSort(list):
    for x in range(len(list) - 1):
        for y in range(x + 1, len(list)):
            if list[x] > list[y]:
                temp = list[x]
                list[x] = list[y]
                list[y] = temp

    return list































