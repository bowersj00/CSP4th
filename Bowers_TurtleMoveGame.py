import turtle , random

def game_input():
    global hard_mode , insane
    print("\nWelcome to the game!\n\nIn this game your objective is to collect as many turtles as possible (there are 25 possible points)!\nUse right and left arrow keys to move and space to jump!")
    mode=input("\nEnter either 1, 2, or 3 (easy mode, hard mode, or insane mode) then hit enter to start the Game!\n")
    global insane
    if mode=="1":
        hard_mode=False
        insane=False
    elif mode=="2":
        hard_mode=True
        insane=False
    elif mode=="3":
        hard_mode=True
        insane=True
    else:
        game_input()
game_input()

screen=turtle.Screen()
global insane
if insane==True:
    screen.bgpic("illusion.png")
else:
    screen.bgpic("sky.png")

mover=turtle.Turtle()

def setup():
    global score_drawer , insane
    mover.speed(0)
    if insane!=True:
        mover.goto(-200,0)
        mover.begin_fill()
        mover.forward(400)
        mover.right(90)
        mover.forward(50)
        mover.right(90)
        mover.forward(400)
        mover.right(90)
        mover.forward(50)
        mover.end_fill()
    mover.penup()
    mover.goto(0,0)
    mover.color("Blue")

    score_drawer=turtle.Turtle()
    score_drawer.hideturtle()
    score_drawer.penup()
    score_drawer.speed(0)
    score_drawer.goto(200,250)
    score_drawer.write("Score: ")

    global gravity , mover_xspeed , mover_yspeed , go_up , go_side , score , turtles_left , game_over , hard_mode
    gravity=3
    mover_xspeed=40
    mover_yspeed=0
    go_up=True
    go_side=True
    score=0
    turtles_left=25
    game_over=False

global gravity , mover_xspeed , mover_yspeed , go_up , go_side , score , turtles_left , game_over
setup()

def end_game():
    global score , game_over
    screen.clearscreen()
    score_drawer=turtle.Turtle()
    score_drawer.hideturtle()
    score_drawer.penup()
    score_drawer.goto(-200,0)
    score_drawer.speed(0)
    score_drawer.write("YOUR FINAL SCORE WAS: "+str(score), font=("Arial", 30, "normal"))
    game_over=True

def update_score():
    global score_drawer
    score_drawer.clear()
    score_drawer.write("Score: "+str(score), font=("Arial", 20, "normal"))

def reset_obstacle():
    global turtles_left
    if turtles_left!=0:
        obstacle.hideturtle()
        obstacle.shape(random.choice(turtle_shapes))
        obstacle.turtlesize(random.choice(turtle_sizes))
        obstacle.goto(300,random.randint(50,150))
        obstacle.showturtle()
        turtles_left-=1
    else: end_game()

def left():
    global go_up , go_side
    go_up=False
    if mover.xcor()>-190 and round(mover.xcor())%40==0 and go_side==True:
        mover.speed(1)
        mover.back(mover_xspeed)
        mover.speed(0)
    go_up=True

def right():
    global go_up , go_side
    go_up=False
    if mover.xcor()<200 and round(mover.xcor())%40==0 and go_side==True:
        mover.setheading(0)
        mover.speed(1)
        mover.forward(mover_xspeed)
        mover.speed(0)
    go_up=True

def up():
    global mover_yspeed
    mover.setheading(90)
    mover.forward(mover_yspeed)

def acceleration():
    global gravity , mover_yspeed , go_up , go_side , score
    go_side=False
    if go_up==True:
        mover_yspeed=30
        while True:
            go_up=False
            up()
            xs, ys, ws=obstacle.turtlesize()
            if abs(mover.xcor()-obstacle.xcor())<(12*xs) and abs(mover.ycor()-obstacle.ycor())<(12*ys):
                if game_over==False:
                    score+=1
                    update_score()
                    reset_obstacle()
            mover_yspeed=mover_yspeed-gravity 
            while mover.ycor()<0:
                mover.goto(mover.xcor(),mover.ycor()+10)
            if mover.ycor()+10>0 and mover.ycor()-10<0:
                mover.goto(mover.xcor(),0)
                break
        go_up=True
        mover_yspeed=30
        mover.setheading(0)
    go_side=True

screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(acceleration, "space")

screen.listen()

obstacle=turtle.Turtle()

obstacle.speed(0)
obstacle.penup()
obstacle.setheading(180)

turtle_sizes=[.5,1,1.5,2]
turtle_shapes=["square","circle","turtle","classic"]

while not game_over:
    reset_obstacle()
    while obstacle.xcor()>-250:
        if hard_mode==True: obstacle.forward(10)
        else: obstacle.forward(5)

screen.mainloop()