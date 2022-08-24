from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scorepong import Score

# Set up the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
POSITION_P1 = (350, 0)
POSITION_P2 = (-350, 0)
screen.tracer(0)

right_paddle = Paddle(POSITION_P1)
left_paddle = Paddle(POSITION_P2)
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "x")
screen.onkey(left_paddle.down, "z")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move)
    ball.ball_pos()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Increase the right paddle score
    elif ball.xcor() < - 390:
        scoreboard.increase_score_r()
        ball.center()
    # Increase the left paddle score
    elif ball.xcor() > 390:
        scoreboard.increase_score_l()
        ball.center()
    # After 5 scores the game is over
    if scoreboard.score_r == 5 or scoreboard.score_l == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
