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
        with open("highscore.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        

        self.write(f"Score: {self.score} High Score: {self.high_score}",False, align=ALIGNMENT, font=(FONT_NAME,FONT_SIZE,FONT_TYPE))
    
    
    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
            
            
            

            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
