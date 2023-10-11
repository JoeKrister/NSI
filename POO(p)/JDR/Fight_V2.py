from personnage import Personnage
from time import sleep 

def presentation() -> None :
    print("""
##############################################
#                                            #
#         Towers & Salamanders 3000          #
#               Dreo et Iwen                 #
#                                            #
##############################################
""")
    print("\n"*3)
    print("Vous allez assister à un combat de titan !")
    print("\n"*2)
    input("(Appuyez sur la touche Entrée...)")
        
    fin = False
    while fin == False:
        demande = input("Etes-vous sur de vouloir continuer ?(oui/non)")
        if type(demande)==str:
            demande = demande.lower()
            demande = demande.strip()
            if demande == 'o' or demande == 'oui' or demande == 'yes' or demande == 'y':
                creation_perso()
                print("\n"*2)
                fin = True
                combat(P1,P2)
            elif demande == 'n' or demande == 'non' or demande == 'no' :
                print("\n"*2)
                print("D'accord, on se reverra...")
                break
            else :
                print("NON !, recommence")
        else :
            print("NON !, recommence")
    return None

def creation_perso():    
    nom = []
    force = []
    endurance = []
    rapidite = []
    intelligence = []
    demande = input("Voulez-vous créer un personnage ?(oui/non)")
    if type(demande)==str:
        demande = demande.lower()
        demande = demande.strip()
        if demande == 'o' or demande == 'oui' or demande == 'yes' or demande == 'y':
            nom = input("Quel est son nom ?")
            force = input("Quelle est sa force ?")
            endurance = input("Quelle est son endurance ?")
            rapidite = input("Quelle est sa rapidité ?")
            intelligence = input("Quelle est son intelligence ?")
            P3 = Personnage(nom, force, endurance, rapidite, intelligence)
        if demande == 'n' or demande == 'non' or demande == 'no' or demande == 'n':
            return None
    

def combat(P1, P2):
    
    P1.combat_pex = 0
    P2.combat_pex = 0
    nb_tour = 0
    
    while P1.pv > 0 and P2.pv > 0:
        nb_tour += 1
        print(f"Round {nb_tour}")
        initP1 = P1.initiative()
        initP2 = P2.initiative()
        if initP1 > initP2:
            P1, P2 = attaque_et_defense(P1,P2)
            sleep(1)
            if P2.pv <= 0 :
                P1.pex += P1.combat_pex
                print (f"Le vainqueur est {P1.nom}, il lui reste {P1.pv} points de vie. Il gagne {P1.combat_pex} points d'expériences.")
                sleep(1)
            else :
                P2, P1 = attaque_et_defense(P2, P1)
                if P1.pv <=0 :
                    print (f"Le vainqueur est {P2.nom}, il lui reste {P2.pv} points de vie. Il gagne {P2.combat_pex} points d'expériences.")
                    sleep(1)
                    
        elif initP2 > initP1:
            P2, P1 = attaque_et_defense(P2, P1)
            if P1.pv <=0 :
                print (f"Le vainqueur est {P2.nom}, il lui reste {P2.pv} points de vie. Il gagne {P2.combat_pex} points d'expériences.")
                sleep(1)
            else :
                P1, P2 = attaque_et_defense(P1, P2)
                if P2.pv <=0 :
                    print (f"Le vainqueur est {P1.nom}, il lui reste {P1.pv} points de vie. Il gagne {P1.combat_pex} points d'expériences.")
                    sleep(1)
        else :
            print ("Malgré la puissance des deux belligérants aucun n'a réussi à prendre l'avantage ! ")

def attaque_et_defense(attaquant, defenseur) :
    VA = attaquant.attaque()
    print(f"{attaquant.nom} à l'initiative et attaque avec {VA}")
    if defenseur.defense(VA) == True :
        print(f"{defenseur.nom} réussit sa défense")
        defenseur.combat_pex += 1
    else :
        print(f"{defenseur.nom} rate sa défense et n'a plus que {defenseur.pv} points de vie")
        attaquant.combat_pex +=2
    return attaquant, defenseur


if __name__ =="__main__"     :
    P1 = Personnage ("Bob",30,20,30,20)
    P2 = Personnage("Bill",25,25,25,25)
    presentation()