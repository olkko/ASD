import turtle
class Node:
    def __init__(self, key):
        self.key = key
    def __eq__(self, other):
        return self.key == other.key
    def __hash__(self) -> int:
        return hash(self.key)
    def __str__(self):
        return f'{self.key}'

class N_mat:
    def  __init__(self, val = 0):
        self.adjMatrix = []
        self.mapVertex = []
        self.val = val

    def isEmpty(self) ->bool:
        return not bool(self.adjMatrix)
    
    def insertVertex(self, vertex):
        self.mapVertex.append(Node(vertex))
        order_n = self.order()+1
        for neighbours in self.adjMatrix:
            neighbours.append(self.val)
        self.adjMatrix.append([self.val for i in range(order_n)]) 
        
    def insertEdge(self, vertex1, vertex2):
        vertex_1 = self.getVertexIdx(vertex1)
        vertex_2 = self.getVertexIdx(vertex2)

        self.adjMatrix[vertex_1][vertex_2] = 1
        self.adjMatrix[vertex_2][vertex_1] = 1

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)

        self.adjMatrix.pop(idx)

        for neighbours in self.adjMatrix:
            neighbours.pop(idx)

        self.mapVertex.pop(idx)
        
    def deleteEdge(self, vertex1, vertex2):
        vertex1 = self.getVertexIdx(vertex1)
        vertex2 = self.getVertexIdx(vertex2)

        self.adjMatrix[vertex1][vertex2] = self.val
        self.adjMatrix[vertex2][vertex1] = self.val

    def getVertexIdx(self, vertex):
        return self.mapVertex.index(Node(vertex))
    
    def getVertex(self, vertex_idx):
        return self.mapVertex(vertex_idx)
    
    def neighbourIdx(self, vertex_idx):
        return [self.getVertexIdx(neighbour) for neighbour in self.adjMatrix[vertex_idx]]

    def neighbour(self, vertex_idx):
        return self.adjMatrix(vertex_idx)
    
    def order(self):
        l = len(self.adjMatrix)
        return l

    def edges(self):
            result = []
            for i in range(self.order()):
                for j in range(self.order()):
                    if self.adjMatrix[i][j] != self.val:
                        result.append((self.getVertex(i).key, self.getVertex(j).key))
            return result


    

class N_list:
    def  __init__(self, val = 0):
        self.adjList = {}
        self.mapVertex = []
        self.val = val

    def edges(self):
        result = []

        for node, neighbours in self.adjList.items():
            result += [(node.key, neighbour.key) for neighbour in neighbours]

        return result


    def isEmpty(self):
        return not bool(self.adjList)
    
    def insertVertex(self, vertex):
        vertex = Node(vertex)
        self.adjList[vertex] = []
        self.mapVertex.append(vertex)

    def insertEdge(self,vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if not (vertex1 in self.adjList[vertex2] and vertex2 in self.adjList[vertex1]):
            self.adjList[vertex1].append(vertex2)
            self.adjList[vertex2].append(vertex1)

    def deleteVertex(self, vertex):
        idx = None
        for i, v in enumerate(self.mapVertex):
            if v.key == vertex:
                idx = i
                break
        if idx is None:
            return

        v = self.mapVertex[idx]
        for neighbour in self.adjList[v]:
            self.adjList[neighbour].remove(v)

        del self.adjList[v]
        self.mapVertex.remove(v)

    def deleteEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        self.adjList[vertex1].remove(vertex2)
        self.adjList[vertex2].remove(vertex1)
    
    def getVertexIdx(self, vertex):
        return self.mapVertex.index(vertex)
    
    def getVertex(self, vertex_id):
        return self.mapVertex[vertex_id]
    
    def neighboursIdx(self, vertex_id):
        vertex = self.getVertex(vertex_id)
        return [self.getVertexIdx(neighbour) for neighbour in self.adjList[vertex]]
        
    def neighbours(self, vertex_idx):
        vertex = self.getVertex(vertex_idx)
        return [self.getVertex(idx) for idx in self.adjList[vertex]]
    
    def order(self):
        l = len(self.mapVertex)
        return l
    
    def size(self):
        degree_sum = sum(len(neighbours) for neighbours in self.adjList.values())

        vertex_count = len(self.mapVertex)
        if vertex_count > 0:
            return degree_sum / vertex_count
        else:
            return 0

polska=[(80,100, 'Z'), (180, 50, 'G'), (330, 80, 'N'), (420, 130, 'B'), 
        (60, 200, 'F'),(140, 200, 'P'), (200, 140, 'C'), (260, 260, 'E'),
        (340, 200, 'W'), (430, 290, 'L'), (110, 300, 'D'), (180, 330, 'O'),
        (240, 350, 'S'), (320, 320, 'T'), (300, 400, 'K'), (400, 380, 'R')]
        
        
slownik = { rej: (x, y, rej) for x, y, rej in polska}  

graf =[('Z','G'), ('Z', 'P'), ('Z', 'F'),
       ('G','Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
       ('N','G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
       ('B','N'), ('B', 'W'), ('B', 'L'), 
       ('F','Z'), ('F', 'P'), ('F', 'D'), 
       ('P','F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P','E'), ('P', 'O'), ('P', 'D'),        
       ('C','P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C','E'),        
       ('E','P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E','S'), ('E', 'O'),        
       ('W','C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W','T'), ('W', 'E'),        
       ('L','W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
       ('D','F'), ('D', 'P'), ('D', 'O'), 
       ('O','D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
       ('S','O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
       ('T','S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T','R'), ('T', 'K'),        
       ('K','S'), ('K', 'T'), ('K', 'R'), 
       ('R','K'), ('R', 'T'), ('R', 'L')]

def coords(x,y):
    y = 470 - y
    dx = -250
    dy = -235
    return x+dx, y+dy
    

def draw_circle(x,y,letter):
    x, y = coords(x, y)
    turtle.penup
    turtle.goto(x,y-20)
    turtle.pendown()
    turtle.circle(20)
    turtle.write(letter,font=("Verdana", 18, "bold"))
    turtle.penup()

def draw_line(edge):   
    x,y,_ = slownik[edge[0]]
    x, y = coords(x, y)
    turtle.penup
    turtle.goto(x, y)
    turtle.pendown()
    x,y,_ = slownik[edge[1]]
    x, y = coords(x, y)
    turtle.goto(x, y)
    turtle.penup()
    
def draw_map(edges, col=None):    
    wn = turtle.Screen()
    wn.setup(width=500,height=470, startx=10, starty=10)
    wn.title("Polska")
    
    wn.addshape("polska.gif") 
    
    myImage = turtle.Turtle()
    myImage.speed(0) 
    myImage.shape("polska.gif")
    myImage.penup()
    myImage.goto(0,0) 
    turtle.speed(0) 
    turtle.penup()
    
    
    if col == None:
        for x,y,r in polska:
            draw_circle(x, y, r)
    else:
        for k, c in col:
            x,y,_ = slownik[k]
            draw_circle(x, y, c)
                        
    for i, e in enumerate(edges):
            draw_line(e)
    turtle.hideturtle()
    
    while True:
      wn.update()     
      
      
if __name__ == "__main__":    
    vertex_list = set([edge[0] for edge in graf] + [edge[1] for edge in graf])

    adj_graph = N_list()
    mat_graph = N_mat()

    for node in vertex_list:
        adj_graph.insertVertex(node)
        mat_graph.insertVertex(node)

    for edge in graf:
        adj_graph.insertEdge(edge[0], edge[1])
        mat_graph.insertEdge(edge[0], edge[1])

    adj_graph.deleteVertex('K')
    mat_graph.deleteVertex('K')

    adj_graph.deleteEdge('W', 'E')
    mat_graph.deleteEdge('W', 'E')

    draw_map(adj_graph.edges())
    draw_map(mat_graph.edges())  
