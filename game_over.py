from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.pencolor("black")
        # self.write(f"GAME OVER, {player} WON", align="center", font=FONT)