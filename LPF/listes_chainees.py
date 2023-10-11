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

def longueur(chaine) :
    n = 0
    chainon = chaine
    while chainon is not None :
        n+=1
        chainon = chainon.suivant
    return n

def n_ieme_elementR(chaine : Chainon , n : int):
    """renvoie la valeur du n-ième élément de la liste chaine passée en argument"""
    a = 0
    if n == 1 :
        return chaine.valeur
    else :
        for i in range(n):
            a = n_ieme_elementR(chaine.suivant,n-1)
        return a
    
def n_ieme_element(chaine : Chainon , n : int):
    a = 0
    chainon = chaine
    for i in range(chaine.suivant.valeur):
        a += chainon.valeur 
    return a


chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
print(chaine)

