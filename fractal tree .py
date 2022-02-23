import turtle as tu
bob=tu.Turtle()
bob.goto(-0,-100)
bob.left(90)
bob.speed(150)

def tree(i):
    if i<10:
        return
    else:
        bob.fd(i)
        bob.left(30)
        tree(3*i/4)
        bob.right(60)
        tree(3*i/4)
        bob.left(30)
        bob.backward(i)

tree(100)
        
