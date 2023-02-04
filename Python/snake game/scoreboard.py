import time
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as score:
            self.highscore=int(score.read())
        self.color("green")
        self.penup()
        self.goto(0,265)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.write(f"High Score: {self.highscore} Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def increment_score(self):
        self.score+=1
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore.txt", mode="w") as score:
                score.write(f"{self.highscore}")
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        while True:
            self.color("white")
            self.write("Game Over", align="center", font=("Arial", 24, "normal"))
            time.sleep(1)
            self.color("red")
            self.write("Game Over", align="center", font=("Arial", 24, "normal"))
            time.sleep(1)
        