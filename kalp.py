import turtle

def mini():
    t.color("red") 
    t.begin_fill()
    t.fillcolor("red") 
    t.right(230)
    t.forward(25)
    for i in range(9):
        t.right(20)
        t.forward(3)
    t.forward(3)
    t.right(225)
    for i in range(9):
        t.right(20)
        t.forward(3)
    t.right(35)
    t.forward(27)
    t.end_fill()

def draw_B_in_heart():
    t.penup()
    t.goto(0, 50)  
    t.pendown()
    t.color("white")  
t = turtle.Turtle()
s = turtle.Screen()


t.hideturtle()
t.speed(0)
s.bgcolor("black") 

t.setheading(0)
t.penup()
t.goto(0,-50)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(25,-15)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-25,-15)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-50,20)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(0,20)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(50,20)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(75,55)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(25,55)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-25,55)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-75,55)
t.pendown()
mini()


t.setheading(0)
t.penup()
t.goto(-100,90)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-50,90)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(0,90)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(50,90)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(100,90)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(125,125)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(75,125)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(25,125)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-25,125)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-75,125)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-125,125)
t.pendown()
mini()


t.setheading(0)
t.penup()
t.goto(-100,160)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-50,160)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(50,160)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(100,160)
t.pendown()
mini()


t.setheading(0)
t.penup()
t.goto(75,195)
t.pendown()
mini()

t.setheading(0)
t.penup()
t.goto(-75,195)
t.pendown()
mini()

draw_B_in_heart()

turtle.done()

