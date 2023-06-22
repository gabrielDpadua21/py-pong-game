from turtle import Screen
from time import sleep
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score


if __name__ == "__main__":
    screen = Screen()
    GAME_ON = True
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.listen()
    SPEED = 0.1

    paddle01 = Paddle((350, 0))
    paddle02 = Paddle((-350, 0))
    ball = Ball()
    score = Score()

    screen.onkey(paddle01.go_up, "w")
    screen.onkey(paddle01.go_down, "s")
    screen.onkey(paddle02.go_up, "Up")
    screen.onkey(paddle02.go_down, "Down")

    while GAME_ON:
        sleep(SPEED)
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(paddle01) < 50 and ball.xcor() > 320:
            ball.bounce_x()
        if ball.distance(paddle02) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        if ball.xcor() > 380:
            score.set_point_player01()
            ball.reset()
            SPEED *= 0.1
        if ball.xcor() < -380:
            score.set_point_player02()
            ball.reset()
            SPEED *= 0.1



    screen.exitonclick()
    