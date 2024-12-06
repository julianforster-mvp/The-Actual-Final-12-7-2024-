#FINAL “Tuple Out” Dice Game
import random
#FUNCTION to check rerolls within my loop
def getrerolldie(dice1):
            if dice1[0] == dice1[1] and dice1[0] != dice1[2]:
                dice1[2] = random.choice([1, 2, 3, 4, 5, 6])
            elif dice1[1] == dice1[2] and dice1[1] != dice1[0]:
                dice1[0] = random.choice([1, 2, 3, 4, 5, 6])
            elif dice1[0] == dice1[2] and dice1[0] != dice1[1]:
                dice1[1] = random.choice([1, 2, 3, 4, 5, 6])       
            else:
                return 
# Initialize game variables
round = 0
max_rounds = 10
final_score = 0
f"LET'S GET READY TO GAMBLE!"
(f"Directions: You have 3 dice. If you roll the same number, no points. "
      "If you roll and they're all different, you get the option to reroll all the dice "
      "If you roll a pair you can only roll the odd one out. Good luck!")
# Game loop
while round < max_rounds and final_score <= 150:
    round += 1
    print(f"\nRound {round}/{max_rounds}")
    
    # Roll 3 dice and print the result
    dice1 = random.choices([1, 2, 3, 4, 5, 6], k=3)
    print(f"You rolled: {dice1}")

    # Check if the player "tupled out" (all dice are the same)
    if dice1[0] == dice1[1] == dice1[2]:
        print("You tupled out and earned -10 points this round!")
        round_score = -10  # -10 for this turn
    else:
        round_score = sum(dice1)  # Calculate score as the sum of the dice

    # If all dice are different, allow rerolling all dice
    # TODO clean code up 
    # TODO create score board using .csv
    while dice1[0] != dice1[1] and dice1[0] != dice1[2] and dice1[1] != dice1[2]:
            reroll_input= input("Would you like to re-roll ? Type 'ROLL' to reroll or 'STOP' to stop:").lower()
        #Recive and process user input to prompt a reroll
            if reroll_input == "roll":
                dice1= random.choices([1,2,3,4,5,6], k =3)
                round_score = sum(dice1)
                

            
            if dice1[0] == dice1[1] == dice1[2]:
                print("You tupled out and earned -10 points this round!")
                round_score = -10
                continue
            # TODO if they roll all the dice and get 1,1,2 how to allow them to reoll 3rd dice after or respective place holder
            #if dice1[1]== dice1[0] or dice1[1] == dice1[2] or dice1[2] == dice1[0]:
                #break
            
        
            else:
                round_score = sum(dice1)  # Recalculate score
            print(f"You re-rolled: {dice1} and your score for this round is: {round_score}")
            print(f"Your score for this round is: {round_score}")
        

    # If two dice are the same and one is different, allow reroll the odd die out
    if dice1[0] == dice1[1] and dice1[0] != dice1[2]:
        reroll_input = input("Would you like to re-roll the third die? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        while reroll_input == "roll":
            dice1[2] = random.choice([1, 2, 3, 4, 5, 6])  # Re-roll the third die

            if dice1[0] == dice1[1] == dice1[2]:
                print("You tupled out and earned -10 points this round!")
                round_score = -10
                continue
            else:
                round_score = sum(dice1)  # Recalculate score
            print(f"You re-rolled the third die and your new roll is: {dice1} with a score of {round_score}")
            reroll_input = input("Would you like to re-roll the third die again? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        print(f"Your score for this round is: {round_score}")
        

    elif dice1[0] == dice1[2] and dice1[0] != dice1[1]:
        reroll_input = input("Would you like to re-roll the second die? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        while reroll_input == "roll":
            dice1[1] = random.choice([1, 2, 3, 4, 5, 6])  # Re-roll the second die

            if dice1[0] == dice1[1] == dice1[2]:
                print("You tupled out and earned 0 points this round!")
                round_score = -10
                continue
            else:
                round_score = sum(dice1)  # Recalculate score
            print(f"You re-rolled the second die and your new roll is: {dice1} with a score of {round_score}")
            reroll_input = input("Would you like to re-roll the second die again? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        print(f"Your score for this round is: {round_score}")
        

    elif dice1[1] == dice1[2] and dice1[1] != dice1[0]:
        reroll_input = input("Would you like to re-roll the first die? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        while reroll_input == "roll":
            dice1[0] = random.choice([1, 2, 3, 4, 5, 6])  # Re-roll the first die

            if dice1[0] == dice1[1] == dice1[2]:
                print("You tupled out and earned -10 points this round!")
                round_score = -10
                continue
            else:
                round_score = sum(dice1)  # Recalculate score
            print(f"You re-rolled the first die and your new roll is: {dice1} with a score of {round_score}")
            reroll_input = input("Would you like to re-roll the first die again? Type 'ROLL' to reroll or 'STOP' to stop: ").lower()
        print(f"Your score for this round is: {round_score}")
        
# elif dice1[1]== dice1[0] or dice1[1] == dice1[2] or dice1[2] == dice1[0]
       
    # Add the round score to the total score
    final_score += round_score

    # Print total score after each round
    print(f"Your total score is now: {final_score}")

# Final message after the game ends
print(f"\nGame over! Your final total score is: {final_score}")
print("Thanks for playing! Goodbye!")
        

