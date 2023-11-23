class Graph1:


    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self):
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print(f"Added vertex, {self.num_vertices - 1} \n")

    def addEdge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print(f"Added edge between vertices {v1} and {v2},   \n")
        elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
            print("Invalid vertices", v1, "and", v2, "\n")
        elif v1 < 0 or v1 >= self.num_vertices:
            print("Invalid vertex ", v1, "\n")
        else:
            print("Invalid vertex ", v2, "\n")

    def displayGraph(self):
        if len(self.adj_matrix) == 0:
            print("Graph is empty")
            return
        for row in self.adj_matrix:
            print("    ".join(map(str, row)))



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def displayNodes(self):
        temp = self.head
        while temp:  # just like writing temp != None
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
