from linkedlist import *

class Trie:
    root=None

class TrieNode:
    parent=None
    children= None
    key=None
    isEndOfWord= False

#Funcion que busca en la lista de hijos de un nodoTrie auqel cuya jey sea =letra
def buscarHijo(nodo, letra):
    if nodo:
        if nodo.children:
            recorrer= nodo.children.head
            while recorrer:
                if recorrer.key==letra:
                    return recorrer
                recorrer= recorrer.nextNode
            return None
        return None

#
def search(T, palabra):
    if T.root and palabra[0]:
        nodo= T.root

        for i in range (0, len(palabra)):
            nodo= buscarHijo(nodo, palabra[i])
            if not nodo:
                return False
        return True

#
def insert(T, palabra):
    if T.root and palabra[0]:
        nodo= T.root
        
        for i in range (0, len(palabra)):
            
            hijo= buscarHijo(nodo, palabra[i])
                #si entre los hijos del nodo no esta la letra, insertamos
            if not hijo:
                insertado= insertAux(nodo, palabra[i])
                if i==len(palabra):
                    insertado.isEndOfWord=True
                nodo= insertado

            else: nodo=hijo

#
def insertAux(padre, letra):
    insertar= TrieNode()
    insertar.key= letra
    insertar.parent= padre

    #verificamos si el nodo actual tiene hijos entre los que buscar
    if padre.children:
        recorrer= padre.children.head
        while recorrer.nextNode:
            recorrer= recorrer.nextNode
        recorrer.nextNode= insertar

    #si no tiene, creamos la lista cuyo primer TrieNode es el caracter actual de la palabra
    else:
        hijos= LinkedList()
        hijos.head= insertar
        padre.children= hijos

    return insertar


    
    





