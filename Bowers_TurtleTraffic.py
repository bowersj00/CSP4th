#   a117_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
def tcheck(ht,vt):
    if ht.xcor()!=(vt.xcor()-10) and ht.ycor()!=(vt.ycor()-10):
            ht.forward(1)
            vt.forward(1)
            tcheck(ht,vt)
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    #Sets location color and shape of turtles in horizontal
	ht = trtl.Turtle(shape=s)
	horiz_turtles.append(ht)
	ht.penup()
	new_color = horiz_colors.pop()
	ht.fillcolor(new_color)
	ht.goto(-350, tloc)
	ht.setheading(0)
    #Sets vertical turles
	vt = trtl.Turtle(shape=s)
	vert_turtles.append(vt)
	vt.penup()
	new_color = vert_colors.pop()
	vt.fillcolor(new_color)
	vt.goto( -tloc, 350)
	vt.setheading(270)
    #Changes implicit location of each turtle
	tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 6:
        ht=horiz_turtles.pop()
        vt=vert_turtles.pop()
        tcheck(ht,vt)
        steps = steps + 1


wn = trtl.Screen()
wn.mainloop()