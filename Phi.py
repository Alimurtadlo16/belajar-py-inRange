from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
c = 0
phi = (1 + 5 ** 0.5) / 2  
up()
goto(40, -110)
down()

for i in range(350):
    c += 0.065
    color(hsv_to_rgb(c, 1, 1))
    forward(i * phi / 20)  
    right(50)
    circle(40 * phi, 139) 
    forward(140 - i * phi) 
hideturtle()
done()