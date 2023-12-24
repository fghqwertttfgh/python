import pygame
import time
import random

clock = pygame.time.Clock()
speed = [0,6]

skier_img = ["./images/skier_forward.png","./images/skier_right1.png","./images/skier_right2.png","./images/skier_left2.png","./images/skier_left1.png"]
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("滑雪大冒险?")

class Skiercl(pygame.sprite.Sprite):
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
        #更新angle
        self.angle = self.angle + direction
        #限制范围
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        #保存self.rect.center
        center = self.rect.center
        #加载对应图片
        self.image = pygame.image.load(skier_img[self.angle])
       #获取图片大小
        self.rect = self.image.get_rect()
        #更改中心
        self.rect.center = center
        #速度
        speed = [self.angle,6 - abs(self.angle) * 2]
        return speed
    def move(self,speed):
        #更新位置
        self.rect.centerx = self.rect.centerx + speed[0]
        #限制位置
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 640:
            self.rect.center = 640
pygame.init()
skier = Skiercl()


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #按键检测
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
                print("left")
            if event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
                print("right")

    
    screen.fill((255,255,255))
    #加载图片
    screen.blit(skier.image,skier.rect)
    #移动
    skier.move(speed)
    
    
    pygame.display.update()

