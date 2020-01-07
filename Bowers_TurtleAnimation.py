"""
Instructions:
Design at least two images with turtle that represent your school year so far. No abstractions.

Challenge:
Add animations to give life to your project

Concept:
1. Me doing notes by lamp light in the living room
    a. living room background
    b. lamp shining
    c. me sitting on couch
    d. book on table
    e. pencil moving
    f. dog by feet
    g. challenge: create night scene outside
2. Me sitting and playing piano during sectionals with the viola gang
    a. practice room background
    b. piano at center
    c. piano bench i'm sitting on
    d. me sitting in front of it
    e. other violas standing around
    f. music notes coming from piano and jiving off the screen
    g. challenge: music plays over drawing

Daily Tasks:
    9/17: create project, plan drawings
    9/19: start scene one, comlete task a maybe b
    9/20: complete tasks c-f
    9/21 & 9/22: complete scene 1, add transition button, complete scene 2 task a-c
    9/23: complete scene 2 task d and e
    9/24: comlete scene 2, debug and refine
"""
import turtle , random
from PIL import Image

screen=turtle.Screen()
pen=turtle.Turtle()

pen.speed(0)
pen.pensize(5)

global next_scene
next_scene=False

def scene_change(x,y):
    global next_scene
    next_scene=True

screen.onclick(scene_change)

def fwd(dist):
    pen.forward(dist)

def left(deg):
    pen.left(deg)

def right(deg):
    pen.right(deg)

def black_key():
    left(90)
    fwd(4)
    right(90)
    fwd(4)
    right(90)
    fwd(4)
    left(90)

def pianokeys():
    fwd(380)
    left(90)
    fwd(9)
    pen.pensize(1)
    left(90)
    fwd(380)
    pen.setheading(270)
    i=42
    while i>0:
        pen.penup()
        pen.goto(151+(9*i),-120)
        pen.pendown()
        fwd(9)
        i-=1
    pen.penup()
    pen.goto(160,-120)
    pen.pendown()
    pen.setheading(0)
    i=12
    key_set=1
    while i>0:
        if key_set==1:
            fwd(7)
            black_key()
            fwd(5)
            black_key()
            fwd(7)
            key_set=2
        elif key_set==2:
            fwd(7)
            black_key()
            fwd(5)
            black_key()
            fwd(5)
            black_key()
            fwd(7)
            key_set=1
        i-=1

class music_notes:
    registry=[]
    def __init__(self,x_heading,y_heading):
        self.x_heading=x_heading
        self.y_heading=y_heading
        self.registry.append(self)

#positioning
pen.penup()
pen.goto(-400,-50)
pen.pendown()
left(90)
#start of cabinet
fwd(350)
right(90)
fwd(300)
right(90)
fwd(350)
#start of couch
pen.goto(-450,-50)
fwd(50)
    #l side
right(140)
pen.circle(25,270)
pen.setheading(270)
fwd(85)
    #l foot
left(90)
fwd(10)
left(90)
fwd(10)
right(90)
    #bottom
fwd(330)
right(90)
    #r leg
fwd(10)
left(90)
fwd(10)
left(90)
    #r side
fwd(85)
right(140)
pen.circle(25,270)
pen.setheading(90)
fwd(50)
    #bottom cushions
pen.penup()
pen.goto(-115,-150)
pen.setheading(180)
pen.pendown()
fwd(320)
left(90)
fwd(25)
left(90)
fwd(320)
left(90)
fwd(25)
    #top cushions
pen.penup()
pen.goto(-220,-150)
pen.pendown()
fwd(100)
left(90)
fwd(120)
left(90)
fwd(100)
right(90)
fwd(10)
right(90)
fwd(100)
right(90)
fwd(140)
right(90)
fwd(100)
    #rim of couch
pen.back(90)
left(90)
fwd(95)
right(90)
pen.goto(-115,-200)
right(90)
fwd(320)
right(90)
fwd(140)
right(90)
fwd(250)
#cabinet windows
    #outer edge
pen.penup()
pen.goto(-390,-40)
left(90)
pen.pendown()
fwd(330)
right(90)
fwd(280)
right(90)
fwd(330)
right(90)
fwd(280)
    #vertical lines
pen.back(65)
right(90)
fwd(330)
right(90)
fwd(10)
right(90)
fwd(330)
left(90)
fwd(65)
left(90)
fwd(330)
right(90)
fwd(10)
right(90)
fwd(330)
left(90)
fwd(65)
left(90)
fwd(330)
right(90)
fwd(10)
right(90)
fwd(330)
left(90)
    #horizontal lines (by 110)
pen.penup()
pen.goto(-110,15)
pen.pendown()
right(180)
fwd(280)
right(90)
fwd(10)
right(90)
fwd(280)
left(90)
fwd(100)
left(90)
fwd(280)
right(90)
fwd(10)
right(90)
fwd(280)
left(90)
fwd(110)
left(90)
fwd(280)
right(90)
fwd(10)
right(90)
fwd(280)
left(90)
#lamp
pen.penup()
pen.goto(-500,-220)
pen.pendown()
left(90)
fwd(50)
right(90)
fwd(5)
right(90)
fwd(50)
right(90)
fwd(5)
pen.penup()
pen.goto(-527.25,-215)
pen.pendown()
pen.setheading(90)
fwd(300)
left(90)
pen.circle(-75,40)
pen.setheading(0)
fwd(95)
right(320)
pen.circle(75,-40)
#me on couch
pen.penup()
pen.goto(-300,-130)
    #image import
        # resizing code from https://opensource.com/life/15/2/resize-images-python
basewidth = 100
img = Image.open("ezgif-5-64088d89924f.gif")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("ezgif-5-64088d89924f.gif")
justin="ezgif-5-64088d89924f.gif"
    #changing pen
screen.addshape(justin)
pen.shape(justin)
pen.stamp()
#pencil in hand
pen2=turtle.Turtle()
pen2.shape("classic")
basewidth = 5
img = Image.open("pencil.gif")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("pencil.gif")
pencil="pencil.gif"
    #changing pen
screen.addshape(pencil)
pen2.shape(pencil)
pen2.penup()
pen2.goto(-280,-110)
pen2.setheading(0)
while True:
    pen2.speed(0)
    i=40
    while i>0:
        pen2.back(1)
        pen2.right(360)
        i-=1
        if next_scene== True:
            break
    pen2.speed(2)
    pen2.forward(40)
    if next_scene== True:
        break

#Scene 2 start
    #dividing line
pen.shape("classic")
pen.pensize(3)
pen.goto(0,1000)
pen.setheading(270)
pen.pendown()
fwd(2000)
    #piano
pen.penup()
pen.goto(150,-230)
pen.pendown()
pen.setheading(90)
        #left side
fwd(100)
left(90)
fwd(10)
right(90)
fwd(50)
right(90)
fwd(10)
left(90)
fwd(90)
        #top
right(90)
fwd(400)
right(90)
        #right side
fwd(90)
left(90)
fwd(10)
right(90)
fwd(50)
right(90)
fwd(10)
left(90)
fwd(100)
        #legs
right(90)
fwd(15)
right(90)
fwd(100)
left(90)
fwd(370)
left(90)
fwd(100)
right(90)
fwd(15)
pen.back(15)
right(90)
fwd(30)
right(90)
fwd(370)
        #keys and face
pen.penup()
pen.goto(150,-130)
pen.pendown()
fwd(400)
pen.penup()
pen.goto(300,-65)
pen.pendown()
fwd(100)
pen.penup()
pen.goto(150,-80)
pen.pendown()
fwd(10)
right(90)
fwd(49)
left(90)
pianokeys()
        # lid
pen.goto(540,-120)
pen.setheading(90)
pen.pensize(3)
fwd(40)
right(90)
fwd(10)
right(180)
fwd(400)
        #bench
pen.penup()
pen.goto(280,-175)
pen.pendown()
pen.begin_fill()
right(180)
fwd(150)
right(90)
fwd(10)
right(90)
fwd(5)
left(90)
fwd(50)
right(90)
fwd(10)
right(90)
fwd(50)
left(90)
fwd(120)
left(90)
fwd(50)
right(90)
fwd(10)
right(90)
fwd(50)
left(90)
fwd(5)
right(90)
fwd(10)
right(90)
pen.end_fill()
    #me
pen.shape("classic")
basewidth = 120
img = Image.open("sitting.gif")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("sitting.gif")
sitting="sitting.gif"
    #changing pen
screen.addshape(sitting)
pen.shape(sitting)
pen.penup()
pen.goto(350,-90)
pen.stamp()
pen.shape("classic")
    #music notes around me
note_list=[]
i=0
while i<5:
    name=("note",i)
    name=turtle.Turtle()
    note_list.append(name)
    i+=1
for pen in note_list:
    basewidth = 40
    img = Image.open("download.gif")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("download.gif")
    note="download.gif"
    screen.addshape(note)
    pen.shape(note)

for objct in note_list:
    objct.penup()
    objct.goto(random.randrange(150,540),random.randrange(50,100))

next_scene=False

while True:
    for objct in note_list:
        move_x=random.randrange(-15,15)
        move_y=random.randrange(0,15)
        objct.goto(objct.xcor()+move_x,objct.ycor()+move_y)
        if objct.ycor()>=400:
            objct.goto(random.randrange(150,540),random.randrange(50,100))
        if next_scene== True:
            break
    if next_scene== True:
            break

screen.mainloop()