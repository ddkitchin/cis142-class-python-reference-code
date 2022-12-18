# Code based upon 
# http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle
from random import randint

# Configure the turtle window
# @return a reference to the window
def setWindow() :
    WIN_WIDTH = 300
    WIN_HEIGHT = 300    
    turtle.setup(WIN_WIDTH, WIN_HEIGHT)
    win = turtle.Screen()                 
    win.title("Drawing Stars") 
    win.bgcolor("lightgreen") 
    
    return win

# Event handler to erase drawing and reposition turtle at the origin
def erase():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.home()
    myTurtle.pendown()

# Handle a mouse click on Tess
# @param x The clicked x-coordinate
# @param y The clicked y-coordinate
def makeStar(x, y):
    win.title("Turtle clicked at {0}, {1}".format(x, y))
    NUM_SQUARE_SIDES = 5
    SIDE_LENGTH=40
    ANGLE=36
    colors=["red", "purple", "blue", "green"]
    myTurtle.penup()
    myTurtle.setposition(x,y)
    myTurtle.setheading(0)
    myTurtle.pencolor(colors[randint(0,3)])
    myTurtle.pendown()
    myTurtle.forward(SIDE_LENGTH)
    myTurtle.right(180-ANGLE)
    myTurtle.forward(SIDE_LENGTH)
    myTurtle.right(180-ANGLE)
    myTurtle.forward(SIDE_LENGTH)
    myTurtle.right(180-ANGLE)
    myTurtle.forward(SIDE_LENGTH)
    myTurtle.right(180-ANGLE)
    myTurtle.forward(SIDE_LENGTH)
    myTurtle.right(180-ANGLE)

# Configure the window, create two turtles, and run the program
win = setWindow()
myTurtle = turtle.Turtle() 
myTurtle.hideturtle()

# Bind the events
win.onclick(makeStar)
win.onkey(erase, "c")

# Listen for events
win.listen()
win.mainloop()
