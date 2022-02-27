from turtle import Turtle, Screen
mine_turtle = Turtle()

#mine_turtle.shape("turtle")
for _ in range(10):
    mine_turtle.forward(10)
    mine_turtle.penup()
    mine_turtle.forward(10)
    mine_turtle.pendown()



screen = Screen()
screen.exitonclick()
