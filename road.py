from turtle import Turtle
X_POSITION = -280
Y_POSITION = -190

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(X_POSITION,Y_POSITION)
        self.color('white')
        self.pensize(4)
        self.x_line_interval = 0
        self.y_line_interval = 0

    def paint_road (self):
        for y in range(9):
            for x in range(6):
                self.goto(X_POSITION + self.x_line_interval, Y_POSITION + self.y_line_interval)
                self.pendown()
                self.x_line_interval += 50
                self.goto(X_POSITION + self.x_line_interval, Y_POSITION + self.y_line_interval)
                self.penup()
                self.x_line_interval += 50
            self.x_line_interval = 0
            self.y_line_interval += 50
