class Graph:
    def __init__(self,vno):
        self.number_of_vertices = vno
        self.adj_List = {v:[] for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            self.adj_List[u].append((v,weight))
            self.adj_List[v].append((u,weight))
        else:
            print("invalide vertices")
    
    def remove_edge(self,u,v):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            self.adj_List[u] = [(vertix,weight) for vertix, weight in self.adj_List[u] if vertix!=v ]
            self.adj_List[v] = [(vertix,weight) for vertix, weight in self.adj_List[v] if vertix!=u]
        else:
            print("invalide vertices")
    def has_edge(self,u,v):
        if 0<=u<self.number_of_vertices and 0<=v<self.number_of_vertices:
            return any(vertex == v for vertex,x  in self.adj_List[u])
        else:
            print("invalid vertices")
    
    def print_adj_list(self):
        for vertex,n in self.adj_List.items():
            print("v",  vertex, ":" ,n)
        

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()