from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.shapesize(2)
        self.start_position()

    def start_position(self):
        self.ht()
        self.penup()
        self.goto(-5, -250)
        self.showturtle()

    def move_up_turtle(self):
        self.forward(20)

    def move_down_turtle(self):
        self.backward(20)