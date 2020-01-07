import turtle
screen=turtle.Screen()

def f(direction):
    print("here")
screen.onkey(f(1), "Up")
screen.listen()
screen.mainloop()