import turtle
import random
import time
import os
import sys
import math
## haeve the game run at 4k and use the gamepal sdk and use the huggingface dall e mega for graphics
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
## resolution of the window
wn.setup(width=1920, height=1080)
player = turtle.Turtle()
player.color("blue")
payerspeed = 15
bulletstate = "ready"
### fix da code settings "Very High"
turtle.bgcolor("black")
turtle.title("Space Invaders")
playerspeed = 15
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
enemies = []
for i in range(20):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    ## make a page about the enemey
    enemies.append(turtle.Turtle())
    ## make a page about the enemey
    enemies.append(turtle.Turtle())
    ## make a page about the enemey
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
enemyspeed = 2
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
bulletstate = "ready"
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed

        ## fix da code "Very High"
        if x > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
 ## use the doom algrothim
        if x < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1  
       ## optimize this code using GAMEPAL SDK AT TIME 5:25 AND SETTINGS VERY HIGH
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
        enemy.setx(x)
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    if player.ycor() > 275:
        player.hideturtle()
        print("Game Over")
        break