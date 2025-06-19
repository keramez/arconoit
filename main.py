import pygame as pg 
from time import time
from random import randint
#hi caca lflfllfl DIMA drrraaaaaaa


pg.init()


class picture():
    def __init__(self, filename, x=0, y=0, w=10, h=10, speed_x = 0, speed_y=0):
        self.rect = pg.Rect(x, y, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pg.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))



bg_color = (66,	133, 180)


mw = pg.display.set_mode((500, 500))
mw.fill(bg_color)

fon = pg.image.load('font.jpg')
fon1 = pg.image.load('game.png')
fon2 = pg.image.load('game.png')

ball = picture('ball.png', 400, 400, 50, 50, 3, -3)

monsters = []
count = 9
y = 5

for i in range(3):
    x = 5 + 27.5*i
    for j in range(count):
        monster = picture('enemy.png', x, y, 50, 50)
        monsters.append(monster)
        x += 55

    count -=1
    y += 55

monster = picture('enemy.png', 5, 5, 3, -3)
platform = picture('platform.png', 200, 300, 100, 20, 0, 0)

clock = pg.time.Clock()
game = True
while game:
    
   

    ball.rect.x += ball.speed_x
    ball.rect.y += ball.speed_y
    platform.rect.x += platform.speed_x

    if ball.rect.x >= 475 or ball.rect.x <= -22:
        ball.speed_x *= -1
    if ball.rect.y <= -22:
        ball.speed_y *= -1

    if ball.rect.colliderect(platform.rect):
        ball.speed_y *= -1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                platform.speed_x = -5
            if event.key == pg.K_RIGHT:
                platform.speed_x = 5 
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                platform.speed_x = 0
            if event.key == pg.K_RIGHT:
                platform.speed_x = 0

                
    if ball.rect.y > 500:
        break

    if len(monsters) == 0:
        break


    mw.blit(fon, (0,0))

    if ball.rect.y > 500:
        mw.blit(fon1, (0, 0))
        pg.display.update()
        break

    if len(monsters) == 0:
        mw.blit(fon1m (0, 0))
        pg.display.update()
        break

    monster.draw()
    ball.draw()
    platform.draw()

    for monster in monsters:
        monster.draw()
        if monster.rect.colliderect(ball.rect):
            monsters.remove(monster)
            ball.speed_y *= -1

    clock.tick(40)
    pg.display.update()


    
