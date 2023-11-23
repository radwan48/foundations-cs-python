# def sortList(l):
#     for i in range(len(l)):
#         for x in range(i + 1):
#             if l[x] > l[i]:
#                 temp = l[x]
#                 l[x] = l[i]
#                 l[i] = temp
#     return l
#
#
#
# def palindrome(s):
#     i = len(s) - 1
#     if len(s) <= 1:
#         return True
#     elif s[0] == s[i]:
#         return palindrome(s[1:i])
#     else:
#         return False
#
#
#
# def matrixToDictionary(m):
#     dic = {}
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             dic[(i, j)] = m[i][j]
#     return dic
#
#
#
#
#
#
#
# def getMatrix(rows, col):
#     matrix = []
#     for i in range(rows):
#         row = []
#         for j in range(col):
#             element = input(f"enter elements for rows {i + 1} column {j + 1} :")
#             row.append(int(element))
#         matrix.append(row)
#     return matrix
#
#
# # rows = int(input("Enter number of rows :"))
# # col = int(input("Enter number of columns :"))
# # get_matrix1 = getMatrix(rows, col)
# #
# # rowss = int(input("Enter number of rows :"))
# # cols = int(input("Enter number of columns :"))
# # get_matrix2 = getMatrix(rowss, cols)
#
#
#
#
# def addMatrices(matrix1, matrix2):
#     result = []
#     for i in range(len(matrix1)):
#        row = []
#        for j in range(len(matrix1[0])):
#            row.append(matrix1[i][j] + matrix2[i][j])
#            result.append(row)
#     return result
#
#
#
# # result = addMatrices(get_matrix1, get_matrix2)
# # print(result)
# #
#
#
#
# def insertionSort(l):
#   # O(N^2), N being the length of the list
#   for i in range(1, len(l)):  # N
#     # we start at 1 since we need to compare with the index before it
#     current = l[i]
#     # current to not lose the value at index i
#     j = i - 1
#     # j is the element before that we want to compare with
#     while j >= 0 and current < l[j]:  # N
#       # While we did not reach index 0 and our current pointer has a value smaller than the element before we keep looping
#       l[j + 1] = l[j]
#       # why j + 1 instead of i?
#       # because j is changing and i is not!
#       j -= 1
#     l[j + 1] = current
#   return l
#
# def reverse(n):
#     if n // 10 == 0:
#         return True
#     return (n % 10) * 10**(len(str(n)) - 1) + reverse(n // 10)
#
#
# def binarySearch(k, list):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (high + low) // 2
#         if k == list[mid]:
#             return mid
#         elif k > list[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
#
# # list = [1, 4, 5, 7, 9]
# # print(binarySearch(5, list))
#
#
#
#
#
# class Node:
#
#     def __init__(self, info):
#          self.info = info
#          self.next = None
# class Queue:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#
#     def getSize(self):
#         current = self.head
#         size = 0
#         while current is not None:
#             size += 1
#             current = current.next
#         print("the size of the ll is", size)
#         return size
#
#     def displayNodes(self):
#         # Prints the info of each node in the LL
#         current = self.head
#         while current is not None:
#             print(current.info, end=" ")
#             current = current.next
#         print()
#
#     def isEmpty(self):
#       return self.head is None
#
#
#
#     def enqueue(self, value):
#         node = Node(value)
#         if self.isEmpty():
#          self.head = node
#          self.tail = node
#          self.size += 1
#         else:
#             self.tail.next = node
#             self.tail = node
#             self.size += 1
#         print("We successfully added :", node.info)
#
#
#     def dequeue(self):
#         if self.isEmpty():
#             print("your Queue is Empty! Enqueue first.")
#         elif self.size == 1:
#             print("We are removing :", self.head.info)
#             self.head = None
#             self.tail = None
#             self.size -= 1
#         else:
#             current = self.head
#             self.head = self.head.next
#             current.next = None
#             self.size -= 1
#
#
# def main():
#  link = Queue()
#
#  node1 = Node(20)
#  node2 = Node(18)
#  node3 = Node(15)
#  node4 = Node(10)
#
#
#  link.head = node1
#  node1.next = node2
#  node2.next = node3
#  node3.next = node4
#  link.displayNodes()
#
#
#
#
# class Node:
#     def __init__(self, info):
#             self.info = info
#             self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def isEmpty(self):
#         return  self.size == None
#
#
#     def push

































