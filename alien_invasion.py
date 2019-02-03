import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	"""运行游戏"""
	pygame.init()		# 初始化
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))		# 初始化屏幕用于显示，返回surface
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	bullets = Group()		# 创建一个存储子弹的编组
	while True:
		# 游戏主循环
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
