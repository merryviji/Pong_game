from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(5,1)
        self.setposition(position)

    def move_up(self):
        self.sety(self.ycor() + 40)

    def move_down(self):
        self.sety(self.ycor() - 40)