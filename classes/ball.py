from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10


    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self) -> None:
        self.y_move *= -1
