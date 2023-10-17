import turtle

def main():
    NUM_SQUARES=20
    colors=["red", "purple", "blue", "green"]
    win=setWindow()
    myTurtle=turtle.Turtle()
    for i in range(NUM_SQUARES):
        myTurtle.pencolor(colors[i % len(colors)])
        drawSquare(myTurtle)
        myTurtle.left(360/NUM_SQUARES)

    win.mainloop()
    
def setWindow():
     
    WIN_WIDTH=300
    WIN_HEIGHT=300
    turtle.setup(WIN_WIDTH, WIN_HEIGHT)
    win=turtle.Screen()
    win.title("Turtle Program 4")
    win.bgcolor("lightblue")
    
    return win

def drawSquare(newTurtle):

    NUM_SQUARE_SIDES = 4
    SIDE_LENGTH=40

    for i in range(NUM_SQUARE_SIDES):
        newTurtle.forward(SIDE_LENGTH)
        newTurtle.left(90)

main()