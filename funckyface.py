from turtle import *

class Face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos):

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutLine()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)

    def goHome(self):
        penup()
        goto(self.coord)

        setheading(0)

    def drawOutLine(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome()

    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self.size)
        pendown()
        dot(self.size / 10)
         self.goHome()
        