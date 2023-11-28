class Graph1:
     def __init__(self, num_vertices):
         self.num_vertices = num_vertices
         self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

     def addVertex(self):
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vertex", self.num_vertices, "\n")

     def addEdge(self, v1, v2):
         if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
             self.adj_matrix[v1][v2] = 1
             self.adj_matrix[v2][v1] = 1
             print(f"Added an edge between vertex {v1} and vertex {v2}")
         elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
             print("Invalid vertices", v1, "and", v2, "\n")
         elif v1 < 0 or v1 >= self.num_vertices:
             print(f"Invalid vertex", v1, "\n")
         elif v2 < 0 or v2 >= self.num_vertices:
             print(f"Invalid vertex", v2, "\n")


     def displayGraph(self):
         if len(self.adj_matrix) == 0:
             print("Graph is empty!")
         for row in self.adj_matrix:
          print("   ".join(map(str, row)))


     def removeEdge(self, v1, v2):
         if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            if self.adj_matrix[v1][v2] == 0 and self.adj_matrix[v2][v1] == 0:
                print(f"There is no edge between vertex {v1} and vertex {v2} to remove!")
                return
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
            print(f"Removed an edge between vertex {v1} and vertex {v2}")
         elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
             print("Invalid vertices", v1, "and", v2, "\n")
         elif v1 < 0 or v1 >= self.num_vertices:
             print(f"Invalid vertex", v1, "\n")
         elif v2 < 0 or v2 >= self.num_vertices:
             print(f"Invalid vertex", v2, "\n")

     def removeVertex(self):
         if len(self.adj_matrix) == 0:
             print("Graph is empty, there is no vertices to be removed !")
         self.num_vertices -= 1
         for row in self.adj_matrix:
             row.pop(0)
         self.adj_matrix.pop()





