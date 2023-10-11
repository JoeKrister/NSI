def moyenne(liste_de_tuples : list) :
    coeff = 0
    valeurs = 0
    for elem in liste_de_tuples :
        valeurs = valeurs + elem[0] 
        coeff = coeff + elem[1]
        if coeff == 0:
            return None
        else :
            return (coeff*valeurs)/valeurs

"""CORRECTION"""

def moyennecorrection(liste_de_tuples : list):
    coeff = 0
    valeurs = 0
    for elem in liste_de_tuples :
        valeurs = valeurs + elem[0] * elem [1]
        coeff = coeff + elem[1]
    if coeff == 0:
        return None
    else :
        return valeurs/coeff


#test 2
def maximum(tab: list) -> int:
    nb_max = tab[0]
    indice_max = 0
    for i in range(0,len(tab),1):
        if tab [i] > nb_max:
            nb_max = tab[i]
            indice_max = i
    return indice_max




def mo(tab):
    v = 0
    c = 0
    for i in tab:
        v = v + i[0]*i[1]
        c = c + i[1]
    if c == 0:
        return None
    return v/c
        







