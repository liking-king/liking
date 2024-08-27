import pygame
import random


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=3):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


# 背景类
class Background(GameSprite):
    # 方法二
    # def __init__(self,is_alt=False):
    #     super(Background, self).__init__('./images/op_1.jpg')
    #     if is_alt:
    #         self.rect.y = -self.rect.height

    def update(self):
        # 调用父类update方法，实现向下移动
        super(Background, self).update()
        # 判断是否飞出屏幕，如果是，则将图片设置到屏幕上方
        if self.rect.y >= 731:
            self.rect.y = -self.rect.height


# 敌机类
class Enemy(GameSprite):
    def __init__(self):
        # 调用父类方法，指定敌机图片
        image_name = random.choice(['./images/dd1.png', './images/dd.png'])
        super().__init__(image_name)
        # 创建随机速度
        self.speed = random.randint(1, 3)
        # 指定随机位置
        self.rect.x = random.randint(0, 1300 - self.rect.width)
        # 设置血量，连续射击n次才会死
        self.blood = 6

    def update(self):
        # 调用父类的update方法，保持向下移动
        super(Enemy, self).update()
        if self.rect.y > 731:
            # 飞出屏幕需要从精灵组中删除，kill方法可以将精灵从精灵组中移出，精灵就会自动销毁
            self.kill()

    def __del__(self):
        # print('敌挂了')
        pass


class Hero(GameSprite):
    def __init__(self):
        # 调用父类方法，传递图片
        super().__init__('./images/cxk.png', 0)
        self.rect.x = 650 - self.rect.width / 2  # 屏幕正中间
        self.rect.y = 731 - self.rect.height  # 距离底部100
        self.upanddown = 0  # 控制向下移动的属性
        self.bullet_group = pygame.sprite.Group()  # 子弹精灵组

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.upanddown
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 1200:
            self.rect.x = 1200
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 731 - self.rect.height:
            self.rect.y = 731 - self.rect.height

    # 发射子弹
    def fire(self):
        # 实列化子弹,创建子弹精灵添加精灵组中
        # 创建3个子弹对象
        for i in range(3):
            bullet = Bullet()
            # 设置子弹的初始位置
            # 子弹中心点 = 飞机中心点
            bullet.rect.centerx = self.rect.centerx
            # 每颗子弹的y距离另一个对象y15
            bullet.rect.y = self.rect.y - (i+1)*10
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/zd.png', -10)

    def update(self):
        # 调用父类方法，实现垂直移动
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.y < -self.rect.height:
            self.kill()

    def __del__(self):
        # print('wu')
        pass
