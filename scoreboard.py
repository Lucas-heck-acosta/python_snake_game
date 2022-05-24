from turtle import Turtle
STYLE = ("arial", 15, "bold")


class Score(Turtle):
    def __init__(self):  # set default text values
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-285, 275)
        self.write(f"Score = {self.score}", False, align="left", font=STYLE)

    def point_up(self):  # increase total score by 1
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align="left", font=STYLE)

    def gameover(self):  # game over text
        self.home()
        self.write("GAME OVER", False, align="center", font=STYLE)


