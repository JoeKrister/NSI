from liste_C import ListeC

class PileL :
    """ Pile construite avec le type list"""
    def __init__(self) :
        self.l = []

    def est_vide(self) :
        return self.l == []

    def empiler(self, v) :
        self.l.append(v)

    def depiler(self) :
        if len(self.l) > 0:
            return self.l.pop()
        else:
            return 'vide'

class PileC :
    """interface de pile"""
    def __init__(self) :
        self.p = ListeC()

    def est_vide(self) :
        return self.p.is_empty()

    def empiler(self, v) :
        self.p.push(v)

    def depiler(self) :
        return self.p.pop()
    
    def __str__(self) :
        return str(self.p)

################

class Chainon :
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
    def __str__(self) :
        if self.suivant == None :
            return f"{self.valeur} -> None"
        else :
            return f"{self.valeur} -> {str(self.suivant)}"

class File :
    """interface de file"""
    def __init__(self) :
        self.tete = None                
        self.queue = None

    def est_vide(self) :
        return self.tete is None and self.queue is None

    def enfiler(self, v) :
        if self.est_vide() :
            c = Chainon(v,None)
            self.tete = c
            self.queue = c
        else :
            c = Chainon(v,None)
            self.queue.suivant = c
            self.queue = c
    
    def defiler(self) :
        if self.est_vide():
            raise IndexError("Cannot pop from an empty queue")
        elif self.tete == self.queue:
            v = self.tete.valeur
            self.tete = None
            self.queue = None
            return v
        else :
            v = self.tete.valeur
            self.tete = self.tete.suivant
            return v

class Filev2 :
    def __init__(self) :
        self.entrees = PileC()
        self.sorties = PileC()

    def est_vide(self) :
        return self.entrees.est_vide() and self.sorties.est_vide()

    def enfiler(self, v) :
        self.entrees.empiler(v)

    def defiler(self) :
        if self.est_vide():
            raise IndexError("Unable to deqeue from an empty queue")
        if self.sorties.est_vide():
            while not(self.entrees.est_vide()) :
                self.sorties.empiler(self.entrees.depiler())
            
        return self.sorties.depiler()
