class LinkedList:
    head= None

class Node:
    value= None
    nextNode= None

#
def add(list, element):
    newNode= Node()
    newNode.value= element

    if list.head==None:
        list.head= newNode
    else:
        newNode.nextNode= list.head
        list.head= newNode

#
def search(list, element):
    currentNode= list.head
    indice=0

    while(currentNode!=None):
        if currentNode.value==element:
            return indice
        indice=indice+1
        currentNode= currentNode.nextNode
    return None

#
def insert(list, element, position):
    long= length(list)

    if position==0:
        add(list, element)
        return 0

    if position>long or position<0:
        return None
    
    current= list.head
    indice=0

    nuevo= Node()
    nuevo.value=element
    while(indice+1<position):
        current= current.nextNode
        indice= indice+1
    nuevo.nextNode=current.nextNode
    current.nextNode= nuevo
    return position

#
def delete(list, element):
    indice= search(list, element)
    currentNode= list.head

    if indice==0:
        list.head= currentNode.nextNode
        return indice

    if indice!=None:
      for i in range (0, indice-1):
        currentNode= currentNode.nextNode

      currentNode.nextNode= currentNode.nextNode.nextNode
    
    return indice

#
def length(list):
    if list.head==None:
        return 0
    
    currentNode= list.head
    contador=0

    while(currentNode!=None):
        contador= contador+1
        currentNode=currentNode.nextNode
    
    return contador

#
def access(list, position):
    long= length(list)
    if position>=long:
        return None
    
    currentNode= list.head

    if position==0:
        return currentNode.value

    for i in range(0, position):
        currentNode= currentNode.nextNode  
    return currentNode.value

#
def update(list, element, position):
    long= length(list)
    if position>=long:
        return None
    
    currentNode= list.head

    if position==0:
        currentNode.value=element
        return position

    for i in range (0, position):
        currentNode=currentNode.nextNode

    currentNode.value= element
    return position

#
def deletePosition(list, posicion):
    if posicion<0 or posicion>=length(list):
        return None
    
    if posicion==0:
        list.head= list.head.nextNode
        return 0
    
    current= list.head

    for i in range(0, posicion-1):
        current= current.nextNode

    current.nextNode= current.nextNode.nextNode
    return posicion

#
def move(list, posOrigen, posDestino):
    if posDestino== posOrigen:
        return None
    
    valor=access(list, posOrigen)
    deletePosition(list, posOrigen)
    insert(list, valor, posDestino)

#
def reverse(list):
    if list.head==None:
        return None
    
    if list.head.nextNode==None:
        return list
    
    reversed=LinkedList()
    current= list.head
    while(current!=None):
        add(reversed, current.value)
        current= current.nextNode
    return reversed








