#imports and setting turtle name
import turtle
import time
t = turtle

#lets define mountain
def mountain(pcolor, psize):
    t.penup()
    t.goto(25,25)
    t.pencolor(pcolor)
    t.pensize(psize)
    t.pendown()
    for m in range(5):
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
    t.penup()
    t.goto(25,25)
    t.shape("turtle")
    t.pencolor("black")
    for m in range(5):
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
    t.write("Hooray! Made it to the top!", align="right", font=("arial", 12, "normal"))
    time.sleep(3)
    t.reset()
    t.shape("classic")

#lets define swimming
def swimming(pcolor, psize):
    t.pencolor(pcolor)
    t.pensize(psize)
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.circle(80)
    t.penup()
    t.goto(-100,110)
    t.color("blue")
    t.pencolor("blue")
    t.begin_fill()
    t.pendown()
    t.circle(70)
    t.end_fill()
    t.penup()
    t.goto(-100,100)
    t.fillcolor("green")
    t.pencolor("green")
    t.shape("turtle")
    t.circle(80)
    t.pencolor("blue")
    t.left(90)
    t.pendown()
    t.forward(50)
    t.pencolor("black")
    t.write("Yeah!, I'm swimming!",align= "right",font=("arial", 12, "normal"))
    time.sleep(3)
    t.reset()
    t.shape("classic")

#lets define Eating
def eating():
    color = ["red", "yellow", "green", "orange"]
    t.penup()
    hor = -175
    ver = -175
    t.goto(hor,ver)
    for f in range(4):
        t.fillcolor(color[f])
        t.pencolor(color[f])
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        hor = hor + 29
        ver = ver + 29
        if f != 4:
            t.goto(hor,ver)
    hor = -175
    ver = -175
    t.goto(hor,ver)
    t.shape("turtle")
    for e in range(4):
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.pencolor("green")
        t.fillcolor("green")
        time.sleep(1)
        hor = hor + 29
        ver = ver + 29
        if e != 3:
            t.goto(hor,ver)
        else:
            t.pencolor("black")
            t.write("Wow! What a great meal!",align= "right",font=("arial", 12, "normal"))
            time.sleep(3)
            t.reset()
            t.shape("classic")

#and now defining sleeping
def sleeping():
    t.penup()
    t.goto(150,-150)
    t.fillcolor("brown")
    t.begin_fill()
    for b in range(2):
        t.forward(50)
        t.left(90)
        t.forward(120)
        t.left(90)
        t.forward(50)
    t.end_fill()
    t.goto(150,-80)
    t.fillcolor("white")
    t.begin_fill()
    for p in range(2):
        t.forward(15)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(15)
    t.end_fill()
    t.goto(150,-160)
    t.fillcolor("green")
    t.pencolor("green")
    t.shape("turtle")
    t.left(90)
    t.forward(95)
    t.pencolor("black")
    t.write("Good Night!",align= "right",font=("arial", 12, "normal"))
    time.sleep(3)

#lets define main
def main():
    t.setup(600,600)
    pcolor = "red"
    psize = 3
    mountain(pcolor, psize)
    pcolor = "yellow"
    swimming(pcolor, psize)
    eating()
    sleeping()

#calling everything
main()
