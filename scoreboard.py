from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-215, 250)
        self.show_score()

    def show_score(self):
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
