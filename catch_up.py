from pygame import *
import pygame
from random import randint
width=600
height=500
window = display.set_mode((width, height))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('back.jpg'), (width, height))
font.init()
clock = time.Clock()
FPS = 60

speed_x = 5
speed_y = 5

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y  
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < height-150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height-150:
            self.rect.y += self.speed

font = font.Font(None, 70)
lose = font.render('LOSE', True, (0,0,0))
finish=False
player1 = Player('player.png', 80, 200, 40, 150, 10)
player2 = Player('player.png', 470, 200, 40, 150, 10)
ball = Player('ball.png', 270, 200, 70,70, 10)
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update_l()
        player2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *=1
        if ball.rect.y > 430 or ball.rect.y < 3:
            speed_y *= -1
        if ball.rect.x >530 or ball.rect.x < 0:
            window.blit(lose, (250, 250))
            finish=True
    for e in event.get():
        if e.type ==  QUIT:
            game = False
    display.update()
    clock.tick(FPS)