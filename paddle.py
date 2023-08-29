from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)

    
    def Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)    