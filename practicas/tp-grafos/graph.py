import linkedlist
from collections import deque

class Graph:
    V= None
    E= None

#toda esta implementación asume que los elementos en la linkedlist E de aristas son listas de python

#diccionario de adyacencia, así recorro E una sola vez y asi armo las listas de adyacencia
def tablaAdj(L2):
    tabla = []
    e= L2.head

    while e:
        origen, destino = e.value

        if not tabla[origen]:
            tabla[origen] = linkedlist.LinkedList()
        linkedlist.add(tabla[origen], destino)
        e = e.nextNode

#implementacion que crearía el grafo en O(V+E) con el diccionario 
def createGraphAux(L1, T, G):
    v = L1.head

    while v:
        if v.value in T:
            G.append(T[v.value])
        else:
            G.append(linkedlist.LinkedList())
        v = v.nextNode

#implementación real que pide el practco, O(V.E)
def createGraph(L1, L2):
    grafo= []

    v= L1.head
    while v:
        adj= linkedlist.LinkedList()
        e= L2.head
        while e:
            if v.value==e.value[0]:
                vertice = e.value[1]
                linkedlist.add(adj, vertice)
            e = e.nextNode
        grafo[v.value]= adj
        v = v.nextNode

#Ejercicio 2: True si hay camino
def existPath(G, v1, v2):
    cola = deque()
    terminados = []

    cola.append(v1)

    while cola:
        vertice = cola.popleft()
        if vertice==v2:
            return True
        
        vecino = G[vertice].head
        while vecino:
            if vecino.value not in terminados and vecino.value not in cola:
                cola.append(vecino.value)
            vecino = vecino.nextNode
        terminados.append(vertice)
    return False

#ejercicio 3: grafo conexo
def isConnected(G):
    cola = deque()
    terminados = []

    cola.append(0)

    while cola:
        vertice = cola.popleft()
        
        vecino = G[vertice].head
        while vecino:
            if vecino.value not in terminados and vecino.value not in cola:
                cola.append(vecino.value)
            vecino = vecino.nextNode
        terminados.append(vertice)
    
    if len(terminados)==len(G):
        return True
    return False

#Ejercicio 4: es árbol
def DFS(G):
    cola = deque()
    terminados = []

    return DFSrecursivo(0, cola, terminados, G)

#esta implementacion devuelve True apenas encuentra un ciclo
def DFSrecursivo(v, cola, terminados, G):
    cola.append(v)
    vecino = G[v].head
    while vecino:
        if vecino.value not in cola:
            DFSrecursivo(vecino.value, cola, terminados, G)
        else:
            return True
    terminados.append(v)

def isTree(G):
    conexo= isConnected(G)
    if conexo == True:
        ciclos= DFS(G)
        if ciclos==True:
            return False
        return True
    return False

#Ejercicio 5: es completo
#implementacion para grafo no dirigido 

def isComplete(G):
    nroVertices = len(G)

    contador=0
    for i in G:
        nroAristas = linkedlist.length(G[i])
        contador= contador+nroAristas

    numeroObjetivo = nroVertices * (nroVertices-1)

    return contador == numeroObjetivo
        




            

