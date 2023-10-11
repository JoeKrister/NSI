import random
from dateHash import *

def genere_groupe() -> list:
    return  [random.randint(1,365) for _ in range(23)]


def contient_doublon( t : list) -> bool:
    s = cree()
    for data in t:
        if contient(data, s) :
            return True
        else:
            ajoute(data, s)
    return False
        
        
def teste_hypothese(n : int) -> float:
    nb_doublon = 0
    for _ in range(n) :
        t = genere_groupe()
        if contient_doublon(t) :
            nb_doublon += 1
    return nb_doublon/n*100
    
    
#if __name__ == "__main__" :
 #   t = genere_groupe()
 #   print(t)
 #   print(contient_doublon(t))