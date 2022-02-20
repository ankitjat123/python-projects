import turtle
import math
import random
bob=turtle.Turtle()
bob.speed(100)
for i in range(10000):
    bob.fd(math.sqrt(i))
    bob.left(i)
    
    
