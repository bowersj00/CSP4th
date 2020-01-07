"""1. Make rows and collums of boxes on user request
2. number said rows and boxes
3. Make the whole thing checkerboard colored"""
import turtle as trtl

def table_maker(rows,columns):
	print(rows,columns)



rows=int(input("How many rows? "))
columns=int(input("How many columns? "))

table_maker(rows,columns)


wn = trtl.Screen()
wn.mainloop()