from random import randint

class Personnage :
    """ une classe pour représenter un personnage générique du MMORPG """
    def __init__(self, nom, force, endurance, rapidite, intelligence) :
        assert type(nom) == str,"Le nom doit etre une chaîne de caractère"
        self.nom = nom
        assert type(force) == int and 1<= force <= 40,"L'attribut force doit être un nombre entier compris entre 1 et 40" 
        self.force = force
        assert type(endurance) == int and 1<= endurance <= 40, "L'attribut endurance doit être un nombre entier compris entre 1 et 40"
        self.endurance = endurance
        assert type(rapidite) == int and 1<= rapidite <= 40, "L'attribut rapidité doit être un nombre entier compris entre 1 et 40"
        self.rapidite = rapidite
        assert type(intelligence) == int and 1<= intelligence <= 40,"L'attribut intelligence doit être un nombre entier compris entre 1 et 40"
        self.intelligence = intelligence
        self.pv = self.endurance + self.force//2
        self.combat_pex = 0
        self.pex = 0
        self.niveau = 1

        
        
    def affiche(self) :
        print(
            f""" Bonjour je m'appelle {self.nom},
            j'ai {self.force} en force , {self.endurance} en endurance ,
            {self.rapidite} en rapidite , {self.intelligence} en intelligence ,
            je suis niveau {self.niveau} et j'ai {self.pv} PV.""")
        
    def initiative(self):
        return randint(1,20)+ self.rapidite


    def attaque (self) :
        d20 = randint(1,20)
        return self.force + d20
    
    def defense(self, VA) :
        VD = randint(1,20) + self.endurance        
        if VD >= VA :
            return True
        else :
            self.pv -= (VA - VD)
            return False
        return secondPlayer.pv
        
if __name__ =="__main__"     :
    firstPlayer = Personnage ("Bob",30,20,30,20)
    secondPlayer = Personnage("Bill",25,25,25,25)
    
    
