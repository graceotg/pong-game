from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_coord):
        super().__init__()
        self.starting_coord = starting_coord
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # default turtle shape is 20 by 20. Stretch means multiply
        self.penup()
        self.goto(self.starting_coord)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)


