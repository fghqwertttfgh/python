import pygame
import time
import random

pygame.init()

skier_img = ["./images/left2.png","./images/left1.png","./images/skier_forward.png","./images/right1.png","./images/right2.png"]
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("滑雪大冒险?")

class Skier(pygame.sprite.Sprite):
    def __init__(self):
        #创建一个子类
        pygame.sprite.Sprite.__init__(self)
        #初始化加载图片
        self.image = pygame.image.load("./images/skier_forward.png")
        #获取图片大小
        self.rect = self.image.get_rect()
        #指定中心
        self.rect.center = [320,100]
        #初始化方向
        self.angle = 0
    def turn(self,direction):
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        center = self.rect.center
        #加载对应图片
        self.image = pygame.image.load(skier_img[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        #速度
        speed = [self.angle,6 - abs(self.angle) * 2]
        return speed
    def move(self,speed)
        self.rect.centerx

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,255))
    
    
    pygame.display.update()

