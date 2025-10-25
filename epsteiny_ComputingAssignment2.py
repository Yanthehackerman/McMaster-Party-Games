""" 
The Game File is split into 5 respective parts:

1) Importation of Files and Libraries 
    Adds i.e. pygame mixer and all game soundtrack/sfx

2) Pre-Game Functions: (2) 
    Includes signature statement as per request
    Includes loading function that mimics a game cartridge booting

3) Minigames + Info: (4)
    Includes all 3 minigames: Look Away, Slot Machine and Pig
    Includes instruction/rules function for the game
    Counts scoring and draws the crosshair

4) Games_Room function
    Acts as the _main_ function (while loop) for the entire game
    Includes menu for games and allows user to select
    Manages user choice per game and references respective game function

5) Function Runner and Final Score Display
    Runs the two Pre-Functions
    Then loads main games_room()
    When done, displays final text on screen

NOTES: 
1)
Many cases include input statements and time.sleep statments
that are not returned or stored; they simply act as pauses 
to allow player more "game" control and clarity

2)
Often through code there are plenty of blank print()
These are simply to allow cleaner user experience

- Both are Cosmetic only and do not affect game logic whatsoever

WARNING: 
Uses mixer from the pygame module
Music files only work if game is working directory
If not, game and music will not work as files will not load

Have fun :D

Yan Epstein, 2025"""

#---------------------------------------------------------------------------------
# Imports the Music and Sound Effects used

'''
Every time .play() is used, it plays the mp3 file
Every time .stop() is used, it stops the respective file
'''

import time
import random
from pygame import mixer


# Imports the music and sfx used in game
# (Game must be working directory or this will crash)
mixer.init()

la_music = mixer.Sound("Look_Away.mp3") # Original Mario Look Away OST used
slots_music = mixer.Sound("Slots_Theme.mp3") 
pig_music = mixer.Sound("Pig.mp3") 

loading_sfx = mixer.Sound("Loading_SFX.mp3") 
slots_sfx = mixer.Sound("Slots_Win.mp3")
wrong_sfx = mixer.Sound("Skill_Issue.mp3")

rules_music = mixer.Sound("Instructions.mp3")
main_music = mixer.Sound("Main_Theme.mp3")
end_music = mixer.Sound("End.mp3")

#---------------------------------------------------------------------------------
## Signature Function
def print_signature(): #Prints info, then scrolls to "clean up" terminal space
    print()
    print("-----------------------------------------------------------------")
    print("Yan Epstein (400624739), Engineering I")
    print("ENG 1P13: Integrated Cornerstone Design Projects in Engineering,")
    print("Sam Scott, Fall 2025")
    print("-----------------------------------------------------------------")
    
    time.sleep(1)
    for i in range (5):
        print()

#---------------------------------------------------------------------------------
## Loading Function
def loading():
    '''
    Prints out hundreds of print statements in quick succession
    to mimic the look of a game cartridge being loaded
    '''

    loading_sfx.play()
    for i in range (100):
        print(f"\033[31mExtracting MacParty Data: {i+1}%\033[0m")
        time.sleep(0.05)
    print()

    for i in range (100):
        print(f"\033[33mCompiling Game Logic Data: {i+1}%\033[0m")
        time.sleep(0.05)
    print()

    for i in range (100):
        print(f"\033[31mLoading McParty: {i+1}%\033[0m")
        time.sleep(0.02)
    print("RUNNING MCPARTY.EXE...")

    for i in range (5):
        print()

#---------------------------------------------------------------------------------
## Instruction function
def instructions():
    
    '''
    Lists the respective games rules for each game (Look Away, Slot Machine, Pig)
    \033[#m acts as print modifier to underline or highlight dependant on index
    '''

    print("---------------------------------------------------------------------")
    print("\033[1mLook Away:\033[0m")
    print("You compete against two computer players") 
    print("You choose one of the four directions:") 
    print("(1 = up, 2 = down, 3 = left, and 4 = right)") 
    print("The two computer players randomly select as well") 
    print("If your direction is different from the two, you win \033[4m10 points\033[0m") 
    print("If your direction matches at least one, you lose and gain no points") 
    print("Every time you play, you \033[0mpre-select 3 directions for 3 rounds total\033[0m") 
    
    print("---------------------------------------------------------------------")
    print("\033[1mSlot Machine\033[0m")
    print("For this game, you must bet your points to play")
    print("and are NOT allowed to bet more than owned")
    print("The slot machine chooses \033[4m3 random symbols from 4 possible symbols\033[0m")
    print("If 2 symbols match, you are rewarded 2x the amount bet")
    print("If all symbols match, you are rewarded 5x the amount bet")
    print("If no symbols match, you are rewarded nothing and lose the bet")

    print("---------------------------------------------------------------------")
    print("\033[1m\'Pig\' Game\033[0m")
    print("You chose how many points you wish to earn")
    print("This is your \033[4mThreshold\033[0m")
    print("The games repeateadly rolls two dice, numbered 1-6")
    print("As the pair is rolled, the total is added up, and this repeats until:")
    print("- Total exceeds Threshold; awarded the total, NOT the threshold   (Win)")
    print("- One of the rolled dice is 1; you win no points and game ends    (Loss)")
    print("- If both rolled dice are a 1, you lose ALL GAME POINTS           (Catastrophic Loss)")
    print("---------------------------------------------------------------------")

    print("If at any time you enter a non-integer direction, move, or threshold")
    print("Game will crash, so please keep that in mind")
    input("Enjoy the minigames! (Press Enter to return to The Games Room): ")
    print()
    print()

#---------------------------------------------------------------------------------
## Look Away Code
def look_away(first_move,second_move,third_move): 
    '''
    Function for the Look Away Minigame
    Accepts 3 moves as arguments and returns game score 
    Refer to instructions for game rules
    '''
    look_away_points = 0
    round_status = ""  # Manages if won/lost
    current_move = ""  # Manages user move per round
    decoder = 0 # Variable used later for number to move conversion 

    print("")
    print("--------------------------------------------")
    for i in range (3):
        cpu1_move = random.randint(1,4)
        cpu2_move = random.randint(1,4)

        # Checks index to extract respective move out of three
        if i == 0:
            current_move = first_move
        elif i == 1:
            current_move = second_move
        else:
            current_move = third_move

        # Compares user moves to computer moves AND checks if move within range
        if (current_move != cpu1_move and current_move != cpu2_move) and current_move > 0 and current_move < 5:
            round_status = "Won"
            look_away_points += 10 # Adds points per round if user won
        else:
            round_status = "Lost"

        for i in range(3):
            # loop decodes the number values of the moves to the actual moves
            # Checks for both computers and user, whom is current_move
            # Accesses each of the three, checks, then rewrites that value

            # Checks which value
            if i == 0:
                decoder = cpu1_move
            elif i == 1:
                decoder = cpu2_move
            else:
                decoder = current_move

            # Converts int to move
            if decoder == 1:
                decoder = str("Up")
            elif decoder == 2:
                decoder = str("Down")
            elif decoder == 3:
                decoder = str("Left")
            elif decoder == 4:
                decoder = str("Right")
            else:
                decoder = str("an Invalid Choice")

            # Rewrites the respective value back
            if i == 0:
                cpu1_move = decoder
            elif i == 1:
                cpu2_move = decoder
            else:
                current_move = decoder

        #Prints round result of each move and point
        print(f"CPU 1 chose {cpu1_move}, CPU 2 chose {cpu2_move}, You chose {current_move} | You {round_status} |")
    
    print("--------------------------------------------")
   
    print(f"You Earned {look_away_points} points")   
    print()
    input("Press Enter to return to The Games Room: ")
    print()
    return(look_away_points) 

#---------------------------------------------------------------------------------
## Slot Machine Code
def slot_machine(bet): 

    '''
    Function for the Slot Machine Away Minigame
    Accepts a bet as argument and returns slot score 
    Refer to instructions for game rules
    '''

    slot_1 = 0
    slot_2 = 0
    slot_3 = 0

    for i in range (3):
        
        # Chooses 1-4, then records respective symbol
        slot_Choice = random.randint(1, 4)  
        if slot_Choice == 1:
            slot_Choice = "💎"
        elif slot_Choice == 2:
            slot_Choice = "🔔"
        elif slot_Choice == 3:
            slot_Choice = "🍒"
        else:
            slot_Choice = "🎲"

        # Checks index to save current slot choice to respective position
        if i == 0:
            slot_1 = slot_Choice
        elif i == 1:
            slot_2 = slot_Choice
        else:
            slot_3 = slot_Choice

    if slot_1 == slot_2 == slot_3: # x5 score if all 3 are the same
        bet_multiplier = 5
        slots_sfx.play()
    elif (slot_1 == slot_2) or (slot_1 == slot_3) or (slot_2 == slot_3):
        bet_multiplier = 2   # x2 score if exactly 2 of 3 are the same
        slots_sfx.play() 
    else:
        bet_multiplier = 0   # Nothing if all different

    slot_points = bet * bet_multiplier # Multiplier x Bet Amount

    # Output shown to user
    print("-------------------------------")
    print(f"| {slot_1} {slot_2} {slot_3} | : You Won {slot_points} points")
    print("-------------------------------")
    print()
    input("Press Enter to return to The Games Room: ")
    print()
    return slot_points

#---------------------------------------------------------------------------------
## Pig Game Code
def pig_dice(threshold):

    '''
    Function for the Pig Minigame 
    Accepts a threshold as argument and returns either score, 0, or -1 
    Score if successfull, 0 if loss, and -1 if catastrophic 
    Refer to instructions for game rules
    '''

    rolls_string = "" # String to hold rolls
    rolls_total = 0   # Holds Roll Total


    while rolls_total < threshold:

        roll_1 = random.randint(1,6)
        roll_2 = random.randint(1,6)

        rolls_total += roll_1 + roll_2    # Adds to Roll Total
        rolls_string += (f"({roll_1},{roll_2}) ") # Concatenates the rolls to the string as output

        if (roll_1 == 1) and (roll_2 == 1): # If Both rolls are "1", Catastropic Loss

            print("---------------------------------------------------------------------")
            print(f"Threshold is {threshold}. Your Rolls: ",end="")
            print(f"{rolls_string} ",end="")
            print("| CATASTROPHIC LOSS | ")
            print("---------------------------------------------------------------------")
            # Outputs rolls, but not total
            print()
            input("Press Enter to return to The Games Room: ")
            print()
            return -1  # -1 is for Cat Loss
        
        elif (roll_1 == 1) or (roll_2 == 1): 
            # If only one roll is 1, regular loss 
            # While this would be true if both are "1", the if statement above supersedes
            print("---------------------------------------------------------------------")
            print(f"Threshold is {threshold}. Your Rolls: ",end="")
            print(f"{rolls_string}",end="")
            print("| Loss | ")
            print("---------------------------------------------------------------------")
            # Outputs rolls, but not total
            print()
            input("Press Enter to return to The Games Room: ")
            print()
            return 0  # -0 is for Regular Loss

    # If not a single "1", rewarded points and plays below
    print("---------------------------------------------------------------------")
    print(f"Threshold is {threshold}. Your Rolls: ",end="")
    print(f"{rolls_string}",end="")
    print(f"| Win ({rolls_total} points) | ")
    print("---------------------------------------------------------------------")
    # Outputs roll and total
    print()
    input("Press Enter to return to The Games Room: ")
    print()
    return rolls_total  # Returns the total points awarded

#---------------------------------------------------------------------------------
## The "main" Games Room function 
def games_room(name): 

    ''' 
    Hub for the minigames and displays current score at any case
    References the game functions above and accepts user input
    to play those games. When quit is chosen, final score is returned
    and while loop is broken

    Accepts name as arguement mostly for display; doesn't serve logical purpose
    '''
    
    score = 0 # Zeros the score before the loop
    print(f"Greetings, {name}! Welcome to MacParty!")
    print()

    while True: # Indefinite Loop that displays instructions, score and manages games
        
        main_music.play(-1) # -1 is to allow music to play indefinitely unless stopped
        print("---------------------------------------")
        print("You are in The Games Room")
        print(f"{name}, Your Current Score is: {score}\n ")
        print("To Play Look Away, Press L")
        print("To Play Slot Machine, Press S")
        print("To Play Pig, Press P\n")
        print("To Learn Games Rules, Press I")
        print("To Quit, Press Q")
        print("---------------------------------------")
        user_selection = input("Select Now: ") # Asks for selection

        # Each function has corresponding letter, with uppercase and lowercase accepted
        if user_selection == "L" or user_selection == "l":
            
            '''
            Following two commands stop menu theme, then play the function's
            music. These commands are seen again for each key
            '''
            main_music.stop()  
            la_music.play()

            print()
            print()
            print("--------------------  LOOK AWAY --------------------")
            print("Reminder: (1 = up, 2 = down, 3 = left, and 4 = right)") 
            print("Any other value will void that round's score, so be warned") 
            print()

            direction_1 = int(input(f"Please enter you direction for round 1: "))
            direction_2 = int(input(f"Please enter you direction for round 2: "))
            direction_3 = int(input(f"Please enter you direction for round 3: "))
            # Saves all three directions
            score += look_away(direction_1,direction_2,direction_3)
            # Runs the minigame and adds total to score
            la_music.stop() # Terminates minigame music
    
        elif user_selection == "S" or user_selection == "s":

            main_music.stop()
            slots_music.play()

            print()
            print()
            print("--------------------  SLOT MACHINE --------------------")
            print("-----McMaster University Does Not Endorse Gambling-----")
            print(f"Reminder, you cannot bet more than you have, which is {score}")
            print()

            user_bet = int(input("You feel lucky...how much do you want to bet? "))
            # Records userbet
            if (user_bet > score): # If more than owned, user kicked back to games_room
                print("You cannot bet more than you have; returning to The Games Room...")
                time.sleep(2)
                print()

                slots_music.stop()  

            elif(user_bet <= 0): # Bans 0 or lower; user kicked as well
                print("You cannot bet negative or 0 points; returning to The Games Room...")
                time.sleep(2)
                print()

                slots_music.stop()  

            else: # If bet is fine, minigame runs
                score -= user_bet #Subtracts the bet, as that's the nature of slots
                print("Rolling the Slots...")
                time.sleep(1)
                score += slot_machine(user_bet)
               # Runs the minigame and adds total to score
                slots_music.stop()  

        elif user_selection == "P" or user_selection == "p":

            main_music.stop()
            pig_music.play()

            print()
            print()
            print("---------------------  PIG ---------------------")
            print("--McMaster University Does Not Endorse Gambling--")

            threshold_score = int(input("You feel lucky...enter your desired Threshold Score: "))
            # Records Threshold

            if (threshold_score < 0):  # Bans less than zero, user kicked back to games_room
                print("You cannot have a negative Threshold; returning to The Games Room...")
                time.sleep(2)
                print()

                pig_music.stop()

            elif(threshold_score == 0): # Bans zero, user kicked back to games_room
                print("Please choose a non-zero Threshold; returning to The Games Room...")
                time.sleep(2)
                print()

                pig_music.stop()

            else:
                print()
                pig_result = pig_dice(threshold_score) 
               # Runs the minigame 
                pig_music.stop()

                if pig_result == -1: # As stated in pig_dice, if -1, zero ALL score
                    score = 0
                else:
                    score += pig_result # Adds score given; if zero, just adds nothing

        elif user_selection == "I" or user_selection == "i":

            main_music.stop()
            rules_music.play()

            print()
            instructions() # Displays rules

            rules_music.stop()
    
        elif user_selection == "Q" or user_selection == "q": 
            # Ends the game and returns final game score
            print()
            main_music.stop()
            end_music.play()
            return score
    
        else: # Catch exception if no correct options were picked
            print()
            print()

            main_music.stop()
            wrong_sfx.play()

            score_deduction = random.randint(1,20) # Penalty given
            score -= score_deduction # Penalty removed from total

            print("Invalid Entry")
            print("And, due to your incompetence")
            print(f"You are penalized {score_deduction} point(s)...")
            if score < 0: # Exception to prevent negative score
                score = 0
                print("And you're now at a rock bottom of 0...")
            time.sleep(3)
            print()
            print()
            
#---------------------------------------------------------------------------------
## Main Function

# Runs the two Pre-Game functions
print_signature() 
loading()

username = input("Enter Your Name: ")
if username == "":
    username = "Alex (Forgot their Name) Doe" # If the user forgot to enter name

print(f"Your final point count is {games_room(username)}. Thanks for Playing!") 
# Runs the ENTIRE game and yields back total points

print("Exiting Game...")
time.sleep(4) # Exception so final music can play