# Detection with paddle for r_paddle: the distance method measures the distance between the MIDDLE of each object.
# In order for the ball to be able to land on all parts of the paddle there needs to be a distance of less than 50.
# This is because the WHOLE length of the paddle is 100. This means that the distance of the ball on the edge of the
# paddle and the MIDDLE of the paddle is 50. Anything less than 50 just means it is closer to the middle of the paddle.
# The ball also has to stop on top of the paddle before it bounces. The top of the paddle is located at (340,0). This is
# because the MIDDLE of the paddle is at (350,0) and the WHOLE paddle is 20 pixels wide. Therefore, there is a distance
# of 10 pixels between the middle of the paddle and the top of the paddle. To tweak it a bit the ball could hit at
# (320,0) so that it hits just above the paddle before bouncing. The same logic applies for the l_paddle but with its
# corresponding numbers
#
# time.sleep(): The parameter has to be positive and the smaller the number the faster the iteration


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.title("PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # pauses the time between each iteration so the ball does not move too fast
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle (look above for logic explanation)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 390:
        ball.out_of_bounds()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -390:
        ball.out_of_bounds()
        scoreboard.r_point()



screen.exitonclick()
