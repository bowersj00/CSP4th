from PIL import Image
import turtle

# resizing code from https://opensource.com/life/15/2/resize-images-python
basewidth = 100
img = Image.open('ezgif-5-e2a6dd25fca2.gif')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('ezgif-5-e2a6dd25fca2.gif')

basewidth = 40
img = Image.open('ezgif-2-5860fd7e3b2a.gif')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('ezgif-2-5860fd7e3b2a.gif')
#
apple='ezgif-2-5860fd7e3b2a.gif'
pirate='ezgif-5-e2a6dd25fca2.gif'

drawer=turtle.Turtle()
drawer.speed(0)

wn = turtle.Screen()
wn.addshape(pirate)
wn.addshape(apple)

"""
Info For Shirts
Center lines 1(-184.29) and 2(175.71)
Left bounds 1(-279.29) and 2(80.71)
Right bounds 1(-89.29) and 2(270.71)
Midline 1&2(-85.36)
Pit line 1&2(14.64)
Bottom line 1&2(-185.36)
"""

def shirt():
    #right arm
    drawer.forward(100)
    #top
    drawer.right(45)
    drawer.forward(45)
    drawer.right(90)
    drawer.circle(50,180)
    drawer.right(90)
    drawer.forward(45)
    drawer.right(45)
    #left arm
    drawer.forward(100)
    drawer.right(90)
    drawer.forward(75)
    drawer.right(90)
    drawer.forward(25)
    drawer.left(135)
    #body
    drawer.forward(200)
    drawer.right(90)
    drawer.forward(190)
    drawer.right(90)
    drawer.forward(200)
    drawer.left(135)
    drawer.forward(25)
    #finnish right arm
    drawer.right(90)
    drawer.forward(75)
def background():
    #Main

    #Background Shirt 1
    drawer.penup()
    drawer.goto(-350,50)
    drawer.pendown()
    drawer.left(45)
    shirt()
    #Background Shirt 2
    drawer.penup()
    drawer.goto(10,50)
    drawer.pendown()
    drawer.right(90)
    shirt()

    #Horizontal Ruler
    drawer.penup()
    drawer.goto(-400,150)
    drawer.setheading(0)
    drawer.pendown()
    while drawer.xcor()<=350:
        drawer.right(90)
        drawer.forward(15)
        drawer.write(int(drawer.xcor()))
        drawer.right(180)
        drawer.forward(15)
        drawer.right(90)
        drawer.penup()
        drawer.forward(50)
        drawer.pendown()
    #Vertical Ruler
    drawer.penup()
    drawer.goto(-400,150)
    drawer.setheading(270)
    drawer.pendown()
    while drawer.ycor()>=-200:
        drawer.left(90)
        drawer.forward(15)
        drawer.write(int(drawer.ycor()))
        drawer.right(180)
        drawer.forward(15)
        drawer.left(90)
        drawer.penup()
        drawer.forward(50)
        drawer.pendown()
def design():
    # Design Start
    drawer.penup()
    drawer.shape(pirate)
    drawer.goto(-184.29,-65.36)
    drawer.stamp()
    drawer.shape("triangle")
    drawer.goto(-244.29,-85.36)
    drawer.pendown()
    drawer.setheading(90)
    drawer.fillcolor("grey")
    drawer.begin_fill()
    drawer.circle(-15,90)
    drawer.forward(50)
    position=drawer.xcor()
    drawer.forward(50)
    drawer.circle(-15,90)
    drawer.forward(50)
    drawer.circle(-15,90)
    drawer.forward(100)
    drawer.circle(-15,90)
    drawer.forward(50)
    drawer.penup()
    drawer.end_fill()
    drawer.shape(apple)
    drawer.goto(position,-110)
    drawer.stamp()
    drawer.shape("triangle")

    drawer.goto(-184.29,0)
    drawer.write("PATTONVILE CSD", move=False, align="center", font=("Times", 20, "italic"))

    drawer.goto(175.71,0)
    drawer.write("COMPUTER SCIENCE", move=False, align="center", font=("Times", 16, "bold"))

    drawer.goto(175.71,-10)
    drawer.write("One if at a time...", move=False, align="center", font=("Halvetica", 10, "normal"))

    drawer.goto(175.71,-150)
    drawer.write(" 01001110 01101111 01110111 \n 00100000 01110111 01101000 \n 01111001 00100000 01110111 \n 01101111 01110101 01101100 \n 01100100 00100000 01111001 \n 01101111 01110101 00100000 \n 01110100 01110010 01100001 \n 01101110 01110011 01101100 \n 01100001 01110100 01100101 \n 00100000 01110100 01101000 \n 01101001 01110011 00111111 ", move=True, align="center", font=("Arial", 10, "normal"))

    drawer.hideturtle()
background()
design()

wn.mainloop()