import turtle as t

SIZE = 0.5
CANDLE_COLOR = "red"
DYE = True
SHAPE = "turtle"

t.fillcolor(CANDLE_COLOR)
t.shape(SHAPE)
t.pu()

def drawCandle(is_candle_burning):
    t.pd()
    t.fillcolor(CANDLE_COLOR)
    t.begin_fill()
    t.forward(SIZE*100)
    t.left(90)
    t.forward(SIZE*400)
    t.left(90)
    t.forward(SIZE*100)
    t.right(90)
    t.forward(SIZE*30)
    t.back(SIZE*30)
    t.left(90)
    t.forward(SIZE*100)
    t.left(90)
    t.forward(SIZE*400)
    t.left(90)
    t.forward(SIZE*100)
    t.end_fill()
    t.pu()
    if is_candle_burning:
        drawFlame()

def drawFlame():
    t.left(90)
    t.fd(SIZE*430)
    t.pd()
    t.color("yellow")
    t.dot(SIZE*60)
    t.color("black")
    t.back(SIZE*30)
    t.pu()
    t.bk(SIZE*400)
    t.right(90)

def drawLop(numCandles):
    t.pd()
    t.pensize(100)
    t.color("darkgreen")
    t.fd(numCandles * 75)
    t.bk(numCandles * 150)
    t.pu()

def drawWreath(numCandles, numBurning):
    t.pu()
    if numCandles in [2,4]:
        t.bk(SIZE * 125)
    t.bk(SIZE * 250) # equivalent to numCandles * SIZE * 250/numCandles
    for i in range(numCandles):
        isBurning = (i < numBurning)
        drawCandle(isBurning)
        t.fd(SIZE * 250)
    t.pu()
    t.home()
    drawLop(numCandles)

if __name__=="__main__":
    drawWreath(4, 4)
    t.hideturtle()
