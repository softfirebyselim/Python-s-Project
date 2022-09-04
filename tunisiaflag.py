import turtle


f =turtle

x,y = 262,162
t = [(x, -y),(x,y),(-x,y), (-x,-y)]
f.bgcolor("black")
f.width(3)
f.ht()


f.goto(-x,-y)
f.color("#e70013")
f.begin_fill()
for i in range(4):
    f.goto(t[i])
f.end_fill()


f.home()
f.color("white")
f.begin_fill()
f.fd(92)
f.seth(90)
f.circle(92)
f.end_fill()


f.goto(66, 0)
f.color("#e70013")
f.begin_fill()
f.circle(66)
f.end_fill()

f.color("white")
f.begin_fill()
f.goto(81, 0)
f.circle(59)
f.end_fill()


f.goto(-6, -20)
f.seth(48)
f.color("#e70013")
f.begin_fill()
for i in range(5):
    f.fd(75)
    f.rt(144)
f.end_fill()

f.done()

