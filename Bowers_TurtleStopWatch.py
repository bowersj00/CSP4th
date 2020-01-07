import turtle

screen=turtle.Screen()

start_button=turtle.Turtle()

start_button.color("green")
start_button.shape("square")
start_button.speed(0)
start_button.turtlesize(3)
start_button.penup()

reset_button=turtle.Turtle()

reset_button.color("yellow")
reset_button.shape("square")
reset_button.speed(0)
reset_button.turtlesize(3)
reset_button.penup()

stop_button=turtle.Turtle()

stop_button.color("red")
stop_button.shape("square")
stop_button.speed(0)
stop_button.turtlesize(3)
stop_button.penup()

start_button.goto(-120,-50)
reset_button.goto(-25,-50)
stop_button.goto(80,-50)

start_button.color("Black")
start_button.write("Start", move=False, align="left", font=("Arial", 20, "normal"))
start_button.goto(-100,-100)
start_button.color("Green")

reset_button.color("Black")
reset_button.write("Reset", move=False, align="left", font=("Arial", 20, "normal"))
reset_button.goto(0,-100)
reset_button.color("Yellow")

stop_button.color("Black")
stop_button.write("Stop", move=False, align="left", font=("Arial", 20, "normal"))
stop_button.goto(100,-100)
stop_button.color("Red")



global clock_interval , clock_on , current_count
clock_interval=1000
clock_on=False
current_count=0

time_turtle=turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.goto(-50,100)

def clock_change():
    global clock_on , current_count
    
    if clock_on==True:
        print("Got Here")
        time_turtle.clear()
        time_turtle.write("Timer: " + str(current_count))
        current_count+=1
        time_turtle.getscreen().ontimer(clock_change, clock_interval)

def clock_start(x,y):
    global clock_on , current_count
    print("timer started")
    clock_on=True

def clock_reset(x,y):
    global clock_on , current_count
    print("timer reset")
    current_count=0
    clock_on=True

def clock_stop(x,y):
    global clock_on , current_count
    print("timer stopped")
    clock_on=False


start_button.onclick(clock_start)
reset_button.onclick(clock_reset)
stop_button.onclick(clock_stop)

screen.ontimer(clock_change, clock_interval)

screen.mainloop()