import colorgram
# colors = colorgram.extract('image.jpg.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle as t, Screen, Turtle
import random
screen = Screen()
screen.colormode(255)
color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]
tim = t()
tim.hideturtle()
tim.penup()
tim.pensize(0)
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(100):
    tim.penup()
    tim.pensize(0)
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if i == 9 or i == 19 or i == 29 or i == 39 or i == 49 or i == 59 or i == 69 or i == 79 or i == 89:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)






screen = Screen()
screen.exitonclick()
