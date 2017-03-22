import turtle as t

GROESSE = 0.4
FARBE = "red"
FAERBEN = True
SHAPE = "turtle"

t.fillcolor(FARBE)
t.shape(SHAPE)
t.pu()

def zeichneKerze(brennt):
    t.pd()
    t.fillcolor(FARBE)
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
    t.bk(GROESSE*400)
    t.right(90)

def zeichneZweige(numCandles):
    t.pd()
    t.pensize(GROESSE * 200)
    t.color("darkgreen")
    t.fd(numCandles * 75 * GROESSE*2)
    t.bk(numCandles * 150 * GROESSE*2)
    t.pu()

def zeichneKranz(numCandles, numBurning):
    t.pu()
    if numCandles in [2,4]:
        t.bk(GROESSE * 125)
    t.bk(GROESSE * 250) # equivalent to numCandles * GROESSE * 250/numCandles
    for i in range(numCandles):
        isBurning = (i < numBurning)
        zeichneKerze(isBurning)
        t.fd(GROESSE * 250)
    t.pu()
    t.home()
    zeichneZweige(numCandles)

if __name__=="__main__":
    zeichneKranz(4, 4)
    t.hideturtle()
