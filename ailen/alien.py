import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """单个外星人"""
    def __init__(self,ai_game):
        """初始化外星人并设置其位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        """加载外星人图像并设置其rect属性"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人一开始都在屏幕的左上方附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #储存外星人的精确水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """检查外星人位于屏幕边缘与否，是就返回true"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """向左右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

