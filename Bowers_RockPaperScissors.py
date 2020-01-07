import random

def play(games):
    i=games
    player_wins=0
    computer_wins=0
    while i>0:
        player_choice=int(input("Rock (1), Paper (2), or Scissors (3)? "))
        chooser=random.randint(1,3)
        if chooser==1:
            comp_choice= "Rock"
            if player_choice==1:
                print("You picked Rock. \nComputer picked Rock.\nIt's A Tie!")
            elif player_choice==2:
                print("You picked Paper. \nComputer picked Rock.\nPlayer Wins!")
                player_wins+=1
                i-=1
            elif player_choice==3:
                print("You picked Scissors. \nComputer picked Rock.\nYou Lose :(")
                computer_wins+=1
                i-=1
        elif chooser==2:
            comp_choice= "Paper"
            if player_choice==1:
                print("You picked Rock. \nComputer picked Paper.\nYou Lose :(")
                computer_wins+=1
                i-=1
            elif player_choice==2:
                print("You picked Paper. \nComputer picked Paper.\nIt's A Tie!")
            elif player_choice==3:
                print("You picked Scissors. \nComputer picked Paper.\nPlayer Wins!")
                player_wins+=1
                i-=1
        elif chooser==3:
            comp_choice= "Scissors"
            if player_choice==1:
                print("You picked Rock. \nComputer picked Scissors.\nPlayer Wins!")
                player_wins+=1
                i-=1
            elif player_choice==2:
                print("You picked Paper. \nComputer picked Scissors.\nYou Lose :(")
                computer_wins+=1
                i-=1
            elif player_choice==3:
                print("You picked Scissors. \nComputer picked Scissors.\nIt's A Tie!")
        if player_wins>=((games/2)+(1/2)) or computer_wins>=((games/2)+(1/2)):
            if player_wins>computer_wins:
                print("Player wins the game!")
            else:
                print("Computer wins the game!")
            break
games=int(input("Best out of how many games? (Enter an odd number) "))
play(games)