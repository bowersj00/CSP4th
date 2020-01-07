#   a113_square.py
#   Write code to draw a square.
import turtle as trtl

drawer = trtl.Turtle()
drawer.pendown()
drawer.speed(0)
drawer.pensize(2)
#set of rainbow colors and handler variable
colors=["red","orange","yellow","green","blue","indigo","violet"]
color_set=0
# Algorithm to draw spiral patern
fibbonacci=[1,1]
stage=0
step=0
while step<18:
    drawer.penup()
    drawer.goto(0,0)
    drawer.right(20)
    drawer.pendown()
    drawer.color(colors[color_set])
    #itterations to draw semi circles using the fibonacci numbers (fibonacci spiral)
    while stage<12:
        fibbonacci.append(fibbonacci[stage]+fibbonacci[stage+1])
        drawer.circle(2*fibbonacci[stage],90)

        stage+=1
    stage=0
    step+=1
    #catch to keep color_set from going to high
    if color_set==6:
        color_set=0
    else:
        color_set+=1
#reset
drawer.penup()
drawer.goto(0,0)
drawer.pendown()
# Reciprocal algorithm for opposite spiral
stage=0
step=0
while step<18:
    drawer.penup()
    drawer.goto(0,0)
    drawer.right(20)
    drawer.pendown()
    drawer.color(colors[color_set])
    while stage<12:
        fibbonacci.append(fibbonacci[stage]+fibbonacci[stage+1])
        drawer.circle(-2*fibbonacci[stage],90)

        stage+=1
    stage=0
    step+=1
    if color_set==6:
        color_set=0
    else:
        color_set+=1
#encompassing circle
drawer.color("black")
drawer.right(13.5)
drawer.circle(-2*173)

drawer.penup()
drawer.goto(500,300)
drawer.pendown()
drawer.circle(5)
drawer.penup()
drawer.goto(530,300)
drawer.pendown()
drawer.circle(5)
drawer.penup()
drawer.goto(490,280)
drawer.pendown()
drawer.right(22)
drawer.circle(50,60)

drawer.penup()
drawer.goto(-500,-500)
wn = trtl.Screen()
wn.mainloop()