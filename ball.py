from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("sky blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # whatever the y direction is, it will continue moving in the opposite direction

    def bounce_x(self):
        self.x_move *= -1  # whatever the x direction is, it will continue moving in the opposite direction
        self.move_speed *= 0.9

    def out_of_bounds(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
