import pygame
import settings

class Ship:
    """管理飞船"""
    def __init__(self, ai_game):
        """初始化飞船"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #每艘飞船都绘制在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        #储存一个浮点数
        self.x=float(self.rect.x)

        #移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船属性x的值，而不是外接矩形
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # 根据self.x来更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
