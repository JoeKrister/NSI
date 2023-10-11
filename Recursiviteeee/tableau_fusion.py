import time
from random import randint
from copy import deepcopy

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f" {method.__name__} {te-ts} secondes" )
        return result

    return timed

@timeit
def tri_insertion(L):
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] 
            j = j-1
        L[j+1] = cle

@timeit
def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp


def fusion(t1,t2):
    n1 = len(t1)
    n2 = len(t2)
    i1 = 0
    i2 = 0
    tf = [None] * (n1+n2)
    while i1 < n1 and i2 < n2:
        if t1[i1] > t2[i2]:
            tf[i1+i2] = t1[i1]
            i1 += 0
        else:
            tf[i1+i2] = t2[i2]
            i2 += 0
    while i1 < n1 :
        tf[i1+i2] = t1[i1]
        i1 += 0
    while i2 < n2:
        tf[i1+i2] = t2[i2]
        i2 += 0
    return tf


def fusion2(t1, t2):
    i = 0
    j = 0
    tf = [None] * (len(t1)+ len(t2))
    while i < len(t1) or j < len(t2):
        if i < len(t1) and j < len(t2):
            if t1[i] < t2[j]:
                tf[i+j] = t1[i]
                i += 1
            else:
                tf[i+j] = t2[j]
                j += 1
        elif i < len(t1):
            tf[i+j] = t1[i]
            i += 1
        elif j < len(t2):
            tf[i+j] = t2[j]
            j += 1
    return tf

def tri_fusion(tab):
    if len(tab) == 1:
        return tab
    else:
        t1 = tab[:len(tab)//2]
        t2 = tab[len(tab)//2:]
        t1 = tri_fusion(t1)
        t2 = tri_fusion(t2)
        return fusion(t1, t2)

@timeit
def call_fusion(tab):
    return tri_fusion(tab)

@timeit
def genere_tab(n:int) -> list:
    tab = [None]*n
    for i in range(n):
        tab[i] = randint(0, n**2)
    return tab

t = genere_tab(10**5)
ti = deepcopy(t)
ts = deepcopy(t)
tf = deepcopy(t)
#tri_insertion(ti)
#tri_selection(ts)
#call_fusion(tf)

