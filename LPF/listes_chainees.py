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
        
### /!\ Fonctions /!\
        
        
def longueurR(chaine: Chainon) -> int :
    """Renvoie la longuer d'une chaine, 0 si la chaine est vide"""
    if chaine == None :
        return 0
    else :
        return 1 + longueurR(chaine.suivant)

def longueurI(chaine) :
    n = 0
    chainon = chaine
    while chainon is not None :
        n+=1
        chainon = chainon.suivant
    return n

def n_ieme_elementR(chaine : Chainon , n : int):
    """renvoie la valeur du n-ième élément de la liste chaine passée en argument"""
    if chaine is None:
        raise IndexError ('non trop grand')
    if n == 0 :
        return chaine.valeur
    else :
        return n_ieme_elementR(chaine.suivant,n-1)

def n_ieme_elementI(chaine, n) :
    if n < 0 :
        raise IndexError("Invalid index")
    ni = 0
    chainon = chaine
    while  chainon != None and ni != n :
        ni += 1
        chainon = chainon.suivant
    if chainon != None :
        return chainon.valeur
    else :
        raise IndexError("Invalid index")

def concatenerR(c1 : Chainon, c2 : Chainon):
    if c1 is None :
        return c2
    else:
        return Chainon(c1.valeur , concatenerR(c1.suivant, c2))
    
def concatenerI(c1, c2) :
    chainon = c1
    while chainon.suivant != None :
        chainon = chainon.suivant
    chainon.suivant = c2
    return c1    
    
    
def inserer(v: int, n: int, chaine: Chainon):
    if n < 0:
        raise IndexError("n doit être positif")
    if n == 0 or chaine is None :
        return Chainon(v,chaine)    
    else: 
        return Chainon(chaine.valeur, inserer(v, n-1, chaine.suivant))

def supprime(n: int, chaine: Chainon):
    if n < 0:
        raise IndexError("n doit être positif")
    if n == 0:
        return chaine.suivant
    elif chaine.suivant is None :
        raise IndexError('indice hors de porté')
    else: 
        return Chainon(chaine.valeur, supprime(n-1, chaine.suivant))


def creer_depuis_tab(tab:list):
    lc = None
    for i in range(len(tab)):
        lc = inserer(tab[i], i, lc)
    return lc

def occurrences(valeur, chaine):
    if chaine is None :
        return 0
    else:
        if chaine.valeur == valeur :
            return 1 + occurrences(valeur, chaine.suivant)
        else:
            return occurrences(valeur, chaine.suivant)

def identique(c1 : Chainon, c2 : Chainon) -> bool:
    if c1 is None and c2 is None:
        return True
    elif c1 is None or c2 is None or c1.valeur != c2.valeur :
        return False
    else:
        return identique(c1.suivant, c2.suivant)

def identiqueI(c1, c2):
    chainon1 = c1
    chainon2 = c2
    while chainon1 != None and chainon2 != None:
        if chainon1.valeur != chainon2.valeur :
            return False
        chainon1 = chainon1.suivant
        chainon2 = chainon2.suivant
    return chainon1 == chainon2
    
    
if __name__ == "__main__":    
    c1 = Chainon(45, Chainon(12, Chainon( 21,Chainon(45,Chainon(45, None)))))
    c2 = Chainon(17, Chainon(42, None))


