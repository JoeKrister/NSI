class Node:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

### Arbres de test
        
tree = Node(1,
            Node(2,
                 Node(3, None, None),
                 None),
            Node(4, None, None))

tree1 = Node('A',
             Node('B',
                  Node('D', None, None),
                  Node('E', None, None)),
             Node('C',
                  None,
                  Node('F',
                       None,
                       Node('G', None, None)
                       )
                  )
             )



tree2 = Node('P',
             Node('A',
                  Node('R',
                       Node('C', None, None),
                       None),
                  Node('I',
                       Node('X', None, None),
                       Node('N', None, None)
                       )
                  ),
             None)


arbre1 = Node('A',
            Node('B', None, None),
            Node('C', None, None)
            )


arbre2 = Node('A',
            Node('B', 
                Node('C',
                    Node('D', None, None),
                    Node('E', None, None)),
                Node('F', 
                    Node('G', None, None),
                    None)
                ),
            Node('H',
                Node('I',
                    None,
                    Node('J', None,None)),
                Node('K',
                    Node('L', None,None),
                    None)
                )                   
            )

abr2 = Node(3,
            Node(1,
                 None,
                 Node(2,None,None)),
            Node(5,
                 Node(4,None, None),
                 Node(6, None, None))
            )

### Fonctions arbres simple

def hauteur(t):
    if t is None:
        return 0
    else:
        return 1+max(hauteur(t.gauche),hauteur(t.droit))
    
def taille(t):
    if t is None :
        return 0
    else:
        return 1 + taille(t.gauche)+taille(t.droit)
    
def estVide(t):
    if t is None:
        return True
    else:
        return False
        
def visitePrefixe(tree) :
    print(tree.valeur, end=" ")
    if not(estVide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    if not(estVide(tree.droit)) :
        visitePrefixe(tree.droit)
        
def visiteInfixe(tree) :
    if not(estVide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    print(tree.valeur, end=" ")
    if not(estVide(tree.droit)) :
        visitePrefixe(tree.droit)

def visiteSuffixe(tree) :
    if not(estVide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    if not(estVide(tree.droit)) :
        visitePrefixe(tree.droit)
    print(tree.valeur, end=" ")

def visiteLargeur(tree):
    f = []
    f.insert(0, tree)
    while f != []:
        nd = f.pop()
        print(nd.valeur, end=" - ")
        if nd.gauche != None:
            f.insert(0, nd.gauche)
        if nd.droit != None:
            f.insert(0, nd.droit)

### Fonctions  ABR
def appartient(x, tree) :
    if tree == None :
        return False
    elif tree.valeur == x :
        return True
    elif x < tree.valeur :
        return appartient(x, tree.gauche)
    else :
        return appartient(x, tree.droit)
    
def minimum(tree):
    if estVide(tree.gauche):
        return tree.valeur
    return minimum(tree.gauche)

def maximum(tree):
    if estVide(tree.droit):
        return tree.valeur
    return maximum(tree.droit)