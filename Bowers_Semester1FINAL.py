import turtle

pen=turtle.Turtle()
pen.penup()
pen.goto(-300,125)
pen.speed(0)
#size is fifty pix
pen.pendown()

for i in range(1,5):
    j=0
    while j<4:
        pen.forward(50*i)
        pen.right(90)
        j+=1

pen.penup()
pen.goto(150,-200)
pen.pendown()
pen.fillcolor("brown")
pen.begin_fill()
pen.forward(30)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(400)
pen.end_fill()
pen.penup()
pen.goto(115,175)
pen.fillcolor("green")
pen.begin_fill()
pen.left(30)
pen.circle(50,360,3)
pen.end_fill()

pen2=turtle.Turtle()
pen2.penup()
pen2.goto(0,200)
pen2.speed(3)
pen2.shape("turtle")
pen2.turtlesize(1)

def turn(x,y):
    pen2.left(360)

pen2.onclick(turn)

def change_color(color):
    if color=="r":
        pen2.color("red")
    if color=="b":
        pen2.color("blue")
    if color=="g":
        pen2.color("green")
    if color=="c":
        pen2.color("black")

turtle.onkeypress(lambda:change_color("r"),"r")
turtle.onkeypress(lambda:change_color("b"),"b")
turtle.onkeypress(lambda:change_color("g"),"g")
turtle.onkeypress(lambda:change_color("c"),"c")

global size
size=1

def change_size():
    global size
    if size==5:
        size=1
    else:
        size+=1  
    pen2.turtlesize(size)
    
    
turtle.onkeypress(change_size,"space")

turtle.listen()

wn = turtle.Screen()
wn.mainloop()