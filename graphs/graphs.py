class Graph:
    def __init__(self,vno):
        self.number_of_vertices = vno
        self.adjacent_matrix = [[0]*vno for i in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            self.adjacent_matrix[u][v] = weight
            self.adjacent_matrix[v][u] = weight
        else:
            print("invalid edge")
    def remove_edge(self,u,v):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            self.adjacent_matrix[u][v] = 0
            self.adjacent_matrix[v][u] = 0
        else:
            print("invalid edge")
    def has_edge(self,u,v):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            return self.adjacent_matrix[u][v] != 0
    def print_adj_matrix(self):
        for row_list in self.adjacent_matrix:
            print(" ".join(map(str,row_list)))
    
g=Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(3,0)

g.print_adj_matrix()
