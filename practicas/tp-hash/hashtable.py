class Dictionary:
    def __init__(self):
        self.D = [[] for _ in range(15)]


#función hash método de la división
def hashFunction(key):
    return key % 15

#
def insert(D, key):
    posicion= hashFunction(D, key)
    D[posicion].append(key)

#
def search(D, key):
    posicion= hashFunction(key)

    for i in D[posicion]:
        if D[posicion][i]==key:
            return key
        return None
    
#
def searchAux(D, key):
    posicion= hashFunction(key)

    for i in D[posicion]:
        if D[posicion][i]==key:
            return i
        return None
    
#
def delete(D, key):
    posicion= hashFunction(D, key)
    indice= searchAux(D, key)
    if indice:
        D[posicion][indice]=None
    return D


########## Ejercicio 11 ###########

class DoubleList:
    head= None

class DoubleNode:
    value= None
    next= None
    prev= None

def insertDouble(L, element):
    nodo= DoubleNode()
    nodo.value= element
    nodo.next= L.head
    L.head= nodo
    return L

def deleteDouble(L, element):
    
