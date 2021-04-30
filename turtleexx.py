import turtle
def init_turtle(t):
	t.pensize(2)
	t.speed(5)
	t.color("white")
	
	
def base(t, length, n=4):
	for k in range(n):
		t.forward(length)
		t.left(360/n)
		
		
def flake(t, length, copies=4, n=4):
	for k in range(copies):
		base(t, length, n)
		t.left(360/copies)


if __name__ == "__main__":
	wn = turtle.Screen()
	wn.bgcolor("blue")
	kasa = turtle.Turtle()
	#wn.exitonclick()
	L=90
	S=6
	N=17
	init_turtle(kasa)
	kasa.penup()
	kasa.left(360/S/2)
	kasa.pendown()
	flake(kasa, L, N, S)
	#wn.mainloop()
	wn.exitonclick()
