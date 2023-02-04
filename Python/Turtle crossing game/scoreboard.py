from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.color("black")
        self.level=1
        self.update_score()

    def game_over(self):
        self.goto(-100,0)
        self.write(f"GAME OVER",align="left",font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)
        self.level+=1
        
    
