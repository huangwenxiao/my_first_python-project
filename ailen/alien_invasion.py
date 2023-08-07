import sys

import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    """management of game"""

    def __init__(self):
        """Initialization of game"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #创建一个用于储存游戏统计信息的实例
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """start the cycle """
        while True:
            self._check_events()
            self.ship.update()
            self._check_update_screen()
            self.clock.tick(60)
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()

    def _check_events(self):
        # 监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)


    def _check_update_screen(self):
        # 重绘屏幕刷新
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # 让最新绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(120)
    def _update_bullets(self):
        """更新子弹位置"""
        # 子弹删除术
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        #检查是否有子弹击中了外星人
        #如果是，就删除响应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            #删除现有的子弹并创建一个新的舰队



    def _check_keydown_events(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DELETE :
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_event(self,event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _fire_bullet(self):
        """创建子弹加入到Bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _create_fleet(self):
        """创建一个外星舰队"""
        #创建一个外星人
        alien = Alien(self)
        self.aliens.add(alien)
        #创建一个外星人，再不断添加，直到没有空间可以添加
        #外星人的间距为外星人的宽度和外星人的高度
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #添加一行外星人后，充值x并递增y值
            current_x = alien_width
            current_y +=2 * alien_height

    def _create_alien(self, x_position,y_position):
        """创建一个外星人并将其放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        """检查外星人和飞船之间的碰撞"""

    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船和外星人碰撞"""
        #将ship_limit -1
        self.stats.ships_left -=1
        #清空外外星人和子弹列表
        self.bullets.empty()
        self.aliens.empty()

        #创建一个新的外星舰队，并将飞船再放置与屏幕下端中间
        self._create_fleet()
        self.ship.center_ship()
        #暂停
        sleep(0.5)

    def center_ship(self):
        """将飞船放在屏幕中央底部"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)




if __name__ == '__main__':
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
