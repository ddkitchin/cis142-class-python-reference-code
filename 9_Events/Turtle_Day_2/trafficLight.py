import turtle  # Tess becomes a traffic light.

def main():

    drawHousing(tess)

    tess.penup()
    # Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    # Turn tess into a big green circle
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("green")

    # Bind trigger to handler
    win.onkey(advanceStateMachine, "space")

    win.listen()  # Listen for events
    win.mainloop()


def setWindow():
    turtle.setup(400, 500)
    win = turtle.Screen()
    win.title("Tess becomes a traffic light!")
    win.bgcolor("lightgreen")
    return win

def drawHousing(tess):
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
def advanceStateMachine():
    global stateNumber
    if stateNumber == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        stateNumber= 1
    elif stateNumber == 1:  # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        stateNumber = 2
    else:  # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        stateNumber = 0

# This variable holds the current state of the machine
stateNumber = 0

# Create the window and create a turtle
win = setWindow()
tess = turtle.Turtle()

main()