from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):  # set default food values
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setpos(random.randint(-277, 277), random.randint(-277, 277))

    def eat(self):  # change food to a new random position
        self.setpos(random.randint(-277, 277), random.randint(-277, 277))





