import random

class GameLogic:
    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score for a given dice roll according to the rules of Ten Thousand game.
        
        Args:
        - roll (tuple): a tuple of integers representing a dice roll
        
        Returns:
        - score (int): an integer representing the roll's score
        """
        score = 0
        counter = [0] * 7  # counter to keep track of the number of each die face
        
        for die in roll:
            counter[die] += 1
        

        if counter[2] == 6:
            score += 800
            return score
            
        elif counter[2] == 5:
            score += 600
            return score
            
        elif counter[2] == 4:
            score += 400

            return score

        if counter[1] == 6:
            score += 4000
            return score
        

        if all(counter[i] == 1 for i in range(1, 7)):
            score += 1500
            return score
        
        # check for each possible scoring combination
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
        """
        Rolls a given number of dice, each with values between 1 and 6.
        
        Args:
        - num_dice (int): the number of dice to roll
        
        Returns:
        - roll (tuple): a tuple of random integers between 1 and 6
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))