# Code based upon 
# http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle

# Event handler to move the turtle where clicked
# @param y The clicked x-coordinate
# @param y The clicked y-coordinate
def move(x, y):
   myTurtle.goto(x, y)

# Event handler to erase drawing and reposition turtle at the origin
def erase():
   myTurtle.clear()
   myTurtle.penup()
   myTurtle.home()
   myTurtle.pendown()

# Configure the window and create a turtle
WIN_WIDTH = 300
WIN_HEIGHT = 300
turtle.setup(WIN_WIDTH, WIN_HEIGHT) 
win = turtle.Screen()  
win.title("Click to Move") 
win.bgcolor("lightgreen") 
myTurtle = turtle.Turtle() 
myTurtle.color("purple")
myTurtle.pensize(3)
myTurtle.shape("circle")

# Bind window events to the event handlers
win.onclick(move)
win.onkey(erase, "c")

# Listen for events
win.listen()
win.mainloop()
