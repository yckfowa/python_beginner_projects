import turtle

ca = turtle.Turtle()

ca.speed(9)
turtle.title("Captain America")
turtle.bgcolor("#f0f0f0")

ca.penup()
ca.setpos(0,-200)
ca.pendown()
ca.begin_fill()
ca.circle(200)
ca.fillcolor("#ec2004")
ca.end_fill()

ca.penup()
ca.setpos(0,-160)
ca.pendown()
ca.begin_fill()
ca.circle(160)
ca.fillcolor("#aeb7c2")
ca.end_fill()

ca.penup()
ca.setpos(0,-120)
ca.pendown()
ca.begin_fill()
ca.circle(120)
ca.fillcolor("#ec2004")
ca.end_fill()

ca.penup()
ca.setpos(0,-80)
ca.pendown()
ca.begin_fill()
ca.circle(80)
ca.fillcolor("#002d5c")
ca.end_fill()

ca.penup()
ca.setpos(-20,30)
ca.pendown()
ca.begin_fill()
for i in range(5):
    ca.left(60)
    ca.forward(53)
    ca.right(133)
    ca.forward(53)
ca.fillcolor("#f0f0f0")
ca.end_fill()

ca.hideturtle()


turtle.done()
