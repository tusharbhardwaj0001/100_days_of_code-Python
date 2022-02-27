import turtle as t
import random
tom = t.Turtle()

colour = ["yellow", "Red", "Black", "Blue", "Green", "grey", "Orange"]
angle = [0,90,180,270]
tom.pensize(5)
tom.speed('fastest')
for _ in range(200):
    tom.color(random.choice(colour))
    tom.forward(30)
    #c = random.randint(1,10)
    #if c%2 == 0:
    #    tom.right(random.choice(angle))
    #else:
    #    tom.left(random.choice(angle))
    tom.setheading(random.choice(angle))

screen = t.Screen()
screen.exitonclick()
