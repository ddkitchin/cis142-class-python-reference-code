# Code based upon 
# http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle

# Event handler to move turtle forward 10 pixels
def forward():
   myTurtle.forward(10)

# Event handler to turn turtle left 45 degrees
def left():
   myTurtle.left(45)

# Event handler to turn turtle right 45 degrees
def right():
   myTurtle.right(45)

# Event handler to close the window
def closeWindow():
   win.bye()  

# Event handler to reset the turtle window
def reset():
   myTurtle.reset()

# Configure the window and create a turtle
WIN_WIDTH = 300
WIN_HEIGHT = 300
turtle.setup(WIN_WIDTH, WIN_HEIGHT) 
win = turtle.Screen()  
win.title("Handling keypresses!") 
win.bgcolor("lightgreen") 
myTurtle = turtle.Turtle() 

# Bind window events to the event handlers
win.onkey(forward, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(closeWindow, "q")
win.onkey(reset, "c")

# Tell window to listen to events
win.listen()

# Wait for user to close window
win.mainloop()
