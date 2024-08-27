

import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=2):
        # 调用父类的初始化方法
        super(GameSprite, self).__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # 获取位置对象(0,0,图片宽,图片高)
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向向下移动
        self.rect.y += self.speed
