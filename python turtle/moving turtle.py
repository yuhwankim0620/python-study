import turtle

turtle.setup(width = 600, height = 600)
gil = turtle.Turtle()
t = turtle.Turtle()

def draw_gil():
    gil.penup()
    gil.goto(-150, -300)
    gil.pendown()
    gil.pensize(5)
    gil.color("brown")
    gil.begin_fill()
    gil.goto(-150, 300)
    gil.goto(150, 300)
    gil.goto(150, -300)
    gil.goto(-150, -300)
    gil.end_fill()

def object():
    t.shape("turtle")
    t.color("green")
    t.setheading(90)
    xy = [[-75,50],[-75,100],[-75,250] ]
    t.penup()
    t.goto(xy[0])
    t.stamp()
    for x,y in xy :
        t.goto(x,y)
        t.stamp()
draw_gil()
object


