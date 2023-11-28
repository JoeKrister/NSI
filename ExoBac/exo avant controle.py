def recherche(a, L:list):
    nb_occ = 0
    for i in L:
        if i == a:
            nb_occ += 1
    return nb_occ

def recherche2(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    else:
        return -1

def maxliste(tab:list):
    a = 0
    for elem in tab:
        if elem > a :
            a = elem
    return a

def fusion(tab1, tab2):
    n1 = 0
    n2 = 0
    l1 = len(tab1)
    l2 = len(tab2)
    tab[] = 0
    while l1 > n1 and l2 > n2:
        if tab1[n1] > tab2[n2]:
            tab.append(tab2[i2])
            i2 = i2 + 1
        else:
            tab.append(tab1[i1])
            i1 = i1 + 1
    while l1 > 0:
        if tab1[n1] > tab2[n2]:
            tab.append(tab2[i2])
            i2 = i2 + 1
    while n1 > 0:
        if tab1[n1] > tab2[n2]:
            tab.append(tab2[i2])
            i2 = i2 + 1