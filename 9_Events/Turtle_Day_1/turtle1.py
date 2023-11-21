import turtle

WIN_WIDTH=300
WIN_HEIGHT=300
turtle.setup(WIN_WIDTH, WIN_HEIGHT)
win=turtle.Screen()

tim=turtle.Turtle()
tim.pencolor("red") # red using standard color names.
#tim.pencolor("#FF0000") # red in hex
#turtle.colormode(255) # 1) set colormode to 255 to then start using RGB
#tim.pencolor((255, 0, 0)) # 2) set color red in rgb
tim.circle(40)

win.mainloop()