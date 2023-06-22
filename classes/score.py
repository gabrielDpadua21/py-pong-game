from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_player01 = 0
        self.score_player02 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Player 1: {self.score_player01} | Player 2: {self.score_player02}", align="center", font=("Courier", 24, "normal"))

    def set_point_player01(self):
        self.score_player01 += 1
        self.print_score()

    def set_point_player02(self):
        self.score_player02 += 1
        self.print_score()
