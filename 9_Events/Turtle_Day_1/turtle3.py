import turtle

def main():
    win=setWindow()
    snapper=turtle.Turtle()
    drawSquare(snapper,25,-50)

    win.mainloop()
    
def setWindow():
     
    WIN_WIDTH=300
    WIN_HEIGHT=300
    turtle.setup(WIN_WIDTH, WIN_HEIGHT)
    win=turtle.Screen()
    win.title("Turtle Program 3")
    win.bgcolor("lightgray")
    
    return win

def drawSquare(newTurtle,x,y):

    NUM_SQUARE_SIDES = 4
    SIDE_LENGTH=40

    newTurtle.penup()
    newTurtle.setposition(x,y)
    newTurtle.pendown()
    for i in range(NUM_SQUARE_SIDES):
        newTurtle.forward(SIDE_LENGTH)
        newTurtle.left(90)

main()