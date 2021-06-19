# Amaranth Red (#D12531), Alice Blue (#F4F9FF) and Chinese Black (#101010).
import turtle

d = turtle.Turtle()
d.speed(9)
turtle.title("Deadpool")
turtle.bgcolor('#20252C')
d.fillcolor("#D12531")
d.begin_fill()
d.penup()
d.setpos(0,-200)
d.pendown()
d.circle(200)
d.end_fill()

def black_circle():
    d.fillcolor("#101010")
    d.begin_fill()
    d.circle(160, -160)
    d.end_fill()


d.color("#D12531")
d.penup()
d.goto(0, -160)
d.pendown()
d.circle(160, -10)
black_circle()

d.penup()
d.setpos(25, 160)
d.pendown()
d.rt(20)
black_circle()

def right_eye(a):
    d.color("#101010")
    d.begin_fill()
    d.goto(a * 40, 0)
    d.color('#F4F9FF')
    d.pendown()
    d.rt(60)
    d.circle(50,70)
    d.lt(20)
    d.circle(80,55)
    d.goto(a * 40, 0)
    d.end_fill()
    d.penup()

def left_eye(b):
    d.penup()
    d.goto(b * 40, 0)
    d.pendown()
    d.color("#101010")
    d.begin_fill()
    d.color('#F4F9FF')
    d.pendown()
    d.lt(20)
    d.goto(b*120,50)
    d.rt(20)
    d.seth(270)
    d.circle(80,55)
    d.lt(20)
    d.circle(50,55)
    d.goto(b * 40, 0)
    d.end_fill()
    d.penup()


right_eye(1)
left_eye(-1)

d.goto(-240,-325)
d.color("#D12531")
d.write("DEADPOOL",font=(
      "Verdana", 80, "bold"))
d.hideturtle()

turtle.done()
