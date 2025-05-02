import random

class RockPaperScissors:
    VALID_CHOICES = ["Rock", "Paper", "Scissor"]

    def __init__(self):
        self.userSelection = ""
        self.computerSelection = ""

    def get_user_input(self):
        #Validate User Input
        while True:
            userInput = input("Please choose Rock, Paper, or Scissor?: ")
            capitalInput = userInput.strip().capitalize()
            if capitalInput in self.VALID_CHOICES:
                self.userSelection = capitalInput
                break
            else:
                print("Invalid! Try again")

    def get_computer_input(self):
        self.computerSelection = random.choice(self.VALID_CHOICES)

    def determine_winner(self):
        #Calculates who wins
        winning_combos = {
            "Rock": "Scissor",
            "Paper": "Rock",
            "Scissor": "Paper"
        }
        if self.computerSelection == self.userSelection:
            return "Its a Tie!"
        elif winning_combos[self.userSelection] == self.computerSelection:
            return "You Win!"
        else:
            return "You Lost..."

    def play_round(self):
        #Plays 1 round for replayability
        print("Welcome to Rock, Paper, Scissor!")
        self.get_user_input()
        self.get_computer_input()
        outcome = self.determine_winner()
        print(f"{outcome} You Chose: {self.userSelection}, Computer Chose: {self.computerSelection}")

# Main program
if __name__ == "__main__":
    userScore = 0
    computerScore = 0

    while True:
        game = RockPaperScissors()
        game.play_round()
        result = game.determine_winner()
        if result == "You Win!":
            userScore += 1
        elif result == "You Lost...":
            computerScore += 1
        print(f"Scoreboard: You-[{userScore}:{computerScore}]-Computer")
        print("Good Game!")

        while True:
            again = input("Do you want to play again? (Yes/No): ").strip().capitalize()
            if again in ["Yes","No"]:
                break
            print("Invalid. Try Again")

        if again == "No":
            break

    print("Thanks for Playing")