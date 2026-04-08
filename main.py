from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

screen.listen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check collision with the walls
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

    # check collision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # if R paddles misses
    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.l_point()


    # if L paddles missed
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()



screen.exitonclick()