import turtle
import random
import time
import math

def Turtle_screen(): # Andy
#setup screen
    turtle.setup(800, 800)
    turtle.screensize(800, 800)


def leaves_season(season): # Andy
# get input and draw leaves
    if season == "summer":
        for x in range(750):
            draw_leaves("green", "dark green")
    elif season == "fall":
        color1 = ["green", "yellow", "red", "orange"]
        color2 = ["dark green", "gold", "dark red", "dark orange"]
        for x in range(750):
            number = random.randint(0, 3)
            draw_leaves(color1[number], color2[number])
    elif season == "spring":
        for x in range(750):
            draw_leaves("green", "dark green")


def random_point_circle(): # Andy
# random function that pick a reandom point in a circular area
    circle_radius = 220
    circle_x = 0
    circle_y = -30
    random_number_in_radius = circle_radius * math.sqrt(random.uniform(0, 1))
    num = random.uniform(0, 1) * 2 * math.pi
    x = circle_x + random_number_in_radius * math.cos(num)
    y = circle_y + abs(random_number_in_radius * math.sin(num))
    return x, y


def draw_leaves(color1, color2): # Andy
# random x and y cords
    x, y = random_point_circle()
    # draw leaves 
    turtle.penup()
    turtle.speed(0)
    turtle.pencolor(color1)
    turtle.fillcolor(color1)
    turtle.goto(x, y)
    turtle.left(random.randint(0, 360))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(60, 70)
    turtle.left(110)
    turtle.circle(60, 70)
    turtle.end_fill()
    turtle.pensize(3)
    # draw inside leaves line
    turtle.pencolor(color2)
    turtle.left(145)
    x, y = turtle.pos()
    leaves_move = [20, 15, 9]
    for count in range(3):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(17.5 * (count + 1))
        turtle.right(30)
        turtle.forward(leaves_move[count])
        turtle.penup()
        turtle.left(30)
    for count in range(3):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(17.5 * (count + 1))
        turtle.left(30)
        turtle.forward(leaves_move[count])
        turtle.penup()
        turtle.right(30)
    turtle.penup()


def draw_leaves_background(color1, color2, x, y): # Andy
    turtle.penup()
    turtle.speed(0)
    turtle.pencolor(color1)
    turtle.fillcolor(color1)
    turtle.goto(x, y)
    turtle.left(random.randint(0, 360))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(60, 70)
    turtle.left(110)
    turtle.circle(60, 70)
    turtle.end_fill()
    turtle.pensize(3)
    # leaves line
    turtle.pencolor(color2)
    turtle.left(145)
    x, y = turtle.pos()
    leaves_move = [20, 15, 9]
    for count in range(3):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(17.5 * (count + 1))
        turtle.right(30)
        turtle.forward(leaves_move[count])
        turtle.penup()
        turtle.left(30)
    for count in range(3):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(17.5 * (count + 1))
        turtle.left(30)
        turtle.forward(leaves_move[count])
        turtle.penup()
        turtle.right(30)
    turtle.penup()


def Stump(): #victoria
  #trunk of tree
  turtle.penup()
  turtle.goto(-50,-325)
  #set pensize and color
  turtle.pensize(10)
  turtle.color('saddlebrown')
  turtle.pendown()
  turtle.begin_fill()
  #begin drawing
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(325)
  turtle.left(90)
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(325)
  turtle.end_fill()
  turtle.penup()
  
  #triangles at bottom of tree
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(90)
  turtle.forward(45)
  turtle.right(135)
  turtle.forward(60)
  turtle.right(45)
  turtle.forward(100)
  turtle.end_fill()
  turtle.begin_fill()
  turtle.right(45)
  turtle.forward(60)
  turtle.right(135)
  turtle.forward(50)
  turtle.end_fill()
  #call function to draw branches
  Branches()


def Branches(): #Victoria
  #define variable
    turn=int()
    first=int()
    second=int()
    third=int()
    firstdeg=int()
    seconddeg=int()
    pensize=int()
    #set turn
    turn = 0
    
    #branches turning right   
    for index in range(0,17): 
      #set up variables/random numbers
        first=random.randint(100,130)
        second=random.randint(60,100)
        third=random.randint(60,100)
        firstdeg=random.randint(25,45)
        seconddeg=random.randint(25,45)
        pensize=random.randint(2,6)
        #start drawing
        turtle.penup()
        turtle.pensize(pensize)
        turtle.goto(0,-30)
        turtle.setheading(170)
        turtle.pendown()
        turtle.right(turn)
        turtle.forward(first)
        turtle.left(firstdeg)
        turtle.forward(second)
        turtle.right(seconddeg)
        turtle.forward(third)
        turtle.penup()
        turn=turn+10
    
    #second set of branches
    turn=5
    for index in range(0,17): 
      #set variables
        first=random.randint(100,130)
        second=random.randint(60,100)
        third=random.randint(60,100)
        firstdeg=random.randint(25,45)
        seconddeg=random.randint(25,45)
        pensize=random.randint(2,6)
        #start drawing
        turtle.penup()
        turtle.pensize(pensize)
        turtle.goto(0,-30)
        turtle.setheading(10)
        turtle.pendown()
        turtle.left(turn)
        turtle.forward(first)
        turtle.right(firstdeg)
        turtle.forward(second)
        turtle.left(seconddeg)
        turtle.forward(third)
        turtle.penup()
        turn=turn+10
  

 
def Floor(season):  # Michael
    if season == "spring":
        # Creating the flooring
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("green")
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-300, -300)
        # Creating the first flowers
        #Creating the stem
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("green")
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(8)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(8)
        turtle.end_fill()
        turtle.penup()
        #Creating the bulb
        turtle.goto(-295, -235)
        turtle.fillcolor('blue')
        turtle.pencolor('blue')
        turtle.pensize(1)
        turtle.begin_fill()
        turtle.circle(15)
        turtle.end_fill()
        #Creating the petals
        #First petal
        turtle.goto(-310, -245)
        turtle.pendown()
        turtle.pencolor("blue")
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.right(45)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.penup()
        #Second petal
        turtle.goto(-290, -245)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(4)
        turtle.penup()
        #Third petal
        turtle.goto(-300, -250)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.penup()
        #Fourth petal
        turtle.goto(-290, -250)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.end_fill()
        turtle.penup()
        #Creating the second flower
        #Stem
        turtle.right(180)
        turtle.goto(250, -300)
        turtle.left(90)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("green")
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(5)
        turtle.end_fill()
        turtle.penup()
        #Bulb
        turtle.goto(252.5, -235)
        turtle.fillcolor('red')
        turtle.pencolor('red')
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        #First petal
        turtle.goto(242.5, -240)
        turtle.pendown()
        turtle.pencolor("red")
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.right(45)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.penup()
        # Second petal
        turtle.goto(255, -240)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(18)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(18)
        turtle.right(90)
        turtle.forward(4)
        turtle.penup()
        # Third petal
        turtle.goto(245, -250)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.penup()
        # Fourth petal
        turtle.goto(260, -245)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(18)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(18)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(45)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
    elif season == "fall":
        # Creating first leaf pile
        turtle.seth(0)
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(285, -355)
        turtle.fillcolor("red")
        turtle.circle(50)
        turtle.end_fill()
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.goto(250, -340)
        turtle.circle(50)
        turtle.end_fill()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.goto(275, -330)
        turtle.circle(35)
        turtle.end_fill()
        # Creating second leaf pile
        turtle.goto(-250, -355)
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.goto(-265, -340)
        turtle.circle(40)
        turtle.end_fill()
        # Creating the floor
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.begin_fill()
        turtle.pencolor("green")
        turtle.fillcolor("green")
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    elif season == "winter":
        # Creating snow pile
        turtle.penup()
        turtle.goto(-250, -325)
        turtle.fillcolor("gray")
        turtle.begin_fill()
        turtle.circle(25)
        turtle.goto(-215, -325)
        turtle.circle(35)
        turtle.goto(-190, -325)
        turtle.circle(20)
        turtle.end_fill()
        #Creating the snowman
        #Creating the bottom
        turtle.goto(275, -320)
        turtle.begin_fill()
        turtle.fillcolor("gray")
        turtle.circle(45)
        #Creating the center
        turtle.goto(275,-245)
        turtle.fillcolor("gray")
        turtle.circle(30)
        #Creating the top
        turtle.goto(275, -190)
        turtle.fillcolor("gray")
        turtle.circle(15)
        turtle.end_fill()
        # Creating the floor
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("gray")
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    elif season == "summer":
        x = int()
        #Creating a bush
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(255, -340)
        turtle.fillcolor("green")
        turtle.pencolor("green")
        turtle.circle(35)
        turtle.end_fill()
        #Creating the floor
        turtle.penup()
        turtle.goto(-400, -325)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("green")
        turtle.pencolor("green")
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.left(90)
        #Creating the grass
        for x in range(50):
            turtle.begin_fill()
            turtle.goto((random.randint(-400, 400)), -325)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(3)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(3)
            turtle.right(90)
            turtle.end_fill()
        turtle.right(90)


def Background(season): #patrick
  turtle.penup()
  if season == "summer":
  #drawing a sun
    turtle.goto(300,300)
    turtle.fillcolor("yellow")
    turtle.pencolor("red")
    turtle.pensize(4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
  elif season == "winter":
    #drawing clouds
    for cloud in range(30):
        c = random.randint(0,1)
        colors = ["darkgray", "gray"]
        turtle.goto((random.randint(-400,400)),(random.randint(340,400)))
        turtle.fillcolor(colors[c])
        turtle.begin_fill()
        turtle.circle((random.randint(30, 50)))
        turtle.end_fill()
    turtle.fillcolor("silver")
    #drawing snow
    for snow in range(40):
      turtle.goto((random.randint(-400,400)),(random.randint(-400,400)))
      turtle.begin_fill()
      turtle.circle(2)
      turtle.end_fill()
  elif season == "fall":
    #drawing scattered leaves
    color1 = ["green", "yellow", "red", "orange"]
    color2 = ["dark green", "gold", "dark red", "dark orange"]
    for leaves in range(25):
        x = random.randint(-400,400)
        y = random.randint(-400, 300)
        colorx = random.randint(0, 3)
        turtle.penup()
        turtle.speed(0)
        turtle.pencolor(color1[colorx])
        turtle.fillcolor(color1[colorx])
        turtle.goto(x, y)
        turtle.left(random.randint(0, 360))
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(60, 70)
        turtle.left(110)
        turtle.circle(60, 70)
        turtle.end_fill()
        turtle.pensize(3)
        # leaves line
        turtle.pencolor(color2[colorx])
        turtle.left(145)
        x, y = turtle.pos()
        leaves_move = [20, 15, 9]
        for count in range(3):
            turtle.goto(x, y)
            turtle.pendown()
            turtle.forward(17.5 * (count + 1))
            turtle.right(30)
            turtle.forward(leaves_move[count])
            turtle.penup()
            turtle.left(30)
        for count in range(3):
            turtle.goto(x, y)
            turtle.pendown()
            turtle.forward(17.5 * (count + 1))
            turtle.left(30)
            turtle.forward(leaves_move[count])
            turtle.penup()
            turtle.right(30)
        turtle.penup()
        #drawing wind swooshes
    for wind in range(3):
        turtle.pensize(1)
        x = random.randint(-400,400)
        y = random.randint(-400, 400)
        turtle.goto(x, y)
        w = 1
        for swoosh in range(8):
            turtle.pencolor("black")
            turtle.pendown()
            turtle.left(w)
            turtle.forward(10)
            w = w + 10
            turtle.penup()
  elif season == "spring":
    #drawing clouds
    for cloud in range(30):
        c = random.randint(0,1)
        colors = ["gray", "dimgray"]
        turtle.goto((random.randint(-400,400)),(random.randint(340,400)))
        turtle.fillcolor(colors[c])
        turtle.begin_fill()
        turtle.circle((random.randint(30, 50)))
        turtle.end_fill()
    turtle.left(90)
    #drawing rain
    for rain in range(50):
        turtle.pensize(2)       
        turtle.goto((random.randint(-400,400)),(random.randint(-400,400)))
        turtle.pencolor("blue")
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
    turtle.right(90)
  

#define the main function
def main(): #andy/victoria
    turtle.speed(0)
    #set turtle screen
    Turtle_screen()
    #define varaibles
    season = str()
    #get inout from user for season
    print('Pick a season: spring, summer, fall or winter.')
    season = input('Season?: ')
    #call functions based on season
    if season == "spring":
        Background(season)
        Floor(season)
        Stump()
        turtle.tracer(0)
        leaves_season(season)
    elif season == "summer":
        Background(season)
        Floor(season)
        Stump()
        turtle.tracer(0)
        leaves_season(season)
    elif season == "winter":
        Background(season)
        Floor(season)
        Stump()
        turtle.tracer(0)
        leaves_season(season)
    elif season == "fall":
        Background(season)
        Floor(season)
        Stump()
        turtle.tracer(0)
        leaves_season(season)
    turtle.update()
    
main()
turtle.done()