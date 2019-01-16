import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	# 初始化游戏，创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")		# 设置标题
	bg_color = (230,230,230)		# 设置背景色
	# 创建一艘飞船
	ship = Ship(screen)

	# 游戏主循环
	while True:

		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# 每次循环时都重绘屏幕
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		# 最近绘制的屏幕可见
		pygame.display.flip()

run_game()
