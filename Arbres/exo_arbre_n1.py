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
    
def est_vide(t):
    if t is None:
        return True
    else:
        return False
        
def visitePrefixe(tree) :
    print(tree.valeur, end=" ")
    if not(est_vide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    if not(est_vide(tree.droit)) :
        visitePrefixe(tree.droit)
        
def visiteInfixe(tree) :
    if not(est_vide(tree.gauche)) :
        visiteInfixe(tree.gauche)
    print(tree.valeur, end=" ")
    if not(est_vide(tree.droit)) :
        visiteInfixe(tree.droit)

def visiteSuffixe(tree) :
    if not(est_vide(tree.gauche)) :
        visiteSuffixe(tree.gauche)
    if not(est_vide(tree.droit)) :
        visiteSuffixe(tree.droit)
    print(tree.valeur, end=" ")

def visiteLargeur(tree):
    f = []  #file de stockage des noeuds à visiter
    f.insert(0, tree) #insert racine dans file
    while f != []:  #tant que file pas vide
        nd = f.pop()   #on defile le noeud courant
        print(nd.valeur, end=" - ")
        if nd.gauche != None:  #on ajoute le FG du noeud courant à la file
            f.insert(0, nd.gauche)
        if nd.droit != None: #on ajoute le FD du noeud courant à la file
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
    if est_vide(tree.gauche):
        return tree.valeur
    return minimum(tree.gauche)

def maximum(tree):
    if est_vide(tree.droit):
        return tree.valeur
    return maximum(tree.droit)

def insertion(tree, elem):
    if est_vide(tree):
        return Node(elem, None, None)
    else:
        if elem < tree.valeur:
            return Node(tree.valeur, insertion(tree.gauche, elem), tree.droit)
        else:
            return Node(tree.valeur, tree.gauche, insertion(tree.droit, elem))
        

def tri_abr(liste) :
    def parcoursInfixe(tree, memo=[]) :        
        if not(est_vide(tree.gauche)) :
            memo = parcoursInfixe(tree.gauche, memo)
        memo.append(tree.valeur)
        if not(est_vide(tree.droit)) :
            memo = parcoursInfixe(tree.droit, memo)
        return memo
    abr = None
    for elem in liste:
        abr = insertion(abr, elem)
    return parcoursInfixe(abr)
        
        
        
l1 = [15,12,7,8,1,23,13]
abrl1 = None
for elem in l1:
    abrl1 = insertion(abrl1, elem)
    
l2 = [7,1,23,13,15,8,12]
abrl2 = None
for elem in l2:
    abrl2 = insertion(abrl2, elem)