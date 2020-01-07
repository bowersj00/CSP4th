import turtle as trtl

spooder = trtl.Turtle()
spooder.pensize(40)
spooder.circle(20)
spooder.goto(0,-20)
spooder.circle(1)
legs = 8
leg_length = 70
leg_rotate = 360 / legs
spooder.pensize(5)
spooder.setheading(340)
i = 1
while (i < legs+1):
    if i<5:
        leg_rotate=20
        spooder.penup()
        spooder.goto(0,20)
        spooder.pendown()
        spooder.circle(-1*leg_length,leg_length)
        spooder.setheading(leg_rotate*i)
    else:
        leg_rotate=20
        spooder.penup()
        spooder.goto(0,20)
        spooder.pendown()
        spooder.circle(leg_length,leg_length)
        spooder.setheading((leg_rotate*i)+50)
    if i==4:
        spooder.setheading(120)

    i = i + 1
spooder.penup()
spooder.goto(10,-20)
spooder.pendown()
spooder.pencolor("red")
spooder.circle(5)
spooder.penup()
spooder.goto(-10,-20)
spooder.pendown()
spooder.circle(5)
spooder.hideturtle()
wn = trtl.Screen()
wn.mainloop()