# Project named ten-thousand.

## prompt 2

    Define a GameLogic class in ten_thousand/game_logic.py file.
    Handle calculating score for dice roll
    Add calculate_score static method to GameLogic class.
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer representing the roll’s score according to rules of game.
    Handle rolling dice
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.



<code>
import random

class GameLogic:
    @staticmethod
   def calculate_score(roll):

   score = 0
        counter = [0] * 7  # counter to keep track of the number of each die face
        
  for die in roll:
            counter[die] += 1

  if counter[1] >= 3:
            score += 1000
            counter[1] -= 3
        
  for i in range(2, 7):
            if counter[i] >= 3:
                score += i * 100
                counter[i] -= 3
        
   score += counter[1] * 100
   score += counter[5] * 50
        
   return score

   @staticmethod
    def roll_dice(num_dice):

   return tuple(random.randint(1, 6) for _ in range(num_dice))
</code>





## prompt 2.

    handle  A straight (i.e., all dice showing consecutive numbers) case


<code># check for a straight
        if all(counter[i] == 1 for i in range(1, 7)):
            score += 1500
            return score</code>











