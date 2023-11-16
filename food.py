from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 1)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):

        # Generate random coordinates for the food to appear
        random_x = random.randint(-725, 725)
        random_y = random.randint(-425, 425)
        self.goto(random_x, random_y)
