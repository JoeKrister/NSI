class Chainon:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
    def __str__(self):
        if self.suivant is None :
            return str(self.valeur)
        else :
            return f"{self.valeur} <- {self.suivant}"
        
class Pile:
    def __init__(self):
        self.p = None
        
    def est_vide(self):
        if self.p is None:
            return True
        else:
            return False
    
    def empiler(self, n:int):
        self.p = Chainon(n, self.p )
        
    def depiler(self):
        if self.p.suivant is None:
            raise AttributeError ("not possible to remove an element from an empty stack")
        v = self.p.valeur
        self.p = self.p.suivant
        return v
          
    def consulter(self):
        if p.est_vide() == True:
            return float("inf")
        else:
            return self.p.valeur
        
    def __str__(self):
        if self.p.suivant is None :
            return str(self.p.valeur)
        else :
            return f"{self.p.valeur} <- {self.p.suivant}"
    
    def _taille(self):
        nb = 0
        for i in self.p.valeur:
            nb = i
        return i
        

p = Pile()