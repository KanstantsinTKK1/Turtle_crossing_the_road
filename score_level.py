from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 21, 'normal')
FONT_GAME_OVER = ('Courier', 30, 'normal')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.score = 0
        self.goto(-230, 260)
        self.write(f'Level: {self.score}', move=False, font=FONT, align=ALIGN)

    def update_level(self):
        self.clear()
        self.score += 1
        self.write(f'Level: {self.score}', move=False, font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 20 )
        self.color('red')
        self.write('Game Over', move=False, align=ALIGN, font=FONT_GAME_OVER)