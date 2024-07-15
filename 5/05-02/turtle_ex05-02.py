#turtle_ex05-02.py
import turtle

turtle.setup(800,800,0,0)
turtle.delay(0)
x=0.0001
turtle01 = turtle.Turtle()
for i in range(200):
    for i in range(360):
        turtle01.forward(x)
        turtle01.right(1)
        x+=0.0001

turtle.done()