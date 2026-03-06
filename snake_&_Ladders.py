#--------------------------------------------------------
# i am going to create snake and ladders game.
#winning run will be 30.
#there will be 2 players p1 and p2 . 
#and who will reach to 30 first he will be winning person.
#------------------------------------------------------------

import random  #random is being imported to take random values from sydtem

#we will make a dictionaries storing snake and ladder value as 
#key and value.

jump={
    5:9,  #ladder
    6:11,  #ladder
    15:7, #snake
    18:23,  #ladder
    28:17,   #snake
    23:16,  #snake
 
}

def ladder_snake():
    player1 = 0      #player 1 at 0th position
    player2 = 0      #player 2 at 0th position
    turn = 1         #the first turn will be 1
    
    print("------Welcome to snake and Game reach 30 to win -----")
    print("   press Enter to roll the dice\n")
    print("---------------------------------------------------")
    
    while True:
        if turn == 1:         #first player turn
            input("First player roll: ")
            roll = random.randint(1,6)  #taking a number between 1 to 4 by system
            print(f"First player rolled : {roll}")
            player1 += roll         #adding the roll number in first player score

             #checking p1 exist in jump or not

            if player1 in jump:
                old = player1
                player1 = jump[player1]
                if player1>old:
                     print(f"Ladder: {old} → {player1} ")
                else :
                     print(f"snake: {old} → {player1} ")

            print(f"player 1 at : {player1}")
            if player1 >=30:
                print("\n First Player Wins.")
                break
            turn = 2

        else:
            input("Second Player roll:")
            roll = random.randint(1,6)
            print(f"First player rolled : {roll}")
            player2 += roll         #adding the roll number in Second player score

            #checking p2 exist in jump or not

            if player2 in jump:
                old = player2
                player2 = jump[player2]
                if player2>old:
                      print(f"Ladder: {old} → {player2} ")
                else :
                      print(f"snake: {old} → {player2} ")

            print(f"player 2 at : {player2}")
            if player2 >=30:
                  print("------------------------")
                  print("\n Second Player Wins.")
                  print("------------------------")
                  break
            turn = 1

        print(f"\n Positions → p1: {player1} and p2 : {player2}\n ")
    
# Running the game (calling the function)

ladder_snake()
    