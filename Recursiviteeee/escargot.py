import turtle
from math import *

def triangleEquilateral(c) :
    for _ in range (3):
        leo.forward(c)
        leo.left(120)
        
        
def pentagramme(c, color="red") :
    leo.pencolor(color)
    for _ in range (5):
        leo.forward(c)
        leo.right(144)
    leo.left(36)
    for _ in range(5):
        leo.forward(c/(2*cos(36*pi/180)))
        leo.right(72)
    leo.left(215)
    leo.circle(c/(4*cos(36*pi/180)*cos(54*pi/180)))


def hexagone(c, diag = False) :
    for _ in range (6):
        leo.forward(c)
        leo.left(60)    
    leo.left(60)
    leo.forward(2*c)
    for _ in range(2):
        leo.left(120)
        leo.forward(c)
        leo.left(120)
        leo.forward(2*c)



if __name__ == "__main__" :
    screen = turtle.Screen()
    screen.bgcolor('lightgray')
    leo = turtle.Turtle()
    
    hexagone(200,0)
    
    turtle.exitonclick()
