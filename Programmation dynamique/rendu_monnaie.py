def rendu_monnaie_rec(P : list, s : int) -> int:
    """ renvoie le nombre minimal de pièces pour rendre la somme s
    en utilisant le jeu de pièces P"""

    if s==0:
        return 0
    else:
        mini = float('inf') # On fixe le nombre de piècé à l'infini
    for i in range(len(P)):
        if P[i] <= s:
            nb = 1 + rendu_monnaie_rec(P, s-P[i])
            if nb < mini:
                mini = nb
    return mini

# import time
# P = (2, 5, 10, 100)
# s = 11
# while True:
#     start = time.perf_counter()
#     print(f"rendu_monnaie_rec(P, {s}) = {rendu_monnaie_rec(P,s)}", end="")
#     end = time.perf_counter()
#     print(f" Temps : {end - start}")
#     s += 1
    
def renduMonnaie1(P : list, s : int) -> int | None :
    nb = [0]+[None] * (s)
    for n in range(1, s+1) :
        for p in P :
            if p <= n and nb[n-p] is not None :
                if nb[n] is None or nb[n] > 1 + nb[n-p]:
                    nb[n] = 1 + nb[n-p]                                         
    return nb[s]


def renduMonnaie1_Desc(P : list, s : int) -> int | None :
    
    memo = [0]+[None] * (s)
    
    def compute(s, memo):
        for p in P :
            if memo[s] is not None:
                if p <= s and memo[s-p] is not None :
                    memo[s] = 1 + compute(s-p, memo)
    return compute(s, memo[s])

def fiboDesc(n : int) -> int :

    memo = [0, 1]+[None]*(n-1)

    def compute(n, memo) :
        if memo[n] is  None :
            memo[n] = compute(n-1, memo) + compute(n-2, memo)
        return memo[n]

    return compute(n, memo)
