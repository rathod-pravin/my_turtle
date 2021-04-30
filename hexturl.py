import turtle
col=("yellow","red","white","cyan","green")
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(25)
c=0
for i in range(150):
	t.color(col[c])
	t.forward(i*1.5)
	t.left(59)
	t.width(3)
	if c==4:
		c=0
	else:
		c+=1
turtle.mainloop()
