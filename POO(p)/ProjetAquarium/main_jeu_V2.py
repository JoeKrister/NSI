import random
import time
import pyxel
from random import randint

#Races possible
#poisson rouge (0)
#poisson combatant (1)
#poisson chat (2)
#Carpe Koï (3)
#Discus (4)

TEMPS_DEBUT = time.time()

def is_mouse_over_button(x, y, width, height):
    mouse_x = pyxel.mouse_x
    mouse_y = pyxel.mouse_y
    if x < mouse_x < x + width and y < mouse_y < y + height:
        return True

class Poisson:
    """ Une classe pour représenter un poisson """
     
    def __init__(self, race, prix, vie, croissance_algue):
        self.argent = Argent()
        self.race = race #race du poisson
        self.prix = prix #prix d'achat
        self.croissance_algue = croissance_algue #influence la rapidité de croissance des algues
        self.vie = vie #durée de vie du poisson
        self.vie_tt = self.vie
        self.x = random.randint(5,188)
        self.y = random.randint(5,130)

    def deplacement(self):
        if self.x >= 5 and self.y >= 130:
            self.x += 1
            self.y -= 1
        elif self.x >= 180 and self.y >= 8:
            self.x -= 1
            self.y += 1
        if self.x <= 5 or self.y <= 8:
            self.x += 1
            self.y += 1
        elif self.x >= 180 or self.y >= 130:
            self.x -= 1
            self.y -= 1
        else:
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)
        if self.race == 0:
            pyxel.blt(self.x, self.y, self.age(), 48, 0, 8, 8, 0)
        elif self.race == 1:
            pyxel.blt(self.x, self.y, self.age(), 48, 8, 8, 8, 0)
        elif self.race == 2:
            pyxel.blt(self.x, self.y, self.age(), 48, 24, 16, 8, 0)
        elif self.race == 3:
            pyxel.blt(self.x, self.y, self.age(), 48, 40, 16, 8, 0)
        elif self.race == 4:
            pyxel.blt(self.x, self.y, self.age(), 48, 48, 16, 8, 0)

    def age(self):
        if self.vie < self.vie_tt/3:
            return 2
        elif self.vie > (self.vie_tt/3)*2:
            return 0
        else:
            return 1


class Requin:
    def __init__(self):
        self.x = 15
        self.y = 15
        self.direc = 'down'
    
    def deplacement(self, direc):
        if direc == 'up' and self.y > 3 :
            self.y -= 1
            self.direc = 'up'
        elif direc == 'down' and self.y < 120:
            self.y += 1
            self.direc = 'down'
        elif direc == 'left' and self.x > 4:
            self.x -= 1
            self.direc = 'left'
        elif direc == 'right' and self.x < 164:
            self.x += 1
            self.direc = 'right'
        
    def affichage(self):
        if self.direc == 'up' :
            pyxel.blt(self.x, self.y, 0, 8, 128, 32, 45, 0)
        elif self.direc == 'down' :
            pyxel.blt(self.x, self.y, 0, 8, 128, 32, 45, 0)
        elif self.direc == 'left' :
            pyxel.blt(self.x, self.y, 0, 8, 128, 32, 45, 0)
        elif self.direc == 'right':
            pyxel.blt(self.x, self.y, 0, 8, 128, 32, 45, 0)
        


class Level:
    def __init__(self):
        self.exp = 0
        self.level = 0
        self.gain_poisson = 5
        self.argent = Argent()

    def level_up(self):
        if self.exp >= 0:
            self.level = 0
        if self.exp >= 100:
            self.level = 1
        if self.exp >= 200:
            self.level = 2
        if self.exp >= 300:
            self.level = 3
        if self.exp >= 501:
            self.level = 4


    def gain_exp(self, liste_poisson):
        if len(liste_poisson) >= self.gain_poisson:
            self.exp += 100
            self.gain_poisson += 5


    def affichage(self):
        if self.level == 1 or self.level == 2 or self.level == 3 or self.level == 4:
            pyxel.blt(0, 136, 0, 16, 40, 8, 8, 0)
        if self.level == 2 or self.level == 3 or self.level == 4:
            pyxel.blt(0, 128, 0, 24, 40, 8, 8, 0)
        if self.level == 3 or self.level == 4:
            pyxel.blt(0, 120, 0, 16, 48, 8, 8, 0)
        if self.level == 4:
            pyxel.blt(0, 112, 0, 24, 48, 8, 8, 0)


class Argent:
    def __init__(self):
        self.argent = 90
        self.argent_tt = 90
        self.multi = 1

    def augmentation(self, liste_poisson):
        multi = 1
        if len(liste_poisson) != 0:
            for i in liste_poisson:
                multi += i.croissance_algue
        self.argent += 1 * multi
        self.argent_tt += 1 * multi
        self.multi = multi

class Aqua_box:
    def __init__(self):
        self.liste_poisson = []
        pyxel.init(256, 160)  
        pyxel.load("main_jeu.pyxres")
        self.argent = Argent()
        self.level = Level()
        self.liste_poisson = []
        self.total_poisson = 0
        self.requin = Requin()
        pyxel.mouse(True)
        pyxel.playm(0, 1, True)
        pyxel.run(self.update, self.draw)
        # ne rien mettre apres
            

    def update(self):
        if self.level.level < 4 :
            if pyxel.btn(pyxel.KEY_A):
                quit()
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.argent.augmentation(self.liste_poisson)
                self.level.exp += 1
            if pyxel.btnr(pyxel.KEY_SHIFT):
                self.argent.argent = 10000000
                self.argent.argent_tt += 10000000
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                if is_mouse_over_button(200, 0, 100, 30) or pyxel.btnr(pyxel.KEY_KP_0):
                    if self.argent.argent >= 100:
                        self.argent.argent -= 100
                        self.liste_poisson.append(Poisson(0, 100, 250, 0.4))
                        self.total_poisson +=1
                if is_mouse_over_button(200, 33, 100, 30):
                    if self.argent.argent >= 200:
                        self.argent.argent -= 200
                        self.liste_poisson.append(Poisson(1, 200, 380, 0.6))
                        self.total_poisson +=1
                if is_mouse_over_button(200, 65, 100, 30):
                    if self.argent.argent >= 300:
                        self.argent.argent -= 300
                        self.liste_poisson.append(Poisson(2, 300, 450, 0.8))
                        self.total_poisson +=1
                if is_mouse_over_button(200, 97, 100, 30):
                    if self.argent.argent >= 500:
                        self.argent.argent -= 500
                        self.liste_poisson.append(Poisson(3, 500, 800, 0.9))
                        self.total_poisson +=1
                if is_mouse_over_button(200, 129, 100, 30):
                    if self.argent.argent >= 999:
                        self.argent.argent -= 999
                        self.liste_poisson.append(Poisson(4, 999, 1000, 1.5))
                        self.total_poisson +=1
            self.level.level_up()
            self.level.gain_exp(self.liste_poisson)
        else:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.requin.deplacement('right')
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.requin.deplacement('left')
            elif pyxel.btn(pyxel.KEY_UP):
                self.requin.deplacement('up')
                for e in self.liste_poisson:
                    if self.requin.x < e.x < self.requin.x +20 and self.requin.y < e.y < self.requin.y +20:
                        self.liste_poisson.remove(e)
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.requin.deplacement('down')
            


    def draw(self):
            pyxel.cls(0)
            pyxel.bltm(0, 0, 0, 0, 0, 256, 160, 0)
            if len(self.liste_poisson) != 0:
                for e in self.liste_poisson:
                    e.deplacement()
                for e in self.liste_poisson:
                    if e.vie <= 0:
                        return self.liste_poisson.remove(e)
                    else:
                        e.vie -= 0.1
            else:
                pyxel.text(8, 40, f'Pour acheter des poissons', 7)
                pyxel.text(8, 48, f'Clic droit sur le poisson dans la boutique', 7)
                pyxel.text(8, 56, f"Attention, vos poissons prennent de l'age", 7)
                if self.argent.argent < 100:
                    pyxel.text(8, 80, f"Pour gagner de l'argent", 7)
                    pyxel.text(8, 88, f"clic gauche sur l'ecran", 7)
            pyxel.text(5, 149.5, f'Nombre de poissons : {len(self.liste_poisson)} / Votre argent : {round(self.argent.argent)}', 7)
            pyxel.text(203, 3, f'P. rouge', 7)
            pyxel.text(222, 18, f'100', 7)
            pyxel.text(203, 35, f'P. combatant', 7)
            pyxel.text(222, 50, f'200', 7)
            pyxel.text(203, 67, f'P. chat', 7)
            pyxel.text(222, 82, f'300', 7)
            pyxel.text(203, 99, f'Carpe Koi', 7)
            pyxel.text(222, 114, f'500', 7)
            pyxel.text(203, 131, f'Discus', 7)
            pyxel.text(222, 146, f'999', 7)
            self.level.affichage()
            if pyxel.btn(pyxel.KEY_S):
                pyxel.text(5, 6, f'Argent total : {round(self.argent.argent_tt)}', 7)
                pyxel.text(5, 14, f'Poissons total : {self.total_poisson}', 7)
                pyxel.text(5, 22, f'Gain par clic: {round(self.argent.multi)}', 7)
                pyxel.text(5, 30, f'Duree : {round(time.time() - TEMPS_DEBUT)}', 7)
                pyxel.text(5, 38, f'EXP : {self.level.exp}', 7)
            else:
                pyxel.text(5, 6, f'S pour stats', 7)
            if self.level.level == 4:
                self.requin.affichage()
                if len(self.liste_poisson) == 0:
                    pyxel.cls(0)
                    pyxel.text(8, 30, f'BRAVO !', 7)
                    pyxel.text(8, 50, f'Argent total : {round(self.argent.argent_tt)}', 7)
                    pyxel.text(8, 58, f'Poissons total : {self.total_poisson}', 7)
                    pyxel.text(8, 66, f'Gain par clic: {round(self.argent.multi)}', 7)
                    pyxel.text(8, 74, f'Duree : {round(time.time() - TEMPS_DEBUT)}', 7)
                    pyxel.text(8, 82, f'EXP : {self.level.exp}', 7)
                    
                    
if __name__ == '__main__':
    Aqua_box()