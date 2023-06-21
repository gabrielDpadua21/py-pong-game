from turtle import Turtle, Screen


turtle = Turtle()

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    
    screen.exitonclick()
    