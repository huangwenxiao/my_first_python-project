import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """初始化按键属性"""
        self.screen =ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #设置按键属性
        self.width, self.height=200,50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #创建案件的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        #按键的标签只需要创建一次
        self._prep_msg(msg)
    def _prep_msg(self, msg):
      """将msg渲染为图像，并在使其在按键上居中"""
      self.msg_image = self.font.render(msg,True,self.text_color, self.button_color)
      self.msg_image_rect = self.msg_image.get_rect()
      self.msg_image_rect.center = self.rect.center
    def drew_button(self):
        """绘制一个按键再填入文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)