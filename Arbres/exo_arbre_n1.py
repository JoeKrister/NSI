class Node:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

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
        
            