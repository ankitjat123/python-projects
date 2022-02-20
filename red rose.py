import turtle as tt
bb=tt.Turtle()
bb.speed(150)
bb.reset()
bb.color("red")
for angle in range(0,360,15):
    bb.seth(angle)
    bb.circle(100)
