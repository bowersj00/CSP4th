"""1. Make rows and collums of boxes on user request
2. number said rows and boxes
3. Make the whole thing checkerboard colored"""
import turtle as trtl
drawer=trtl.Turtle()

drawer.left(180)
drawer.color("green")\

def make_box(box_num,fill):
    if fill==True:
        drawer.fillcolor("black")
        drawer.begin_fill()
        i=0
        while i<4:
            drawer.forward(50)
            drawer.right(90)
            i+=1
        drawer.forward(50)
        drawer.end_fill()
    else:
        i=0
        while i<4:
            drawer.forward(50)
            drawer.right(90)
            i+=1
        drawer.forward(50)

    drawer.penup()
    drawer.goto(drawer.xcor()+20,drawer.ycor()+20)
    drawer.pendown()
    drawer.write(box_num)
    drawer.penup()
    drawer.goto(drawer.xcor()-20,drawer.ycor()-20)
    drawer.pendown()

def table_maker(rows,columns):
    rows_left=rows
    columns_left=columns
    box_num=(rows*columns-1)
    fill=False
    print("Making table with",rows,"rows and",columns,"columns!")
    while columns_left>0:
        drawer.penup()
        drawer.goto(0,0-(50*columns_left))
        drawer.pendown()
        if columns_left%2==0:
            fill=True
        else:
            fill=False
        while rows_left>0:
            if fill==True:
                fill=False
            else:
                fill=True
            make_box(box_num,fill)
            rows_left-=1
            box_num-=1
        rows_left=rows
        columns_left-=1

rows=int(input("How many rows? "))
columns=int(input("How many columns? "))

table_maker(rows,columns)


wn = trtl.Screen()
wn.mainloop()