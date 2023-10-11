from personnage import Personnage

def fight(P1, P2) :
    nbr = 0
    while P1.pv > 0 and P2.pv > 0 :
        nbr += 1
        print(f'\n Round {nbr}')
        tour_results = tour(P1, P2)
        P1.pv, P2.pv, P1.pex, P2.pex = tour_results[0], tour_results[1], tour_results[2], tour_results[3]
    if P1.pv > 0:
        print(f"Le vainqueur est {P1.nom}, il lui reste {P1.pv} PV. Il gagne {P2.pex} points d'exp.")
        P1.pex += P2.pex
    else:
        print(f"Le vainqueur est {P2.nom}, il lui reste {P2.pv} PV. Il gagne {P1.pex} points d'exp.")
        P2.pex += P1.pex

def ordre_tour(P1, P2):
    if P1.initiative() > P2.initiative():
        P1.pex += 2
        return [P1, P2]
    elif P2.initiative() > P1.initiative():
        P2.pex += 2
        return [P2, P1]
    else:
        return []

def tour(P1, P2):
    ordre = ordre_tour(P1, P2)
    if ordre == []:
        print("Personne n'a réussi à attaquer en premier !, les combattants veulent probablement se reposer un peu mais le round suivant va démarrer.")
        return (P1.pv, P2.pv)
    PAtk = ordre[0] #joueur qui attaque
    PDef = ordre[1] #joueur qui se défend
    Vatk = PAtk.attaque()
    Vdef = PDef.defense(Vatk)
    print(f"{PAtk.nom} a l'initiative et attaque {PDef.nom} avec {Vatk} !")
    if Vdef:
        print(f"{PDef.nom} réussit sa défense.")
        PDef.pex += 3
    else:
        if PDef.pv > 0:
            print(f"{PDef.nom} rate sa défense et n'a plus que {PDef.pv} points de vie !")
            PAtk.pex += 3
        else:
            print(f"{PDef.nom} rate sa défense, le coup porté par {PAtk.nom} lui a été fatal !")
            PAtk.pex += 5
            if ordre[0] == P1:
                return (PAtk.pv, PDef.pv, PAtk.pex, PDef.pex)
            else:
                return (PDef.pv, PAtk.pv, PDef.pex, PAtk.pex)
    Vatk = PDef.attaque()
    Vdef = PAtk.defense(Vatk)
    print(f"{PDef.nom} attaque avec {Vatk} !")
    if Vdef:
        print(f"{PAtk.nom} réussit sa défense.")
        PAtk.pex += 3
    else:
        if PAtk.pv > 0:
            print(f"{PAtk.nom} rate sa défense et n'a plus que {PAtk.pv} points de vie !")
        else:
            print(f"{PAtk.nom} rate sa défense, le coup porté par {PDef.nom} lui a été fatal !")
            if ordre[0] == P1:
                return (PAtk.pv, PDef.pv, PAtk.pex, PDef.pex)
            else:
                return (PDef.pv, PAtk.pv, PDef.pex, PAtk.pex)
    if ordre[0] == P1:
        return (PAtk.pv, PDef.pv, PAtk.pex, PDef.pex)
    else:
        return (PDef.pv, PAtk.pv, PDef.pex, PAtk.pex)

if __name__ == "__main__":
    firstPlayer = Personnage("Bill", 30, 25, 25, 20)
    secondPlayer = Personnage("Bob", 28, 19, 40, 40)