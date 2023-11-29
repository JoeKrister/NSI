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
        return self.p is None
    
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
        if self.est_vide() :
            return float("inf")
        return self.p.valeur
        
    def __str__(self):
        if self.est_vide() :
            return ""
        return str(self.p)
    

class HanoiGame:
    def __init__(self, n:int):
        self.n = n
        self.piles = [Pile(), Pile(), Pile()]
        self.petit_a_bouger = False
        self.position_petit = 0
        for i in range(n):
            self.piles[0].empiler(n-i)
        
    def show(self): 
        print( f"""
D : {self.piles[0]}
I : {self.piles[1]}
A : {self.piles[2]}
        """)
    
    def next_move(self):
        if not(self.petit_a_bouger):
            next_position = (self.position_petit-1)%3
            self.piles[next_position].empiler(self.piles[self.position_petit].depiler())
            self.position_petit = next_position
            self.petit_a_bouger = True
        else:
            tours = [0, 1, 2]
            tours.remove(self.position_petit)
            tourA, tourB = tours
            if self.piles[tourA].consulter() < self.piles[tourB].consulter():
                self.piles[tourB].empiler(self.piles[tourA].depiler())
            elif self.piles[tourB].consulter() < self.piles[tourA].consulter():
                self.piles[tourA].empiler(self.piles[tourB].depiler())
            self.petit_a_bouger = False
                     
    def solve(self, verbose = True) -> int:
        nb_etapes = 0
        while not(self.piles[0].est_vide() and self.piles[1].est_vide()):
            self.next_move()
            nb_etapes += 1
            if verbose == True :
                self.show()
                print(f"""étape numéro: {nb_etapes}""")
        return nb_etapes

    def solve_rec(self) :
        def solve_r(n, d, i, a, nb_move) :
            if n == 1 :
                self.piles[a].empiler(self.piles[d].depiler())
                return 1
            else :
                nb_move += solve_r(n-1, d, a, i, 0)
                self.piles[a].empiler(self.piles[d].depiler())
                nb_move +=1
                nb_move += solve_r(n-1, i, d, a, 0)
                return nb_move
        return solve_r(self.n, 0, 1, 2, 0)



