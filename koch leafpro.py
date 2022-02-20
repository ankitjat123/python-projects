# snowflake program to clear the idea of recuursion
import turtle
t=turtle.Turtle()
t.speed(1)

def ks(length,d):
    if d==0:
        t.forward(length)
    else:
        length=length/3
        d=d-1
        ks(length,d)
        t.right(60)
        ks(length,d)
        t.left(120)
        ks(length,d)
        t.right(60)
        ks(length,d)

colors=["red","orange","pink","blue"]
for i in range(1):
    t.color(colors[i])
    ks(120,3)
    t.left(120)
s= input()
