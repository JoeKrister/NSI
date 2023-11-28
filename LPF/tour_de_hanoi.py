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
        self._taille = 0
        
    def est_vide(self):
        if self.p is None:
            return True
        else:
            return False
    
    def empiler(self, n:int):
        self._taille += 1
        self.p = Chainon(n, self.p )
        
    def depiler(self):
        self._taille -= 1
        if self.p.valeur is None:
            raise AttributeError ("not possible to remove an element from an empty stack")
        v = self.p.valeur
        self.p = self.p.suivant
        return v
          
    def consulter(self):
        if p.est_vide() :
            return float("inf")
        else:
            return str(self.p.valeur)
        
    def __str__(self):
        if self.p is None :
            return ""
        else :
            return f"{self.p.valeur} <- {self.p.suivant}"
    

class HanoiGame:
    def __init__(self, n:int):
        p0 = Pile()
        p1 = Pile()
        p2 = Pile()
        self.n = 0
        self.piles = [p0, p1, p2]
        self.petit_a_bouger = False
        self.position_petit = self.piles[0]
        for i in range(n):
            self.piles[0].empiler(n-i)
        
    def show(self): 
        print(f'''
                D: {h.piles[0]}
                I: {h.piles[1]}
                F: {h.piles[2]}''')
    
    def next_move(self):
        if self.petit_a_bouger == False:
            positions_possibles = [0, 1, 2].remove([self.position_petit])
            h.piles[positions_possibles] = self.empiler(n)
        else :
            if self.position_petit == 2:
                self.depiler()
                h.piles[1] = self.empiler(self.position_petit)
            elif self.position_petit == 1:
                self.depiler()
                h.piles[0] = self.empiler(self.position_petit)
            elif self.position_petit == 0:
                self.depiler()
                h.piles[2] = self.empiler(self.position_petit)
            
            
            
            
    def solve(self, verbose = True) -> int:                
        if verbose == True :
            return self.p.show
        else:
            return None

h = HanoiGame(3)
p = Pile()