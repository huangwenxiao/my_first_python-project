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

        self.ship_limit = 3
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动速度,为-1表示向左移动
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.alien_points = 50
    def initialize_dynamic_settings(self):
        """初始化随游戏变化而进行的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.5

        #fleet_drection为1表示右，为-1表示左
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        """提高速度的值"""
        self.ship_speed *=self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *=self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
        print(self.alien_points)
