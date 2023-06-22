from turtle import Turtle

SHAPE = "square"
WIDTH = 5
LEN = 1

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LEN)
        self.color("white")
        self.points = 0

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
