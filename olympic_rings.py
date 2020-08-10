from turtle import *

speed("fastest")

def olympicRings(canvasSize):
    setup(canvasSize, canvasSize/2)
    ringThickness = canvasSize/75
    ringRadius = canvasSize/10

    
    rings = [["blue", canvasSize/-6.667, canvasSize/-40],
             ["black",0 , canvasSize/-40],
             ["red", canvasSize/6.667, canvasSize/-40],
             ["yellow", canvasSize/-13.333, canvasSize/-6.667],
             ["green", canvasSize/13.333, canvasSize/-6.667]]
    
    pensize(ringThickness)
    
    def circleCreator(size, color, x, y):
        pu()
        goto(x, y)
        pencolor(color)
        setheading(0)
        pd()
        circle(size)
        
        
    for ring in rings:
        circleCreator(ringRadius, ring[0], ring[1], ring[2])



olympicRings(500)




hideturtle()
done()
