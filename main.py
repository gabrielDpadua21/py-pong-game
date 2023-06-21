from turtle import Screen
from classes.paddle import Paddle


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.listen()

    paddle01 = Paddle((350, 0))
    paddle02 = Paddle((-350, 0))

    screen.onkey(paddle01.go_up, "w")
    screen.onkey(paddle01.go_down, "s")
    screen.onkey(paddle02.go_up, "Up")
    screen.onkey(paddle02.go_down, "Down")

    screen.exitonclick()
    