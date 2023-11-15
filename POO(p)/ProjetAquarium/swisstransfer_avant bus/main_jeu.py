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
liste_poisson = []
total_poisson = 0


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
        self.croissance_algue = croissance_algue #influance la rapidité de croissance des algues
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

    def crea_poisson(self,nb):
        global total_poisson
        if nb == 0 :
            p = Poisson(nb, 100, 250, 0.4)
        elif nb == 1 :
            p = Poisson(nb, 200, 380, 0.6)
        elif nb == 2 :
            p = Poisson(nb, 300, 450, 0.8)
        elif nb == 3 :
            p = Poisson(nb, 500, 800, 0.9)
        elif nb == 4 :
            p = Poisson(nb, 999, 1000, 1.5)
        if self.argent.argent >= p.prix:
            self.argent.argent -= p.prix
            liste_poisson.append(p)
            total_poisson += 1

    def toujours_en_vie(self):
        if self.vie <= 0:
            liste_poisson.remove(self)
        else:
            self.vie -= 0.1

    def age(self):
        if self.vie < self.vie_tt/3:
            return 2
        elif self.vie > (self.vie_tt/3)*2:
            return 0
        else:
            return 1


class Level:
    def __init__(self):
        self.exp = 0
        self.level = 0
        self.gain_poisson = 5
        self.argent = Argent()

    def level_up(self):
        if self.exp >= 0:
            self.level = 0
        if self.exp >= 500:
            self.level = 1
        if self.exp >= 1000:
            self.level = 2
        if self.exp >= 1800:
            self.level = 3
        if self.exp >= 3000:
            self.level = 4


    def gain_exp(self):
        if len(liste_poisson) >= self.gain_poisson:
            self.exp += 100
            self.gain_poisson += 5
        elif len(liste_poisson) < self.gain_poisson - 5:
            self.exp -= 100
            self.gain_poisson -= 5

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

    def augmentation(self):
        multi = 1
        if len(liste_poisson) != 0:
            for i in liste_poisson:
                multi += i.croissance_algue
        self.argent += 1 * multi
        self.argent_tt += 1 * multi
        self.multi = multi

class App:
    def __init__(self):
        global liste_poisson
        pyxel.init(256, 160)
        pyxel.load("main_jeu.pyxres")
        self.argent = Argent()
        self.level = Level()
        pyxel.mouse(True)
        pyxel.playm(0, 1, True)
        pyxel.run(self.update, self.draw)
        # ne rien mettre apres


    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            quit()
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.argent.augmentation()
            self.level.exp += 1
        if pyxel.btnr(pyxel.KEY_KP_0):
            Poisson.crea_poisson(self, 0)
        if pyxel.btnr(pyxel.KEY_KP_1):
            Poisson.crea_poisson(self, 1)
        if pyxel.btnr(pyxel.KEY_KP_2):
            Poisson.crea_poisson(self, 2)
        if pyxel.btnr(pyxel.KEY_KP_3):
            Poisson.crea_poisson(self, 3)
        if pyxel.btnr(pyxel.KEY_KP_4):
            Poisson.crea_poisson(self, 4)
        if pyxel.btnr(pyxel.KEY_SHIFT):
            self.argent.argent = 10000000
            self.argent.argent_tt += 10000000
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            if is_mouse_over_button(200, 0, 100, 30):
                Poisson.crea_poisson(self, 0)
            if is_mouse_over_button(200, 33, 100, 30):
                Poisson.crea_poisson(self, 1)
            if is_mouse_over_button(200, 65, 100, 30):
                Poisson.crea_poisson(self, 2)
            if is_mouse_over_button(200, 97, 100, 30):
                Poisson.crea_poisson(self, 3)
            if is_mouse_over_button(200, 129, 100, 30):
                Poisson.crea_poisson(self, 4)
        self.level.level_up()
        self.level.gain_exp()


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 160, 0)
        if len(liste_poisson) != 0:
            for i in liste_poisson:
                i.toujours_en_vie()
            for i in liste_poisson:
                i.deplacement()
        else:
            pyxel.text(8, 40, f'Pour acheter des poissons', 7)
            pyxel.text(8, 48, f'utilise les touches 0,1,2,3,4 du numpad', 7)
            pyxel.text(8, 56, f'ou clic droit sur le poisson dans la boutique', 7)
            pyxel.text(8, 64, f"Attention, vos poissons prennent de l'age", 7)
            if self.argent.argent < 100:
                pyxel.text(8, 80, f"Pour gagner de l'argent", 7)
                pyxel.text(8, 88, f"clic gauche sur l'ecran", 7)
        pyxel.text(5, 149.5, f'Nombre de poissons : {len(liste_poisson)} / Votre argent : {round(self.argent.argent)}', 7)

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

        if pyxel.btn(pyxel.KEY_S):
            pyxel.text(5, 6, f'Argent total : {round(self.argent.argent_tt)}', 7)
            pyxel.text(5, 14, f'Poissons total : {total_poisson}', 7)
            pyxel.text(5, 22, f'Gain par clic: {round(self.argent.multi)}', 7)
            pyxel.text(5, 30, f'Duree : {round(time.time() - TEMPS_DEBUT)}', 7)
            pyxel.text(5, 38, f'EXP : {self.level.exp}', 7)
        else:
            pyxel.text(5, 6, f'S pour stats', 7)

        self.level.affichage()

App()
