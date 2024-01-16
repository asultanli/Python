from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    def increse_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Courier", 24, "normal"))
    def check_highScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt",mode="w") as file1:
            file1.write(str(self.highscore))
