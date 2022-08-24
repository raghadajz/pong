from turtle import Turtle


class Ball(Turtle):
    """Represents the ball of the game.
    public attributes:
    - x: this number will be added to the current x-coordinate
    to update the ball position (integer).
    - y: this number will be added to the current y-coordinate to update the ball
    position (integer).
    - move: to make the game more challenging this number will be updated so that the ball will move faster
    as the game continues (float)."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move = 0.1

    def ball_pos(self):
        """Update the ball position."""
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        """If the ball collides with the wall it will bounce to the opposite direction."""
        self.y *= -1

    def bounce_x(self):
        """If the ball collides with one of the paddles it will bounce to the opposite direction."""
        self.x *= -1
        self.move *= 0.9

    def center(self):
        """If one of the players scores the ball will be returned to the center and bounce in the opposite direction."""
        self.goto(0, 0)
        self.move *= 0.9
        self.bounce_x()
