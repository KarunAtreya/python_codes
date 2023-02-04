from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle_left=Paddle((-350,0))
paddle_right=Paddle((350,0))
ball = Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_right)<50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()