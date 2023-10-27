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

def displayMatrix(matrix):
     for row in matrix:
         print(row)


rows = int(input("Enter number of rows :"))
col = int(input("Enter number of col :"))

print("Enter elements of the first matrix")
matrix1 = get_matrix(rows, col)
print("Enter elements of the second matrix")
matrix2 = get_matrix(rows, col)
print("The sum of two matrices")
result_matrix = addMatrices(matrix1, matrix2)