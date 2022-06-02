from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_start()

    def move_up(self):
        y_axis = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_axis)

    def move_left(self):
        x_axis = self.xcor() - MOVE_DISTANCE
        self.goto(x_axis, self.ycor())

    def move_right(self):
        x_axis = self.xcor() + MOVE_DISTANCE
        self.goto(x_axis, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
