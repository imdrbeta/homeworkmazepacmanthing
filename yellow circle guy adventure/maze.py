import math
import random
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Yellow circle mouth guy")
wn.setup(1200, 1080)
wn.tracer(0)
turtle.register_shape("cherry.gif")
turtle.register_shape("pacman.gif")
turtle.register_shape("ghost.gif")
turtle.register_shape("key.gif")
turtle.register_shape("door.gif")

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("pacman.gif")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("cherry.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("ghost.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0

            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction = "left"
                elif player.xcor() > self.xcor():
                    self.direction = "right"
                elif player.ycor() < self.ycor():
                    self.direction = "down"
                elif player.ycor() > self.ycor():
                    self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("key.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("door.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)


levels = [""]

level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "xx   T xx               xx    xx",
    "xx  xxxxx   xxxxxxxxxxxxxx P  xx",
    "xx     xx                     xx",
    "xxxxx  xxxxxxxxx   xx    xx   xx",
    "xx     xx    E     xx    xxxxxxx",
    "xx   xxxx   xxxxxxxxx    xx   xx",
    "xx          xx                xx",
    "xx   xxxxx  xxx  xxxxx   xx   xx",
    "xxxxxx      xx      xxxxxxxx  xx",
    "xx      xxxxxx   x  T xx      xx",
    "xx      xx       xxxxxxx   xxxxx",
    "xx   xxxxx   xxxxxx   xx      xx",
    "xx T xx      xx       xxxxxx  xx",
    "xxxxxxx  xxxxxx   xxxxxx      xx",
    "xx       xx   E   xx    T xxxxxx",
    "xxxxx  xxxx  xxx  xx   xxxx   xx",
    "xx     xx    xxx  xx          xx",
    "xx T xxxx Kxxxxx  xx   xxxx E xx",
    "xx     xx  xx     xxxxxxxxx   xx",
    "xxxx   xxxxxx  xxxxx          xx",
    "xx    xx       x  xx  xxxxxxxxxx",
    "xxxx  xx   xx     xx      xx  xx",
    "xx         xx     xx  xx      xx",
    "xx   xxxxxxxxxxxxxxxxxxxxxxx  xx",
    "xx   xx      xx           xx  xx",
    "xx           xxxxxx           xx",
    "xxxxxx   xx      xx  T  xxxxxxxx",
    "xx    E  xx     xxxxxxxxxx    xx",
    "xxxxxxxxxxxxx   xx            xx",
    "xx T            E    xxxxx D  xx",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]

levels.append(level_1)



def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.stamp()

                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            if character == "K":
                keys.append(Key(screen_x, screen_y))

            if character == "D":
                doors.append(Door(screen_x, screen_y))


pen = Pen()
player = Player()
enemies = []
keys = []
walls = []
treasures = []
doors = []
setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

door_collision = 0
Key.green = 0
player_death = 0
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player cherries: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player has died")
            player_death = player_death + 1
            player.goto(360,240)
            if player_death == 3:
                print("YOU DIED.")
                turtle.Screen().bye()

    for Key in keys:
        if player.is_collision(Key):
            print("escape route unlocked")
            Key.destroy()
            keys.remove(Key)
            Key.green = 1

    for door in doors:
        if player.is_collision(door) and Key.green == 1:
            print("YOU COMPLETED THE LEVEL")
            turtle.Screen().bye()

    wn.update()