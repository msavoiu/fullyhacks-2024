import turtle
import time
from turtle import *

juno = turtle.Turtle()

def loopFour(t, colors):
    def breathingLoop(t, color):
        t.pensize(5)
        turtle.delay(16)
        t.color(color)
        t.shape("turtle")
        t.begin_fill()
        t.circle(150)
        t.end_fill()

    t.penup()
    t.goto(0, -120)
    t.pendown()
    color_index = 0
    while True:
        if color_index > 1:
            color_index = 0
        breathingLoop(t, colors[color_index])
        color_index += 1

colors = ['#32FF00', '#00FFF7']
loopFour(juno, colors)