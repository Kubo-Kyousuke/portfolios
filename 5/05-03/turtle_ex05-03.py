#turtle_ex05-03.py
import turtle
import random

turtle.setup(800,800,0,0)
turtle.delay(0)


class MyPen:
    def __init__(self,my_size,x,y,my_color):
        self.pointx=x
        self.pointy=y
        self.pen=turtle.Turtle()
        self.pen.hideturtle
        self.size=my_size
        self.pen.color(my_color)
        self.pen.pencolor(my_color)

def main():
    p1=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'red')
    p2=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'blue')
    p3=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'pink')
    p4=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'gold')
    p5=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'green')
    p6=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'purple')
    p7=MyPen(random.randint(20,50),random.randint(-350,350),random.randint(-350,350),'yellow')

    p1.pen.penup()
    p1.pen.forward(p1.pointx)
    p1.pen.left(90)
    p1.pen.forward(p1.pointy)
    p1.pen.pendown()
    p1.pen.hideturtle
    p1.pen.begin_fill()
    p1.pen.circle(p1.size)
    p1.pen.end_fill()

    p2.pen.penup()
    p2.pen.forward(p2.pointx)
    p2.pen.left(90)
    p2.pen.forward(p2.pointy)
    p2.pen.pendown()
    p2.pen.hideturtle
    p2.pen.begin_fill()
    p2.pen.circle(p2.size)
    p2.pen.end_fill()

    p3.pen.penup()
    p3.pen.forward(p3.pointx)
    p3.pen.left(90)
    p3.pen.forward(p3.pointy)
    p3.pen.pendown()
    p3.pen.hideturtle
    p3.pen.begin_fill()
    p3.pen.circle(p3.size)
    p3.pen.end_fill()

    p4.pen.penup()
    p4.pen.forward(p4.pointx)
    p4.pen.left(90)
    p4.pen.forward(p4.pointy)
    p4.pen.pendown()
    p4.pen.hideturtle
    p4.pen.begin_fill()
    p4.pen.circle(p4.size)
    p4.pen.end_fill()

    p5.pen.penup()
    p5.pen.forward(p5.pointx)
    p5.pen.left(90)
    p5.pen.forward(p5.pointy)
    p5.pen.pendown()
    p5.pen.hideturtle
    p5.pen.begin_fill()
    p5.pen.circle(p5.size)
    p5.pen.end_fill()

    p6.pen.penup()
    p6.pen.forward(p6.pointx)
    p6.pen.left(90)
    p6.pen.forward(p6.pointy)
    p6.pen.pendown()
    p6.pen.hideturtle
    p6.pen.begin_fill()
    p6.pen.circle(p6.size)
    p6.pen.end_fill()

    p7.pen.penup()
    p7.pen.forward(p7.pointx)
    p7.pen.left(90)
    p7.pen.forward(p7.pointy)
    p7.pen.pendown()
    p7.pen.hideturtle
    p7.pen.begin_fill()
    p7.pen.circle(p7.size)
    p7.pen.end_fill()
    turtle.done()

if __name__=="__main__":
    main()

