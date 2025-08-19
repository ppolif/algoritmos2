import linkedlist 

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

    if not T.root:
        raiz= TrieNode()
        T.root= raiz

    if palabra[0]:
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
        hijos= linkedlist.LinkedList()
        hijos.head= insertar
        padre.children= hijos

    return insertar

#
def delete(T, palabra):
    encontrado= search(T, palabra)

    if encontrado:
        deleteR(T.root, palabra, 0)
        return True
    return False

#
def deleteR(nodo, palabra, long):
    if long==len(palabra):
        nodo.isEndOfWord=False
        return
    
    nodo= buscarHijo(nodo, palabra[long])
    deleteR(nodo, palabra, long+1)

    if not nodo.children and nodo.isEndOfWord==False:
        linkedlist.delete(nodo.parent.children, nodo.key)
        nodo.parent=None


#Función para buscar todas las palabras de un Trie
def listar(T):
    if T.root:
        total=[]
        palabra=[]

        listarR(T.root, palabra, total)
        return total

#
def listarR(nodo, palabra, total):
    if nodo.key:
        palabra.append(nodo.key)

    if nodo.isEndOfWord==True:
        total.append("".join(palabra))
    
    if nodo.children:
        recorrer= nodo.children.head
        while recorrer:
            listarR(recorrer, palabra.copy(), total)
            recorrer= recorrer.nextNode


#Punto 4
def patron(T, prefijo, n):
    encontrado= search(prefijo)

    if not encontrado:
        return []
    
    totalPalabras=[]
    palabra= list(prefijo)

    nodo=T.root
    for i in range (0, len(prefijo)):
        nodo= buscarHijo(nodo, prefijo[i])

    numero= n-len(prefijo)
        
    patronR(nodo, palabra, numero, 0, totalPalabras)
    return totalPalabras


#
def patronR(nodo, palabra, n, long, total):
    if long!=0:
        palabra.append(nodo.key)

    if long==n:
        if nodo.isEndOfWord:
            total.append("".join(palabra))
        return

    if nodo.children:
        recorrer= nodo.children.head
        while recorrer:
            patronR(recorrer, palabra.copy(), n, long+1, total)
            recorrer= recorrer.nextNode

#Punto 5
def mismoDoc(T1, T2):
    documento= listar(T1)

    for palabra in documento:
        if not search(T2, palabra):
            return False
    return True


#Punto 6
def invertida(T, palabra):
    nodo= T.root

    for i in range (len(palabra)-1, -1, -1):
        nodo= buscarHijo(nodo, palabra[i])
        if not nodo:
            return False
    return nodo.isEndOfWord

#
def buscarInvertido(T):
    documento= listar(T)

    for i in documento:
        if invertida(T, i):
            return True
    return False


#Punto 7
def autoCompletar(T, cadena):
    palabra= []

    nodo= T.root
    for i in range (0, len(cadena)):
        nodo= buscarHijo(nodo, cadena[i])
        if not nodo:
            return palabra

    if nodo.children:
        while linkedlist.length(nodo.children)==1 and not nodo.isEndOfWord:
            nodo= nodo.children.head
            palabra.append(nodo.key)

    return "".join(palabra)


    
    





