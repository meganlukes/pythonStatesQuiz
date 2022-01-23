from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.pu()
        self.goto(220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.level}/50 States", align="center", font=FONT)

    def game_over(self):
        self.goto(-220, 260)
        self.write("You got them all!", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
