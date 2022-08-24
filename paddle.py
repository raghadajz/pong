from turtle import Turtle


class Paddle(Turtle):
    """Represents the paddles of the game.
        public attributes:
        - pos: represents the current position of the paddle (tuple)."""
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(self.pos)

    def up(self):
        """Move the paddle upwards."""
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        """Move the paddle downwards."""
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
