# Created by Xu Tianyue 2021/12/24
# Email: xutianyue@sjtu.edu.cn

# This is a Christmas Card from xxxxx to xxxxx.
from turtle import *
import random
import time

n = 100.0
delay(0)
tree_t = Turtle()
screensize(bg='mistyrose')
load_t = Turtle()
# Loading
load_t.penup()
load_t.color("dark green")
load_t.goto(-0,-250)
load_t.write("Your Christmas card is loading...\
    ", align="center", font=("Freestyle Script", 35, "bold"))
load_t.ht()
# Tree
tree_t.penup()
tree_t.goto(0,0)
tree_t.pendown()
tree_t.left(90)
tree_t.forward(3 * n)
tree_t.color("orange", "yellow")
tree_t.begin_fill()
tree_t.left(126)
tree_t.pensize(6)

for i in range(5):
    tree_t.forward(n / 5)
    tree_t.right(144)
    tree_t.forward(n / 5)
    tree_t.left(72)
tree_t.end_fill()
tree_t.right(126)

tree_t.backward(n * 4.8)

def tree(d, s):
    if d <= 0: return
    tree_t.forward(s)
    tree(d - 1, s * .8)
    tree_t.right(120)
    tree(d - 3, s * .5)
    tree_t.right(120)
    tree(d - 3, s * .5)
    tree_t.right(120)
    tree_t.backward(s)

tree_t.color("dark green")
tree(15, n)
tree_t.backward(n / 2)
time.sleep(1)
load_t.clear()

# Gifts
tracer(0)
tree_t.color('lavenderblush')
tree_t.write('Steam Cdkey:xxxxxxxxxxxxxxxxxx',align="center")
for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    tree_t.up()
    tree_t.forward(b)
    tree_t.left(90)
    tree_t.forward(a)
    tree_t.down()
    if random.randint(0, 1) == 0:
        tree_t.color('tomato')
    else:
        tree_t.color('wheat')
    tree_t.circle(2)
    tree_t.up()
    tree_t.backward(a)
    tree_t.right(90)
    tree_t.backward(b)

# Message
tree_t.goto(110,-30)
time.sleep(2)
tree_t.color('orangered')
tree_t.write("Merry Christmas\n     My Love", align="left",\
     font=("Freestyle Script", 35, "bold"))
tree_t.goto(110,-40)
# tree_t.write("Oops! Your gift is under the tree. Search for it !")
tree_t.ht()
update()

# Snow
snow_t = Turtle() 
snow_t.pensize(2)
snow_t.color('white')
tracer(0)
def snow(snowsize,dens):
    for i in range(dens):
        snow_t.pendown()
        snow_t.forward(snowsize)  
        snow_t.backward(snowsize)  
        snow_t.right(360 / dens)  
while True:
    for i in range(8):
        for j in range(7):
            height = random.randint(-400+i*100,-300+i*100)
            width = random.randint(300-100*j,400-100*j)
            angle = random.randint(0,359)
            snowsize = random.randint(7,12)
            snow_t.penup()
            snow_t.goto(height,width)
            snow_t.right(angle)
            snow(snowsize,12)
    update()
    time.sleep(1)
    snow_t.clear()

# 2021 Christmas Eve

