from turtle import Turtle


class PrintX(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.pencolor("#263159")
        self.write(f"X", align="center", font=('Arial', 20, 'bold'))


class PrintO(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.pencolor("#9D3C72")
        self.write(f"O", align="center", font=('Arial', 20, 'bold'))