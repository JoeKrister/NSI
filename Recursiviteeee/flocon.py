import turtle
import random

def segment(c):
    raph.pencolor(random.choice(couleurs))
    raph.forward(c/3)
    raph.left(60)
    raph.forward(c/3)
    raph.right(120)
    raph.forward(c/3)
    raph.left(60)
    raph.forward(c/3)

        
def segmentR(c,n):
    if n == 0:
        raph.forward(c)
    else:    
        segmentR(c/3, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.left(60)
        segmentR(c/3, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.right(120)
        segmentR(c/3, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.left(60)
        segmentR(c/3, n-1)
        raph.pencolor(random.choice(couleurs))
    
def floconVK(long,n) :
    raph.pencolor(random.choice(couleurs))
    raph.begin_fill()
    for _ in range(3) :
        raph.pencolor(random.choice(couleurs))
        segmentR(long, n)
        raph.right(120)

def triangleR(c,n):
    if n == 0:
        raph.forward(c)
    else:    
        triangleR(c, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.left(120)
        triangleR(c, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.left(120)
        triangleR(c, n-1)
        raph.pencolor(random.choice(couleurs))
        raph.left(120)
        triangleR(c, n-1)
        raph.pencolor(random.choice(couleurs))
        
def triforce(c,n):
    if n == 0:
        raph.begin_fill()
        for _ in range(3):
            raph.forward(c)
            raph.left(120)
        raph.end_fill()
            
    else:
        raph.color(random.choice(couleurs), random.choice(couleurs))
        triforce(c/2, n-1)
        raph.forward(c/2)
        triforce(c/2, n-1)
        raph.left(120)
        raph.forward(c/2)
        raph.right(120)
        triforce(c/2, n-1)
        raph.penup()
        raph.right(120)
        raph.forward(c/2)
        raph.left(120)
        raph.pendown()
        
def drapeau(n):
    if n == 0:
        raph.forward(150)
        raph.right(90)
        raph.forward(50)
        raph.right(90)
        raph.forward(150)
        raph.right(90)
        raph.forward(50)
    else:
        drapeau(0)
        raph.forward(15)
        drapeau(n)
            
        
        
            
if __name__ == "__main__" :
    couleurs=["black","white","grey","red","orange","green",
  "blue","navy","yellow","gold","tan","brown",
  "sienna","wheat","cyan","pink","salmon","violet","purple"]
    screen = turtle.Screen()
    screen.bgcolor(random.choice(couleurs))
    raph = turtle.Turtle()
    raph.speed(0)
    
    drapeau(2)
    
    turtle.exitonclick()