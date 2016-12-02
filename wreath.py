import turtle as t
import kerze

def zeichneZweige(numCandles):
    t.pd()
    t.pensize(100)
    t.color("darkgreen")
    t.fd(numCandles * 75)
    t.bk(numCandles * 150)
    t.pu()

def zeichneKranz(numCandles, numBurning):
    t.pu()
    if numCandles in [2,4]:
        t.bk(kerze.GROESSE * 125)
    t.bk(kerze.GROESSE * 250) # äquivalent zu numCandles * kerze.GROESSE * 250/numCandles
    for i in range(numCandles):
        isBurning = (i < numBurning)
        kerze.zeichneKerze(isBurning)
        t.fd(kerze.GROESSE * 250)
    t.pu()
    t.home()
    zeichneZweige(numCandles)

if __name__=="__main__":
    zeichneKranz(4, 1)
    t.hideturtle()
