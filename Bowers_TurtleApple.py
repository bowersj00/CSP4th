import turtle as trtl , random
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
apple.speed(1)

drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

letter_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def draw_apple():
  print("here")
  apple.clear()
  drawer.clear()
  apple.shape(apple_image)
  apple.speed(0)
  apple.goto(random.randint(-200,200),random.randint(0,150))
  apple.speed(1)
  wn.tracer(False)
  drawer.goto(apple.xcor()-15,apple.ycor()-35)
  draw_letter(random.choice(letter_list))
  wn.update()

def move_apple(apple):
  apple.goto(apple.xcor(),-310)

# This function takes care of font and color.
def draw_letter(letter):
  drawer.color("white")
  drawer.write(letter, font=("Arial", 50, "bold")) 

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.

wn.onkeypress(draw_apple)

wn.listen()
wn.mainloop()