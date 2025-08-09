class AVLtree:
    def __init__(self, root):
        self.root= root

class AVLnode:
    def __init__(self, parent, leftnode, rightnode, key, value, bf):
        self.parent= parent
        self.leftnode= leftnode
        self.rightnode= rightnode
        self.key= key
        self.value= value
        self.bf= bf

#
def search(tree, element):
    if tree.root==None:
        return None
    
    if tree.root.value==element:
        return tree.root.key
    
    nodo = searchR(tree.root, element)
    if nodo!=None:
        return nodo.key
    return None

#
def searchR(current, element):
    if current==None:
        return None
        
    if current.value==element:
        return current
    
    izquierda= searchR(current.leftnode, element)
    if izquierda!=None:
        return izquierda
    
    derecha= searchR(current.rightnode, element)
    if derecha!=None:
        return derecha

#
def insert(tree, element, k):
    new= AVLnode()
    new.key= k
    new.value= element

    if tree.root==None:
        tree.root= new
        new.bf=0
        new.h=0
        return k
    
    nodo= insertR(tree.root, new)
    if nodo!=None:
        new.parent= nodo
        reBalance(tree)
        return k
    return None
    
#
def insertR(current, new):
    if current.key>new.key:
        if current.leftnode==None:
            current.leftnode=new
            return current
        else:
            return insertR(current.leftnode, new)
    else:
        if current.rightnode==None:
            current.rightnode=new
            return current
        else:
            return insertR(current.rightnode, new)

#    
def delete(tree, element):
    nodo= searchR(tree.root, element)

    if nodo==None:
        return None
    
    if nodo==tree.root:
        padre = AVLnode()
        padre.leftnode = tree.root
        tree.root.parent = padre
        llave = deleteR(tree.root)
        tree.root = padre.leftnode
        reBalance(tree)
        return llave
    
    llave= deleteR(nodo)
    reBalance(tree)
    return llave
       
#
def deleteR(nodo):
    #Caso 1: el nodo es una hoja
    if nodo.leftnode==None and nodo.rightnode==None:
        if nodo.parent.leftnode!=None and nodo==nodo.parent.leftnode:
            nodo.parent.leftnode=None
        elif nodo.parent.rightnode!=None:
            nodo.parent.rightnode=None

        return nodo.key
    
    #Caso 2: el nodo tiene un hijo
    if (nodo.leftnode!=None and nodo.rightnode==None) or (nodo.rightnode!=None and nodo.leftnode==None):
        if nodo.parent.leftnode!=None and nodo==nodo.parent.leftnode:
            if nodo.leftnode!=None:
                nodo.parent.leftnode= nodo.leftnode
                nodo.leftnode.parent= nodo.parent
            else:
                nodo.parent.leftnode= nodo.rightnode
                nodo.rightnode.parent= nodo.parent
        elif nodo.parent.rightnode!=None and nodo==nodo.parent.rightnode:
            if nodo.leftnode!=None:
                nodo.parent.rightnode= nodo.leftnode
                nodo.leftnode.parent= nodo.parent
            else:
                nodo.parent.rightnode= nodo.rightnode
                nodo.rightnode.parent= nodo.parent

        return nodo.key

    #Caso 3: el nodo tiene dos hijos
    if nodo.leftnode!=None and nodo.rightnode!=None:
        cambiar= menorMayores(nodo.rightnode)

        nodo.key= cambiar.key
        nodo.value= cambiar.value

        deleteR(cambiar)
        return nodo.key

#funcion que busca el menor de los mayores
def menorMayores(nodo):
    if nodo.leftnode==None:
        return nodo
    
    return menorMayores(nodo.leftnode)

#
def access(tree, k):
    if tree.root==None:
        return None
    
    if tree.root.key==k:
        return tree.root.value
    
    nodo= accessR(tree.root, k)
    if nodo!=None:
        return nodo.value
    return None
    
#
def accessR(current, k):
    if current==None:
        return None

    if current.key==k:
        return current
    
    if current.key>k:
        return accessR(current.leftnode, k)
    else:
        return accessR(current.rightnode, k)

#
def update(tree, element, k):
    if tree.root==None:
        return None
    
    if tree.root.key==k:
        tree.root.value=element

    node= updateR(tree.root, k)
    if node!=None:
        node.value= element
        return k
    return None

#
def updateR(current, k):
    if current==None:
        return None
    
    if current.key==k:
        return current
    
    if current.key>k:
        return updateR(current.leftnode, k)
    else:
        return updateR(current.rightnode, k)



#Recalcular bf
def calculateBalance(AVL):
    if AVL.root:
        calculateBalanceR(AVL.root)
    return AVL
    

def calculateBalanceR(nodo):
    if nodo:
        if nodo.leftnode and nodo.rightnode:
            nodo.h= 1+ max(nodo.leftnode.h, nodo.rightnode.h)
        elif nodo.leftnode:
            nodo.h= 1+ nodo.leftnode.h
        elif nodo.rightnode:
            nodo.h= 1+ nodo.rightnode.h
        else:
            nodo.h= 0

    #Ahora calcular el bf
    balanceFactor(nodo)

    calculateBalanceR(nodo.rightnode)
    calculateBalanceR(nodo.rightnode)

def balanceFactor(nodo):
    if nodo:
        if nodo.rightnode and nodo.rightnode:
            nodo.bf= nodo.lefttnode.h - nodo.rightnode.h
        else:
            nodo.bf= nodo.h

#
def reBalance(AVL):
    #primero recalculamos los bf
    calculateBalance(AVL)
    reBalanceR(AVL.root)
    
    return AVL

def reBalanceR(nodo):
    #esta función busca un nodo que deba balancearse y aplica el balanceo que corresponda
    if nodo:
        if nodo.bf>1:
            rotateRight(nodo)
        elif nodo.bf<-1:
            rotateLeft(nodo)
    reBalanceR(nodo.leftnode)
    reBalanceR(nodo.rightnode)


def rotateLeft(AVL, nodo):
    newRoot= nodo.rightnode
    nodo.rightnode= newRoot.leftnode

    if newRoot.leftnode:
        newRoot.leftnode.parent= nodo

    if nodo.parent==None:
        AVL.root= newRoot
    elif nodo.parent.rightnode==nodo:
        newRoot.parent.rightnode= newRoot
    else:
        nodo.parent.leftnode= newRoot
    newRoot.rightnode= nodo
    nodo.parent= newRoot

    return newRoot

def rotateRight(AVL, nodo):
    newRoot= nodo.leftnode
    nodo.leftnode= newRoot.rightnode

    if newRoot.rightnode:
        newRoot.rightnode.parent= nodo

    if nodo.parent==None:
        AVL.root= newRoot
    elif nodo.parent.rightnode==nodo:
        nodo.parent.rightnode= newRoot
    else:
        nodo.parent.leftnode= newRoot
    newRoot.rightnode=nodo
    nodo.parent= newRoot

    return newRoot