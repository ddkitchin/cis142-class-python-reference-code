import turtle

WIN_WIDTH=300
WIN_HEIGHT=300
turtle.setup(WIN_WIDTH, WIN_HEIGHT)
win=turtle.Screen()
win.title("Turtle Program 2")
win.bgcolor("lightgray")

terry=turtle.Turtle()
terry.forward(40)
terry.left(90)
terry.forward(40)
terry.left(90)
terry.forward(40)
terry.left(90)
terry.forward(40)
terry.left(90)

tim=turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.setposition(-50,25)
tim.pencolor("red")
tim.pendown()
tim.circle(20)

win.mainloop()