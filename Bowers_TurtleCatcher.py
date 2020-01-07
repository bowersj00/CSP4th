import turtle , random
import leaderboard as lb

leaderboard_file_name="Bowers_CatcherLeaderboard.txt"
leader_names_list=[]
leader_scores_list=[]
player_name=input("What is your name? (Be advised: game will commence as soon as you click the first shape in the center of the screen.)\n")

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global spot
    spot=turtle.Turtle()
    #load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
    #TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

screen=turtle.Screen()

print("Sign field trip form")

catch=turtle.Turtle()
counter=turtle.Turtle()
scorer=turtle.Turtle()

color_list=["blue","red","green","yellow","orange","indigo","violet","black"]
size_list=[.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

catch.color(random.choice(color_list))
catch.shape("circle")
catch.speed(0)
catch.turtlesize(random.choice(size_list))
catch.penup()

counter.penup()
counter.hideturtle()
counter.goto(250,250)

scorer.penup()
scorer.hideturtle()
scorer.goto(250,240)

global score , time_out , timer , count_interval
score=0
time_out=False
timer=20
count_interval=1000

def changer():
    catch.color(random.choice(color_list))
    catch.shape("circle")
    catch.speed(0)
    catch.turtlesize(random.choice(size_list))

def caught(x,y):
    global score , time_out , timer
    if time_out==False:
        score+=1
        #print("Turtle was caught at (",x,",",y,").")
        scorer.clear()
        scorer.write("Your score is: "+str(score))
        move()
        changer()
        
    else:catch.hideturtle()
    
def start_clock():
    global timer, time_out
    counter.clear()
    if timer <= 0:
        counter.write("Time has run out")
        time_out = True
        catch.hideturtle()
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer))
        timer -= 1
        counter.getscreen().ontimer(start_clock, count_interval)

def move():
    catch.hideturtle()
    catch.goto(random.randrange(-250,250),random.randrange(-250,250))
    catch.showturtle()

catch.onclick(caught)

screen.ontimer(start_clock, count_interval) 
screen.mainloop()