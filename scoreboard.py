from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            high_score = int(data.read())
        self.high_score = high_score
        self.color('white')
        self.penup()
        self.goto(0, 420)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update and display the current score and high score
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        # Reset score, update high score and store it in data.txt, and display on the scoreboard
        if self.score > self.high_score:
            with open("data.txt", mode='w') as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        # Increase the score and update the scoreboard
        self.score += 1
        self.update_scoreboard()
