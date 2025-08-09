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
        return k
    
    nodo= insertR(tree.root, new)
    if nodo!=None:
        new.parent= nodo
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
        padre = BinaryTreeNode()
        padre.leftnode = tree.root
        tree.root.parent = padre
        llave = deleteR(tree.root)
        tree.root = padre.leftnode
        return llave
    
    return deleteR(nodo)
       
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