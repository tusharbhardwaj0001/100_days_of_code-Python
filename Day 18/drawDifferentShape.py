import turtle as t
import random
mTurtle = t.Turtle()
mTurtle.shape("turtle")
colour = ["blue", "Yellow", "Red", "Green", "Black"]
"""
def traingle():
    for _ in range(3):
        mTurtle.forward(100)
        mTurtle.right(120)

def square():
    for _ in range(4):
        mTurtle.forward(100)
        mTurtle.right(90)

def pentagon():
    for _ in range(5):
        mTurtle.forward(100)
        mTurtle.right(72)

def hexagon():
    for _ in range(6):
        mTurtle.forward(100)
        mTurtle.right(60)

def heptagon():
    for _ in range(7):
        mTurtle.forward(100)
        mTurtle.right(51.4285)

def octagon():
    for _ in range(8):
        mTurtle.forward(100)
        mTurtle.right(45)

mTurtle.color("orange", "Red")
mTurtle.begin_fill()
traingle()
square()
pentagon()
hexagon()
heptagon()
octagon()
mTurtle.end_fill()
"""
def drawShape(noOfEdge):
    angle = 360/noOfEdge
    for _ in range(noOfEdge):
        mTurtle.forward(100)
        mTurtle.right(angle)

for noOfEdge in range(3,11):
    mTurtle.color(random.choice(colour), random.choice(colour))
    drawShape(noOfEdge)
    noOfEdge += 1

screen = t.Screen()
screen.exitonclick()
