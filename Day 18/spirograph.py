import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
def randomColor():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    colour = (r,g,b)
    return colour

tim.speed('fastest')
angle = 0
while angle<= 360:
    tim.color(randomColor())
    tim.circle(100)
    tim.setheading(angle)
    angle += 4


screen = t.Screen()
screen.exitonclick()
