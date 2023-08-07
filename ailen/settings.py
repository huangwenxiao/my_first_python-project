class Settings:

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5.5
        #子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10
        # 外星人设置
        self.alien_speed = 1.0
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动速度,为-1表示向左移动
        self.fleet_direction = 1
