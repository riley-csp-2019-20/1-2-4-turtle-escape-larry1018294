import turtle as trtl
import random

player = trtl.Turtle()
drawer = trtl.Turtle()
drawer.pensize(5)
drawer.ht()
drawer.speed(0)

amount = 15
drawer.speed(0)
wall_width = 15
door_width = 20
drawer.color("red")
drawer.pensize(5)
barrier= 10




def up():
    player.setheading(90)
    player.forward(5)
   
def right():
    player.setheading(0)
    player.forward(5)

def left():
    player.setheading(180)
    player.forward(5)

def down():
    player.setheading(270)
    player.forward(5)
   
for i in range(25):
    if i > 4 and i < 22:
        door = random.randint(2*wall_width, amount - 2*wall_width)
        barrier = random.randint(2*wall_width, amount - 2*wall_width)

        if door < barrier:
            drawer.forward(door)

            #door thingy
            drawer.penup()
            drawer.forward(door_width)
            drawer.pendown()

            drawer.forward(barrier - door - door_width)

            #barrier thingy
            drawer.left(90)
            drawer.forward(wall_width*2)
            drawer.back(wall_width*2)
            drawer.right(90)

            drawer.forward(amount - barrier)

        else:
            drawer.forward(barrier)

            #barrier thingy part 2
            drawer.left(90)
            drawer.forward(wall_width*2)
            drawer.back(wall_width*2)
            drawer.right(90)

            drawer.forward(door - barrier)

            #door thingy part 2
            drawer.penup()
            drawer.forward(door_width)
            drawer.pendown()

            drawer.forward(amount - door - door_width)

        
    drawer.left(90)
    amount += wall_width 

wn = trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(down,"Down")
wn.listen()
wn.mainloop()
