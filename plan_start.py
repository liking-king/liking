import pygame
import plan_sprite
import sys

# 敌机出场事件代号
ENEMY_EVENT = pygame.USEREVENT

# 发射子弹事件
FIRE = pygame.USEREVENT + 1


# 初始化
class PlaneGame:
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((1300, 731))
        # 设置窗口标题
        pygame.display.set_caption('飞坤大战')
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        # 函数调用，创建精灵和精灵组
        self.creat_sprite()
        # 创建敌机出场定时器(每隔一秒触发一次)
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        # 创建发射子弹定时器(每隔0.4秒发射一次)
        pygame.time.set_timer(FIRE, 300)

    # 创建精灵和精灵组
    def creat_sprite(self):
        # 创建背景精灵和精灵组
        bg = plan_sprite.Background('./images/op_2.jpg')
        bg2 = plan_sprite.Background('./images/op_1.jpg')

        # 方法二
        # bg = plan_sprite.Background()
        # bg2 = plan_sprite.Background(True)

        bg2.rect.y = -bg2.rect.height
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(bg, bg2)

        # 创建一个敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = plan_sprite.Hero()
        self.hero_group = pygame.sprite.Group()
        self.hero_group.add(self.hero)

    # 事件监听
    def event_handler(self):
        # 获取按键
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # 上键
            self.hero.upanddown = -10

        elif keys[pygame.K_s]:  # 下键
            self.hero.upanddown = 10

        elif keys[pygame.K_a]:  # 左键
            self.hero.speed = -10  # 向左移动

        elif keys[pygame.K_d]:  # 右键
            self.hero.speed = 10  # 向右移动

        else:
            self.hero.speed = 0
            self.hero.upanddown = 0

        # 监听事件发生
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == ENEMY_EVENT:
                # print('敌机出场')
                # 实列化敌机对象
                enemy = plan_sprite.Enemy()
                self.enemy_group.add(enemy)
            elif event.type == pygame.QUIT:
                sys.exit()
            elif event.type == FIRE:
                # print('fire')
                self.hero.fire()

    # 碰撞检测
    def check_collide(self):
        # 子弹碰撞敌机
        rel = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, False)
        if rel:
            for value in rel.values():
                e = value[0]
                e.blood -= 1
                if e.blood == 0:
                    e.kill()

        # 敌机碰撞英雄
        rel2 = pygame.sprite.groupcollide(self.enemy_group, self.hero_group, True, True)
        if rel2:
            pygame.quit()

    # 更新/绘制精灵组
    def update_sprite(self):
        # 更新绘制背景精灵组
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        # 更新绘制敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新绘制英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 更新绘制子弹精灵组
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def start_game(self):
        pass
        while 1:
            self.clock.tick(60)

            self.event_handler()

            self.check_collide()

            self.update_sprite()

            pygame.display.update()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
