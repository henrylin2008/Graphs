class Graph:
    '''
    In order to implement a Graph as an Adjacency List what we need to do is define the methods our Adjacency List object will have:
    Graph() creates a new, empty graph.
    addVertex(vert) adds an instance of Vertex to the graph.
    addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
    addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
    getVertex(vertKey) finds the vertex in the graph named vertKey.
    getVertices() returns the list of all vertices in the graph.
    in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
    '''
    def __init__(self):
#         self.nodes = set() # all the vertexes in the graph -- could be done in the edges part
        self.connections = {} # all the connections start_vertex:{end_vertex:weigth}
        
#     def add_node(self, node):
#         self.nodes.add(node)
    
    def contains(self, v):
        return v in self.connections.keys()
        
    def connect(self, start, end, weight=1):
#         v = self.get_vertex(str(from_vertex)) or Vertex(str(from_vertex))
        if start not in self.connections:
            self.connections[start] = {end:weight} 
        else:
            self.connections[start][end] = weight
            
        if end not in self.connections:
            self.connections[end] = {}

    def get_nodes(self):
        return self.connections.keys()
        
#     assume there is one and only one start node (no one points to it) in the directed graph
    def get_start_vertex(self):
        cadidates = set(self.get_nodes())
        for end in self.connections.values():
            for k in end.keys():
                if k in cadidates:
                    cadidates.remove(k)
#         return set(self.get_nodes()) - set(end_nodes)
        return cadidates
        
    def paint(self):
        print(self.connections)


# In [2]:
g = Graph()
# v1 = Node(1)
g.connect(1, 2)

g.connect(1,3)
g.connect(1,4)
g.connect(2,4)
g.connect(2,5)
g.connect(3,5)
g.connect(5,4)
# In [3]:
g.paint()
{1: {2: 1, 3: 1, 4: 1}, 2: {4: 1, 5: 1}, 3: {5: 1}, 4: {}, 5: {4: 1}}
# In [4]:
g.get_nodes()
# Out[4]:
dict_keys([1, 2, 3, 4, 5])
# In [6]:
g.get_start_vertex()
# Out[6]:
{1}
# In [8]:
type(g.get_start_vertex())
# Out[8]:
set
# In [10]:
s = set([1,2,3])
# In [11]:
s
# Out[11]:
{1, 2, 3}