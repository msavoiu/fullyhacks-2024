import turtle
import time
from turtle import *

juno = turtle.Turtle()

def loopFour(t, colors):
    def breathingLoop(t, color):
        t.shapesize(1)
        t.pensize(5)
        turtle.delay(10)
        t.color(color)
        t.shape("turtle")
        t.begin_fill()
        t.circle(150)
        t.end_fill()

    color_index = 0
    for x in range(4):
        if color_index > 1:
            color_index = 0
        breathingLoop(t, colors[color_index])
        color_index += 1

colors = ['#32FF00', '#00FFF7']
loopFour(juno, colors)

# timer=turtle.Turtle()
# start=time.time()
# while True:
#     timer.clear()
#     timer.write(int(time.time() - start))
