from turtle import Turtle
alingment="center"
font="courier",24,"normal"

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Score :{self.score}",align=alingment,font=font)

    def increasescore(self):
        self.score=self.score+1
        self.clear()
        self.updatescoreboard()
    def gameover(self):
        self.goto(0,0)
        self.write(f" GAME OVER  ",align=alingment,font= font)

