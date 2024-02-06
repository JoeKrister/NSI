### Imports
import os
from graphviz import Digraph


os.environ['PATH'] += os.pathsep +"P:\\Documents\\Graphviz\\bin"


### Fonctions générales    

def hauteur(t):
    if t is None:
        return 0
    else:
        return 1+max(hauteur(t.gauche),hauteur(t.droit))


### Fonctions spécifiques

class Node :
    def __init__(self, valeur, gauche = None, droit = None, parent = None) :
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        self.parent = parent

    def est_feuille(self):
        return self.gauche is None and self.droit is None
    
    def to_string(self, shift=""):
        representation = shift + str(self.valeur)+"\n"
        if self.gauche is not None:
            representation += self.gauche.to_string(shift+"  ")
        elif self.droit is not None:
            representation += shift + "  X\n" 
        if self.droit is not None:
            representation += self.droit.to_string(shift+"  ")
        elif self.droit is not None:
            representation += shift + "  X\n"
        return representation
    
    def to_image(self, graphe, etiquette = None) :            
        noeud = str(self.valeur)
        graphe.node(noeud)
        if not(self.parent is None) :
            graphe.edge(str(self.parent.valeur), noeud, label=etiquette)
        if not(self.gauche is None) :
            self.gauche.to_image(graphe, "G")
        if not(self.droit is None) :
            self.droit.to_image(graphe, "D")
            
    def search(self, x):
        if x == self.valeur:
            return self
        elif x < self.valeur:
            if self.gauche is None:
                return None
            else:
                return self.gauche.search(x)
        else:
            if self.droit is None:
                return None
            else:
                return self.droit.search(x)
            
    def minimum(self):
        if self.gauche is None:
            return self
        return self.gauche.minimum()

    def maximum(self):
        if self.droit is None:
            return self
        return self.droit.maximum()
    
    def insert(self, x):
        if x < self.valeur:
            if self.gauche is None:
                self.gauche = Node(x, parent = self)
            else:
                self.gauche.insert(x)
        else:
            if self.droit is None:
                self.droit = Node(x, parent = self)
            else:
                self.droit.insert(x)
            
            
    
    


class ABR :
    def __init__ (self, racine = None) :
        self.racine = racine

    def est_vide(self):
        return self.racine is None
    
    def hauteur(self):
        return hauteur(self.racine)
    
    def __str__(self):
        return self.racine.to_string()
    
    def to_image(self, title="arbre") :
        if not(isinstance(title, str)) :
            title = 'arbre'
        graphe=Digraph()
        self.racine.to_image(graphe)
        graphe.render(title, view = True, format='png')

    def search(self, x):
        if self.racine is None:
            return None    
        return self.racine.search(x)
    
    def minimum(self):
        if self.racine is None:
            return self
        return self.racine.minimum()

    def maximum(self):
        if self.racine is None:
            return self
        return self.racine.maximum()
    
    def successeur(self,x):            
        n = self.search(x)
        if n is None :
            return None
        else :
            if not(n.droit is None) :
                return n.droit.minimum()
            else :
                ancetre = n.parent
                while not(ancetre  is None) and (n == ancetre.droit) :
                    n = ancetre
                    ancetre = n.parent
                return ancetre

    def predecesseur(self,x):            
        n = self.search(x)
        if n is None :
            return None
        else :
            if not(n.gauche is None) :
                return n.gauche.maximum()
            else :
                ancetre = n.parent
                while not(ancetre  is None) and (n == ancetre.gauche) :
                    n = ancetre
                    ancetre = n.parent
                return ancetre
            
    def insert(self, x):
        if self.racine is None:
            self.racine = Node(x)
        else:
            self.racine.insert(x)
    
    
    
if __name__ == "__main__" :
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2, n1, n2)
    n1.parent = n3
    n2.parent = n3
    n4 = Node(10)
    n5 = Node( 7)
    n6 = Node(9,n5, n4)
    n4.parent=n6
    n5.parent = n6
    n7 = Node(5, n3, n6)
    n3.parent = n7
    n6. parent = n7
    n8 = Node(4)
    n2.droit = n8
    n8.parent = n2

    tree = ABR(n7)
    
    tree = ABR()
    for elem in [15,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,5,15,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,5,15,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,515,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,5,15,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,5,15,12,7,8,1,23,13,82,46,54,3541,0,987,65465,65465132,5465654321,117,100000,177,117,177,171,177,117,177,177,117,117,177,171,71,5] :
        tree.insert(elem)
    tree.to_image()
