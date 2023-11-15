from liste_C import ListeC

class Chainon :
    """Chainon d'une liste chainée"""
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        
    def __str__(self):
        if self.suivant == None:
            return f"{self.valeur} -> None"
        else:
            return f"{self.valeur} -> {str(self.suivant)} "

class Pilefromlist:
    """Pile construite avec le type list"""
    def __init__(self) :
        self.p = list()

    def est_vide(self) :
        return self.p == []

    def empiler(self, v) :
        self.p.append(v)

    def depiler(self) :
        return self.p.pop()


class PileC :
    """interface de pile basé sur les listes chainées"""
    def __init__(self) :
        self.p = ListeC()
        self._taille = 0

    def est_vide(self) :
        return self.p.is_empty() == True

    def empiler(self, v) :
        self.p.push(v)
        self._taille += 1

    def depiler(self) :
        if self.est_vide():
            raise IndexError("Stack is empty")
        self._taille -= 1
        return self.p.pop()

    def vider(self):
        self.p = ListeC()
        
    def consulter(self):
        if self.est_vide():
            raise IndexError("Stack is empty")
        return self.p[0]
    
    def taille(self):
        return self._taille
    
    def __len__(self):
        return self._taille
    
    def __str__(self):
        return str(self.p)
    
            
#####


class File1 :
    """interface de file"""
    def __init__(self) :
        self.tete = None                
        self.queue = None

    def est_vide(self) :
        return self.tete is None and self.queue is None

    def enfiler(self, v) :
        if self.est_vide():
            c = Chainon(v, None)
            self.tete = c
            self.queue = c
        else :                
            c = Chainon(v, None)
            self.queue.suivant = c
            self.queue = c

    def defiler(self) :
        if self.est_vide():
            raise IndexError("Cannot pop from an empty queue")
        elif self.tete == self.queue :
            v = self.tete.valeur
            self.tete = None
            self.queue = None
        else:                
            v = self.tete.valeur
            self.tete = self.tete.suivant
            return v
        
class File :
    def __init__(self) :
        self.entrees = PileC()
        self.sorties = PileC()

    def est_vide(self) :
        return self.entrees.est_vide() and self.sorties.est_vide()

    def enfiler(self, v) :
        self.entrees.empiler(v)
        
    def defiler(self):
        if self.est_vide():
            raise IndexError("Unable to dequeue from an empty queue")
        if self.sorties.est_vide():
            while not(self.entrees.est_vide()):
                self.sorties.empiler(self.entrees.depiler())
        return self.sorties.depiler()
    

def NPI(calcul: str) -> float:
    p = PileC()
    calc = calcul.split(" ")
    for elem in calc:
        if elem == "+":
            p.empiler( p.depiler() +  p.depiler() )            
        elif elem == "-":
            v1 = p.depiler()
            v2 = p.depiler()
            p.empiler( v2 -  v1 )
        elif elem == "*":
            p.empiler( p.depiler() *  p.depiler() )
        elif elem == "/":
            v1 = p.depiler()
            v2 = p.depiler()
            p.empiler( v2 /  v1 )
        elif elem == "sqrt":
            p.empiler(p.depiler()**0.5)
        else:
            p.empiler(float(elem))
    return p.depiler()
            