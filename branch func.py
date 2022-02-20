import turtle
import time
elsa=turtle.Turtle()
def branch(size): 
    for i in range(3): 
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3) 
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size)
branch(8)    
