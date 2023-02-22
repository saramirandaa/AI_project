#Importacion del grafo desde csv
import csv
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
plt.title("Graph Image")
image = mpimg.imread("graph.png")
plt.imshow(image)
plt.show()

matrix = []
nodes = []

#los valores de la matriz se pasan a una lista de listas
with open('matrix.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cStr = ",".join(row)
        cStr2 = cStr.split(',')
        A = [int(x) for x in cStr2]
        matrix.append(A)
        del cStr2, A
#los valores de los nodos se pasan a un string
with open('nodes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader: 
        nodes.append(row)  
#se convierte de string a lista
nodesStr = "".join(nodes[0])
nodes = nodesStr.split(',')


#clase grafo en donde se pasa como parametros los nodos y la matriz
class graph:
    #constructor que nos permite tener los parametros 
    def __init__(self, nodes, graph_matrix):
        self.nodes = nodes
        self.graph = graph_matrix
        
    #metodo que nos devolverá los nodos creados 
    def get_Tuples(self):
        formed_nodes = []
        self.weights = []
        self.nodes_and_weigths = []
        #un for con la longitud de la longitud en y de nuestra matriz
        for y in range(len(self.graph)):
            for x in range(len(self.graph[0])):
                if self.graph[y][x] != 0:
                    #Aqui se forman las conexiones de cada nodo
                    formed_nodes.append([self.nodes[y], self.nodes[x]])
                    self.weights.append(self.graph[y][x])
                    #Aquí se hace una lista con los nodos y su peso
                    self.nodes_and_weigths.append([formed_nodes[y], self.graph[y][x]])   
        return formed_nodes
    
    #metodo que regresa solo los pesos
    def get_weights(self):
        self.get_Tuples()
        return self.weights
    
    #metodo que regresa una lista de los nodos y sus respectivos pesos
    def get_tuples_weights(self):
        self.get_Tuples()
        return self.nodes_and_weigths

class graph_Search_methods():
    def __init__(self, nodes, tree):
        self.__nodes = nodes
        self.__tree = tree
    def Depth_Search(self):
        print("===== DEPTH SEARCH =====")
        start_node = input("Enter the start node: ")
        # Verificamos que el nodo inicial exista en el grafo
        if start_node not in self.nodes:
            print("\nERROR . . . The start node does not exist in the graph")
            return
        
        # Inicializamos la lista de visitados y la pila del DFS
        visited = []
        stack = [start_node]
 
        # Mientras hayan nodos por visitar
        while stack:
            # Sacamos el último nodo agregado a la pila
            node = stack.pop()
            # Si el nodo no ha sido visitado, lo visitamos y agregamos a su vecinos a la pila
            if node not in visited:
                visited.append(node)
                for neighbor in self.__tree.get_Tuples():
                    if node == neighbor[0] and neighbor[1] not in visited:
                        stack.append(neighbor[1])
        return visited
    
    def Depth_Limited(self):
        pass
    def Breadth_search(self):
        pass
    def Dijkstra_search(self):
        print("===== DIJKSTRA SEARCH =====")
        start = input("Enter the start node: ") # Nodo inicial
        destiny = input("Enter the destiny node: ") # Nodo final

        #  Verificamos que el nodo inicial y el nodo final existan en el grafo
        if start not in self.nodes:
            print("\nERROR . . . The start node does not exist in the graph")
            return
        if destiny not in self.nodes:
            print("\nERROR . . . The destiny node does not exist in the graph")
            return
        # Inicializamos las variables necesarias para el algoritmo
        nodes = set(self.nodes)
        visited = {start: 0}
        path = {}
        unvisited = {node: float("inf") for node in nodes}
        unvisited[start] = 0
        # Mientras haya nodos por visitar
        while unvisited:
            # Seleccionamos el nodo con la menor distancia
            current_node = min(unvisited, key=unvisited.get)
            # Marcamos el nodo como visitado
            visited[current_node] = unvisited[current_node]
            unvisited.pop(current_node)
            # Calculamos la distancia de los nodos vecinos al nodo actual
            for neighbor in self.nodes:
                if self.graph[self.nodes.index(current_node)][self.nodes.index(neighbor)] != 0:
                    distance = visited[current_node] + self.graph[self.nodes.index(current_node)][self.nodes.index(neighbor)]
                    if neighbor not in visited and distance < unvisited[neighbor]:
                        unvisited[neighbor] = distance
                        path[neighbor] = current_node
            # Si el nodo actual es el nodo final, terminamos el algoritmo
            if current_node == destiny:
                break
        #Si no hay un camino
        if destiny not in path:
            print("\nERROR . . . There is no path between", start, "and", destiny)
        else:
            #Imprimir el camino más corto entre el nodo inicial y el nodo final, Además de los pesos entre cada nodo
            print("\nThe shortest path between", start, "and", destiny, "is:")
            print(destiny, end="")
            current_node = destiny
            while current_node != start:
                print(" <--- ", path[current_node], end="")
                current_node = path[current_node]
            print("\n\n ---> The total weight is:", visited[destiny])

    def Binary_Search(self):
        pass

def Search_Menu():
    print("\n\tWelcome to the Graph Search program")
    print("Choose the type of search you would like to implement in your graph:\n")
    print("1. Breadth Search\n2. Depth Search\n3. Depth Limited Search\n4. Dijkstra Search\n5. Binary Search")
    
def main():
    g = graph(nodes, matrix)
    Search_Menu()
    option = int(input("Enter the number of the search you want to implement: "))
    if option == 1:
        print("Breadth Search")
    elif option == 2:
        print("Depth Search")
        graph_Search_methods.Depth_Search(g)
    elif option == 3:
        print("Depth Limited Search")
    elif option == 4:
        print("Dijkstra Search")
        graph_Search_methods.Dijkstra_search(g)

    elif option == 5:
        print("Binary Search")
    else:
        print("Invalid option")

    
main()