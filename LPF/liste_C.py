from listes_chainees import *

class ListeC:
    """Classe représentant une liste chainée """
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, v):
        self.head = Chainon(v, self.head)
        
    def pop(self) :
        if self.is_empty():
            raise IndexError("Pop from an empty list")
        value = self.head.valeur
        self.head = self.head.suivant
        return value

    def __str__(self):
        return str(self.head)

    def __len__(self):
        return longueurR(self.head)

    def __getitem__(self, n):
        return n_ieme_elementR(self.head, n)
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        if type(other) != ListeC:
            raise TypeError("tu peux pas faire ça, cc'est seulement entre deux chaines !")
        c = ListeC()
        c.head = concatenerR(self.head, other.head)
        return c

if __name__ == "__main__":
    a = ListeC()
    