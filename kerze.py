import turtle as t

GROESSE = 0.5
FARBE = "red"
FAERBEN = True
SHAPE = "turtle"

t.fillcolor(FARBE)
t.shape(SHAPE)
t.pu()

def zeichneKerze(brennt):
    t.pd()
    t.begin_fill()
    t.forward(GROESSE*100)
    t.left(90)
    t.forward(GROESSE*400)
    t.left(90)
    t.forward(GROESSE*100)
    t.right(90)
    t.forward(GROESSE*30)
    t.back(GROESSE*30)
    t.left(90)
    t.forward(GROESSE*100)
    t.left(90)
    t.forward(GROESSE*400)
    t.left(90)
    t.forward(GROESSE*100)
    t.end_fill()
    t.pu()
    if brennt:
        zeichneFlamme()

def zeichneFlamme():
    t.left(90)
    t.fd(GROESSE*430)
    t.pd()
    t.color("yellow")
    t.dot(GROESSE*60)
    t.color("black")
    t.back(GROESSE*30)
    t.pu()
    t.home()

if __name__=="__main__":
    zeichneKerze(True)
    t.hideturtle()
