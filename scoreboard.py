from turtle import  Turtle
FONT_NAME = "Arial"
FONT_SIZE = 20
FONT_TYPE = "normal"
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color("white")
        self.goto(x = 0, y = 270)
        self.write("Score: " + str(self.score),False, align = ALIGNMENT, font=(FONT_NAME,FONT_SIZE,FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write("Score: " + str(self.score),False, align=ALIGNMENT, font=(FONT_NAME,FONT_SIZE,FONT_TYPE))
    
    def gameover(self):
        self.goto(x = 0,y = 0)
        self.write("Game Over" ,False, align=ALIGNMENT, font=(FONT_NAME,FONT_SIZE,FONT_TYPE))

