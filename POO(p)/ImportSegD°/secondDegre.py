from math import sqrt

def polynome(*t) :
    try :
        if len(t) ==1 :
            t = t[0]
    except TypeError:
        raise TypeError("Must pass three argument ")        
    if len(t) >3 :
        raise ValueError("length of tuple argument greater than 3")
    if len(t) <3:
        raise ValueError("length of tuple argument smaller than 3")
    a, b, c = t
    if not(isinstance(a,(int, float))
        ) or not(isinstance(b,(int, float))
        ) or not(isinstance(c,(int, float))) :
        raise TypeError("argment Error : argument must be a tuple integers or float")
    if a == 0 :
        raise ValueError("First element of tuple must not be 0")
    return t

def _discriminant(p) :
    if polynome(p) is not None :
        a,b,c = polynome(p)
        return b**2 - 4*a*c
    return None

def _nombreRacines(p) :
    if _discriminant(p) < 0 :
        return 0
    elif _discriminant(p) == 0:
        return 1
    else:
        return 2

def valeursracines(p):
    a, b, c = polynome(p)
    delta = _discriminant(p)
    if _nombreRacines(p) == 0 :
        return None
    elif _nombreRacines == 1 :
        return -b/2*a
    else :
        return (-b -sqrt(delta)) / (2*a) , (-b +sqrt(delta)) / (2*a)


def convexite(p) :
    a, b, c = polynome(p)
    if a > 0:
        return "convexe"
    else :
        return "concave"
    
def _calcule(p, x) :
    a,b,c = polynome(p)
    return a*x**2 + b*x +c

def _nombreDerive(p, x0):
    a, b, c= polynome(p)
    return 2*a*x0 + b

def tangente(p, x0) :
    nb_derive = _nombreDerive(p,x0)
    image = _calcule(p,x0)
    chaine = f"y="
    if nb_derive == 1:
        chaine += "x"
    elif nb_derive == -1:
        chaine += "-x"
    elif nb_derive != 0:
        chaine += f"{nb_derive}x"    
    if image - nb_derive*x0 >0:
        chaine += f" +{image - nb_derive*x0}"
    elif image - nb_derive*x0 <0:
        chaine += str(image - nb_derive*x0)
    return chaine

