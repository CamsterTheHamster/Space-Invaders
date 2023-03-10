import turtle
import math 
screen = turtle.Screen()


#screen.bgpic("Start Screen.png")
#def arena():
screen.bgcolor("purple")
screen.bgpic("Backround.png")
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()


# Score : Variable with a number
score = 0 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-290, 278)
scorestring = "SCORE: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#player lives
lives = 3
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("yellow")
lives_pen.penup()
lives_pen.setposition(135, 278)
style = font = ("verdana", 12, "normal")
lives_pen.write("Lives Remaining: " + str(lives), font = style, align = "left")
lives_pen.hideturtle

#Enemy Counter : Variable with a number
def counter():
    counter = 15
    if enemy == hit():
        counter -= 1


#Current Level : Variable with a number
level = 1

#When enemy counter = 0 new level starts : true/false statement
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(40, 278)
style = font = ("verdana", 12, "normal")
level_pen.write("you are on level" + str(level), font = style, align = "right")
level_pen.hideturtle 

if counter == 0:
    level += 1
    

if level == 2: 
    screen.bgpic("Win Screen.png")


turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("Bullet.gif")




#User ship
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 25




#enemies
import random


number_of_enemies = 15
enemies = []


for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


for enemy in enemies:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
   


enemyspeed = 15


#enemy.hitbox = (enemy.x + 10, enemy.y + 10, 10, 10)


#Tell User how to move : String
turtle.textinput("movement", "move with left and right arrow keys")
#Tell User how to shoot : String
turtle.textinput("shoot", "shoot with spacebar")


#tell user the score 
turtle.color("white")
style = font=("Verdana", 12, "normal")
turtle.write("Score: " + str(score), font= style, align = "right")

#Projectile
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletstate = "ready"


bulletspeed = 150

enemy_bullet = turtle.Turtle()
enemy_bullet.color("red")
enemy_bullet.shape("triangle")
enemy_bullet.penup()
enemy_bullet.speed(0)
enemy_bullet.setheading(90)
enemy_bullet.shapesize(0.5, 0.5)
enemy_bullet.hideturtle()

enemy_bulletstate = "ready"

enemy_bulletspeed = 50

enemyBullets = []
for _ in range(1):
    enemyBullets.append(enemy_bullet)


#User movement : Key binds
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
#User shoot: Key binds 
def shoot():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 1
        bullet.setposition(x, y)
        bullet.showturtle()


def hit ():
    if abs(bullet.xcor() - enemy.xcor()) < 20 and abs(bullet.ycor() - enemy.ycor()) < 20:
        enemy : enemy.hideturtle(); 
        enemy.remove(enemy);
        bullet.hideturtle();
        bullet.remove(bullet);
        

    if abs(bullet.xcor() - player.xcor()) < 10 and abs(bullet.ycor() - player.ycor()) < 10:
        player : player.hideturtle();
        player.remove(player);
        bullet.hideturtle();
        bullet.remove(bullet);
        arena : bullet.hideturtle();
        bullet.remove(bullet);
       
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(shoot, "space")


#Gameloop

Game_Over = False
missed_enemies = 0
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)


        if enemy.xcor() > 270:
            for e in enemies:
                y = e.ycor()
                y -= 40


                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
            enemyspeed  *= -1


        if enemy.xcor() < -270:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
            enemyspeed *= -1

    for enemy in enemies:
        if bullet.distance(enemy) < 30:
            bullet.hideturtle()
            enemy.hideturtle()
            bulletstate = "ready"
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(
                scorestring, False, align="left", font=("Arial", 14, "normal")
            )
    
    for enemy in enemies:
        if player.distance(enemy) < 20:
            player.hideturtle()
            enemy.hideturtle()
            score_pen.hideturtle()
            lives_pen.hideturtle()
            border.hideturtle()
            screen.bgpic("Lose Screen.png")
                    
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)


    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


    if player == hit:
        player.hideturtle()
        lives -= 1
        player.setposition(0, -250)
        player.showturtle()
        
    if lives == 0:
        screen.bgpic("Lose Screen.png")


        
    #written enemy counter
    #enemy_pen = turtle.Turtle()
    #enemy_pen.speed(0)
    #enemy_pen.color("white")
    #enemy_pen.penup()
    #enemy_pen.setposition(135, 278)
    #style = font = ("verdana", 12, "normal")
    #enemy_pen.write("enemies remaining: " + str(counter), font = style, align = "right")
    #enemy_pen.hideturtle

#-add boss
#def boss():
    #turtle.addshape("Boss", "Boss.png")
    #boss.shape("Boss")
    #boss.penup()
   
    #boss.speed(0)
    #boss.hitbox = (boss.x + 10, boss.y + 10, 10, 10)


#-When current level = 3 and enemy counter = 0 Boss level: true false statement
#if Level == 3:
    #boss()
    #-When Boss is def:
    #if boss == False:
        #screen.bgpic("Win Screen.png")        

#When hit by enemy projectile: despawn animation and add value to scoreeat screen : String (Player lives)

turtle.done