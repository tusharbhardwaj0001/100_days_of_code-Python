from turtle import Turtle, Screen

mine_turtle = Turtle()
mine_turtle.shape("turtle")
mine_turtle.color("Black", "yellow")

mine_turtle.begin_fill()
for _ in range(4):
    mine_turtle.forward(100)
    mine_turtle.left(90)
mine_turtle.end_fill()

screen = Screen()
screen.exitonclick()
