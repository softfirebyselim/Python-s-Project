

from re import A
import turtle

a = turtle

a.bgcolor("white")
a.speed(1)

width = 400
height = 200

a.up()
a.goto(-width //2 , height//2)
a.down()
a.color("black", "green")
a.begin_fill()
for i in range(4):
    a.fd(width //2)
    a.right(90)
a.end_fill()


a.up()

a.goto(0, height//2)
a.down()
a.color("black", "white")
a.begin_fill()
for i in range(4):
    a.fd(width//2)
    a.right(90)
a.end_fill()

a.color("red" ,"red")
a.left(120)
a.up()
a.goto(65, 40)
a.down()
a.begin_fill()
a.circle(80, 300)
a.right(10)
a.circle(61, -285)
a.end_fill()
a.up()


a.goto(0,10)
a.down()
a.setheading(0)
a.right(15)
a.begin_fill()
for i in range(5):
    a.fd(40)
    a.right(144)
a.end_fill()


a.done()