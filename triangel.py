import imp


import turtle
import colorsys


tr = turtle.Turtle()
tr.screen.bgcolor("black")

tr.penup()
tr.goto(-200, -100)
tr.pendown()
tr.speed(0)

a = 400
h = 0
n =100


def trianglepy():
    global a,h,n
    for i in range(40):
        c= colorsys.hsv_to_rgb(h, 1,0.6)
        h = h+(1/n)
        tr.color(c)
        tr.forward(a)
        tr.left(120)
        a=a-10

trianglepy()
trianglepy()


tr.hideturtle()
turtle.done