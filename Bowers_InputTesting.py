import turtle as trtl

def polygon_num_function():
    polygon_num=input("How many sides should the shape have? ")
    if polygon_num.isdigit() == False:
        print("Please retry side number select. Use only numeric characters")
        polygon_num_function()

def polygon_side_function():
    polygon_side=input("How long should each side be? ")
    if polygon_side.isdigit() == False:
        print("Please retry side length select. Use only numeric characters")
        polygon_side_function()

def polygon_color_function():
    polygon_color=input("What color should the shape be? ")
    if polygon_color.isalpha() == False or polygon_color.islower() == False:
        print("Please retry color select. Use only lowercase, alphabetic characters")
        polygon_color_function()

drawer = trtl.Turtle()
drawer.pendown()
drawer.speed(0)

polygon_num=input("How many sides should the shape have? ")
if polygon_num.isdigit() == False:
    print("Please retry side number select. Use only numeric characters")
    polygon_num_function()

polygon_side=input("How long should each side be? ")
if polygon_side.isdigit() == False:
    print("Please retry side length select. Use only numeric characters")
    polygon_side_function()

polygon_color=input("What color should the shape be? ")


drawer.begin_fill()
drawer.fillcolor(polygon_color)
drawer.color(polygon_color)
drawer.circle(int(polygon_side),360,int(polygon_num))
drawer.end_fill()

drawer.penup()
drawer.goto(-500,-500)
wn = trtl.Screen()
wn.mainloop()