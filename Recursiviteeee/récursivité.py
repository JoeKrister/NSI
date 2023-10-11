def maSuiteArithmetique(n:int) -> int:
    Un = 3 + n*7
    return Un

def maSuiteAG(n:int) -> int:
    Un = 7
    for _ in range(n):
        Un = -2*Un+5
    return Un

def maSuiteAGR(n):
    if n ==0:
        return 7
    else:
        return -2*maSuiteAGR(n-1)+5
    
def factorielle(n) :
    if type(n) != int:
        raise TypeError("n doit être un nombre entier")
    if n < 0:
        raise ValueError("n doit être un nombre positif")
    nb= 1
    for i in range(1,n+1):
        nb = nb*i
    return nb

def factorielleR(n):
    if type(n) != int:
        raise TypeError("n doit être un nombre entier")
    if n < 0:
        raise ValueError("n doit être un nombre positif")
    if n == 0 or n == 1:
        return 1
    else:
        return factorielleR(n-1)*n

def etoile(n):
    for i in range(n+1):
        print('*'*i)
        
def etoileR(n):
    if n == 1 :
        print('*')
    else:
        etoileR(n-1)
        print (n*'*')
        

def etoileRinverse(n):
    if n == 1 :
        print('*')
    else:
        print (n*'*')
        etoileRinverse(n-1)


def binomeR(n,p):
    """
    renvoie le coeff binomial (n,p) avec n>=0 et 0<=p<=n
    """
    if n < 0:
        raise ValueError("n doit être un nombre positif")
    if p > n or p<0 :
        raise ValueError("p doit être inférieur à net positif")
    if p == 0 or p == n :
        return 1
    else:
        return binomeR(n-1, p) + binomeR(n-1, p-1)
    
         
def mo(tab):
    v = 0
    c = 0
    for i in tab:
        v = v + i[0]*i[1]
        c = c + i[1]
    if c == 0:
        return None
    return v/c

    