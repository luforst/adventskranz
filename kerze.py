from turtle import *

GROESSE = 0.5
FARBE = "red"
FAERBEN = True
SHAPE = "turtle"

fillcolor(FARBE)
shape(SHAPE)

def zeichneKerze(brennt):
    pd()
    begin_fill()
    forward(GROESSE*100)
    left(90)
    forward(GROESSE*400)
    left(90)
    forward(GROESSE*100)
    right(90)
    forward(GROESSE*30)
    back(GROESSE*30)
    left(90)
    forward(GROESSE*100)
    left(90)
    forward(GROESSE*400)
    left(90)
    forward(GROESSE*100)
    end_fill()
    pu()
    if brennt:
        zeichneFlamme()

def zeichneFlamme():
    left(90)
    fd(GROESSE*430)
    pd()
    color("yellow")
    dot(GROESSE*60)
    color("black")
    back(GROESSE*30)
    pu()
    home()

if __name__=="__main__":
    zeichneKerze(True)
    hideturtle()
