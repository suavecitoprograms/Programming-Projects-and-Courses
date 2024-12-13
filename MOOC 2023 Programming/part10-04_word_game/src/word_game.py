# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        return 0
    
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def vowel_count(self, word:str):
        vowels = "aeiouAEIOU"
        count = 0
        
        for letter in word:
            if letter in vowels:
                count += 1
        return count
    
    
    def round_winner(self, player1_word: str, player2_word: str):
        if self.vowel_count(player1_word) > self.vowel_count(player2_word):
            return 1
        elif self.vowel_count(player1_word) < self.vowel_count(player2_word):
            return 2
        return 0
    
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        choices = {"rock": 0, 
                   "paper": 1, 
                   "scissors": 2}
        ## key is the choice, value is what they win against
        ## check if inputs are valid
        valid = choices.keys()
        if player1_word not in valid and player2_word not in valid:
            return 0
        if player1_word not in valid:
            return 2
        if player2_word not in valid:
            return 1
        
        difference = choices[player1_word] - choices[player2_word]
        
        if difference == 0:
            return 0
        
        if difference == -1 or difference == 2:
            return 2
        return 1
        
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()