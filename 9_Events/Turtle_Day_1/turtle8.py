# Code based upon 
# http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle

# Configure the turtle window
# @return a reference to the window
def setWindow() :
    WIN_WIDTH = 300
    WIN_HEIGHT = 300    
    turtle.setup(WIN_WIDTH, WIN_HEIGHT)
    win = turtle.Screen()                 
    win.title("Click each turtle") 
    win.bgcolor("lightgreen") 
    
    return win

# Handle a mouse click on Tess
# @param x The clicked x-coordinate
# @param y The clicked y-coordinate
def clickTess(x, y):
    win.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)

# Handle a mouse click on Alex
# @param x The clicked x-coordinate
# @param y The clicked y-coordinate
def clickAlex(x, y):
    win.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(84)
    alex.forward(50)

def main() :  
    # Modify the turtles further
    tess.color("purple")
    tess.resizemode("user")
    tess.shapesize(2, 2)
    alex.color("blue")
    alex.resizemode("user")
    alex.shapesize(2, 2)

    # Separate the turtles
    alex.penup()
    alex.forward(50)
    alex.pendown()
    tess.penup()
    tess.backward(50)
    tess.pendown()
        
    # Bind the events
    tess.onclick(clickTess)
    alex.onclick(clickAlex)

    # Wait for user to close window
    win.mainloop()

# Configure the window, create two turtles, and run the program
win = setWindow()
tess = turtle.Turtle() 
alex = turtle.Turtle()
main()
