import random
import turtle
import time

turtle.setup(600, 600)
turtle.write("Ready for more circles?" , align= "center", font=("Arial", 16, "bold"))

time. sleep(3)
turtle.undo()

radius = int()
colors = ("red", "blue", "yellow", "green")

pen_size = int()
random_index = int()

x = int()
y =  int()

for i in range (20):

    x = random.randint(-150, 150)
    y = random.randint(-150, 150)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    random_index = random.randint(0,3)
    radius = random.randint(25,125)
    pen_size =random.randint(0,10)

    turtle.fillcolor(colors[random_index])
    turtle.pensize(pen_size)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.mainloop()
