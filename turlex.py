import turtle
win=turtle.Screen()
win.bgcolor("white")
tess=turtle.Turtle()
tess.speed(0)
tess.color("blue")
tess.pensize(3)
offset=90

def donextEvent(x,y):
	global offset
	global win
	tess.forward(20)
	tess.right(1+offset)
	offset=offset-2
	if(offset<1):
		win.exitonclick()
		
		
win.onclick(donextEvent)
win.listen()
win.mainloop()
