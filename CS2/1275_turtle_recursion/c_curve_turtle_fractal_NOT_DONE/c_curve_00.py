import turtle

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
#Change screen dimensions
screen.setup (width=500, height=500, startx=500, starty=0)

pen = turtle.Turtle()
pen.penup()
pen.goto(300,350)
pen.pensize(1)

def drawLine(turt, x1, y1, x2, y2):
    turt.penup()
    turt.goto(x1,y1)
    turt.pendown()
    turt.goto(x2,y2)

def cCurve(turt, x1, y1, x2, y2, level):
    if level == 0:
        drawLine(turt, x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) / 2
        ym = (x2 + y1 + y2 - x1) / 2
        cCurve(turt, x1, y1, xm, ym, level-1)
        cCurve(turt, xm, ym, x2, y2, level-1)

cCurve(pen, 75, -75, 75, 75, 12)

#Refresh the screen
turtle.update()
turtle.done()