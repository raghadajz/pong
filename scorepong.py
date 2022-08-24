from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        """Represents the scoreboard for the game.
        public attributes:
        - score_r: used to keep track of the right paddle score (integer).
        - score_l: used to keep track of the left paddle score (integer)."""
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the game score."""
        self.write(f"Score: {self.score_l} | {self.score_r}", align=ALIGNMENT, font=FONT)

    def increase_score_r(self):
        """Increase the score for the right paddle. """
        self.score_r += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_l(self):
        """Increase the score for the left paddle. """
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """States that the game is over."""
        if self.score_r == 5 or self.score_l == 5:
            self.clear()
            self.write(f"GAME OVER. {self.score_l} | {self.score_r}", align=ALIGNMENT, font=FONT)
