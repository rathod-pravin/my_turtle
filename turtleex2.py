import turtle
wn=turtle.Screen()
try:
	kasa=turtle.Turtle()
except:
	kasa=turtle.Turtle()
kasa.color('blue')
kasa.forward(100)
kasa.color([ .9, .5, .2])
kasa.left(90)
kasa.forward(100)
wn.exitonclick()
